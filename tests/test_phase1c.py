"""Synthetic annotations below are test fixtures only, never project labels."""
import csv
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import pandas as pd

from curate_material_candidates import audit_overlap_deep, strict_json_value
from review_classification import combine_review, read_csv, split_review, write_csv

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "reports/classification_review.csv"


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.batches = self.directory / "batches"
        split_review(REFERENCE, self.batches)
        self.files = sorted(self.batches.glob("*.csv"))

    def change(self, action):
        fields, rows = read_csv(self.files[0])
        action(rows)
        with self.files[0].open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def test_split_and_blank_combine(self):
        fields, rows, report = combine_review(REFERENCE, self.files)
        self.assertEqual(rows, read_csv(REFERENCE)[1])
        self.assertEqual([len(read_csv(p)[1]) for p in self.files], [67, 67, 67, 67, 66, 66])
        self.assertEqual(report["status"], "awaiting_labels")
        self.assertNotIn("by_category", report)
        self.assertNotIn("accuracy", report)
        self.assertTrue(all(not row[k] for row in rows for k in ("human_label", "reviewer_note", "usable_for_matching")))

    def test_duplicate(self):
        self.change(lambda rows: rows.append(rows[0].copy()))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            combine_review(REFERENCE, self.files)

    def test_missing(self):
        self.change(lambda rows: rows.pop())
        with self.assertRaisesRegex(ValueError, "Missing corpus_ids"):
            combine_review(REFERENCE, self.files)

    def test_unknown(self):
        self.change(lambda rows: rows[0].update(corpus_id="unknown"))
        with self.assertRaisesRegex(ValueError, "Unknown"):
            combine_review(REFERENCE, self.files)

    def test_invalid_label(self):
        self.change(lambda rows: rows[0].update(human_label="material"))
        with self.assertRaisesRegex(ValueError, "invalid human_label"):
            combine_review(REFERENCE, self.files)

    def test_invalid_usability(self):
        self.change(lambda rows: rows[0].update(usable_for_matching="yes"))
        with self.assertRaisesRegex(ValueError, "usable_for_matching"):
            combine_review(REFERENCE, self.files)

    def test_source_tampering(self):
        self.change(lambda rows: rows[0].update(source_url="changed"))
        with self.assertRaisesRegex(ValueError, "changed source field"):
            combine_review(REFERENCE, self.files)

    def test_partial_metrics_and_zero_denominators(self):
        # Use a separate tiny synthetic reference to make the expected ratios explicit.
        fields = read_csv(REFERENCE)[0]
        rows = []
        for index, predicted in enumerate(["individual_material", "individual_material", "service_or_works"]):
            row = dict.fromkeys(fields, "")
            row.update(corpus_id=str(index), predicted_category=predicted)
            rows.append(row)
        source = self.directory / "reference.csv"
        write_csv(source, fields, rows)
        paths = []
        for index in range(6):
            path = self.directory / f"synthetic_{index}.csv"
            batch = []
            if index < 3:
                row = rows[index].copy()
                row["human_label"] = ["individual_material", "service_or_works", ""][index]
                batch.append(row)
            write_csv(path, fields, batch)
            paths.append(path)
        _, _, report = combine_review(source, paths)
        self.assertEqual(report["status"], "partial")
        self.assertEqual(report["labeled_rows"], 2)
        material = report["by_category"]["individual_material"]
        self.assertEqual(material["precision"], 0.5)
        self.assertEqual(material["recall"], 1.0)
        service = report["by_category"]["service_or_works"]
        self.assertIsNone(service["precision"])
        self.assertEqual(service["recall"], 0.0)
        json.dumps(report, allow_nan=False)

    def test_complete_metrics(self):
        for path in self.files:
            fields, rows = read_csv(path)
            for row in rows:
                row["human_label"] = row["predicted_category"]
            with path.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
        report = combine_review(REFERENCE, self.files)[2]
        self.assertEqual(report["status"], "complete")
        self.assertEqual(report["labeled_rows"], 400)
        for metrics in report["by_category"].values():
            if metrics["support"]:
                self.assertEqual(metrics["precision"], 1)
                self.assertEqual(metrics["recall"], 1)

    def test_preserve_annotations_and_no_overwrite(self):
        with self.assertRaises(FileExistsError):
            split_review(REFERENCE, self.batches)
        fields, rows = read_csv(REFERENCE)
        rows[0]["reviewer_note"] = "Existing human note"
        path = self.directory / "annotated.csv"
        write_csv(path, fields, rows)
        with self.assertRaisesRegex(ValueError, "human entries"):
            split_review(path, self.directory / "new")
        with self.assertRaisesRegex(ValueError, "changed existing human entry"):
            combine_review(path, self.files)

    def test_cli_no_metrics_and_overwrite_refusal(self):
        output = self.directory / "result"
        command = [sys.executable, str(ROOT / "review_classification.py"), "--reference", str(REFERENCE),
                   "combine", "--output-dir", str(output), *map(str, self.files)]
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)
        report = json.loads((output / "review_metrics.json").read_text())
        self.assertNotIn("by_category", report)
        self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)

    def test_curation_preserves_existing_review_bytes(self):
        reports = self.directory / "reports"
        reports.mkdir()
        fields, rows = read_csv(REFERENCE)
        rows[0]["reviewer_note"] = "Synthetic preservation test note"
        rows[0]["human_label"] = "individual_material"
        review = reports / "classification_review.csv"
        write_csv(review, fields, rows)
        before = review.read_bytes()
        result = subprocess.run([
            sys.executable, str(ROOT / "curate_material_candidates.py"),
            "--data-dir", str(ROOT / "data/raw/huggingface"),
            "--reports-dir", str(reports), "--processed-dir", str(self.directory / "processed")
        ], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(review.read_bytes(), before)
        def reject_constant(value):
            raise ValueError(value)
        json.loads((reports / "curation_report.json").read_text(), parse_constant=reject_constant)


class AuditTests(unittest.TestCase):
    def test_strict_json_nonfinite(self):
        value = {"nested": [float("nan"), float("inf"), -float("inf"), pd.NA, 2]}
        self.assertEqual(json.loads(json.dumps(strict_json_value(value), allow_nan=False)),
                         {"nested": [None, None, None, None, 2]})

    def test_measured_audit(self):
        corpus = pd.DataFrame({"description": ["Pump", "Valve"], "source_url": ["https://example.invalid", None]})
        ntpc = pd.DataFrame({"item_text": ["Pump.", "Unmatched"]})
        iocl = pd.DataFrame({"item_description": ["Valve", "X"], "quantity": [None, None],
                             "unit": [None, None], "estimated_value_rs_crores": [None, None]})
        result = audit_overlap_deep(corpus, ntpc, iocl)
        self.assertEqual(result["ntpc_audit"]["possible_overlap_count"], 1)
        self.assertEqual(result["ntpc_audit"]["unmatched_count"], 1)
        self.assertEqual(result["iocl_audit"]["unmatched_description_length_lt_8_count"], 1)
        self.assertEqual(result["provenance_coverage"]["corpus"]["source_url"]["nonempty_rows"], 1)
        self.assertFalse(result["provenance_coverage"]["corpus"]["document_url"]["column_present"])
        json.dumps(result, allow_nan=False)

    def test_empty_audit(self):
        corpus = pd.DataFrame(columns=["description"])
        ntpc = pd.DataFrame(columns=["item_text"])
        iocl = pd.DataFrame(columns=["item_description", "quantity", "unit", "estimated_value_rs_crores"])
        result = audit_overlap_deep(corpus, ntpc, iocl)
        self.assertIsNone(result["ntpc_audit"]["exact_overlap_pct"])
        json.dumps(result, allow_nan=False)


if __name__ == "__main__":
    unittest.main()
