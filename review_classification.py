"""Split the existing sample or validate, combine, and evaluate human reviews."""
import argparse
import csv
import json
from pathlib import Path

LABELS = (
    "individual_material", "service_or_works", "broad_tender_package",
    "administrative_notice", "broad_tender_title", "unclassified_or_other",
)
HUMAN_FIELDS = {"human_label", "usable_for_matching", "reviewer_note"}


def read_csv(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        fields = reader.fieldnames
        if not fields or len(fields) != len(set(fields)):
            raise ValueError(f"{path}: missing or duplicate headers")
        rows = list(reader)
    if any(None in row or None in row.values() for row in rows):
        raise ValueError(f"{path}: malformed CSV row")
    return fields, rows


def reference(path):
    fields, rows = read_csv(path)
    if not (HUMAN_FIELDS | {"corpus_id", "predicted_category"}) <= set(fields):
        raise ValueError("Reference is missing required fields")
    ids = [row["corpus_id"] for row in rows]
    if not rows or any(not key.strip() for key in ids) or len(ids) != len(set(ids)):
        raise ValueError("Reference has empty or duplicate corpus_ids")
    if any(row["predicted_category"] not in LABELS for row in rows):
        raise ValueError("Reference contains invalid predicted categories")
    return fields, rows


def write_csv(path, fields, rows):
    with Path(path).open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def split_review(source, destination):
    fields, rows = reference(source)
    if len(rows) != 400:
        raise ValueError("Expected the existing 400-row review sample")
    if any(row[key] for row in rows for key in HUMAN_FIELDS):
        raise ValueError("Reference contains human entries; refusing to create blank copies")
    destination = Path(destination)
    # A new directory prevents accidental overwrites of any reviewer work.
    destination.mkdir(parents=True, exist_ok=False)
    sizes = []
    for index in range(6):
        batch = rows[index::6]
        write_csv(destination / f"review_{index + 1:02d}.csv", fields, batch)
        sizes.append(len(batch))
    return {"review_rows": len(rows), "batch_sizes": sizes}


def combine_review(source, files):
    fields, originals = reference(source)
    expected = {row["corpus_id"]: row for row in originals}
    collected = {}
    if len(files) != 6:
        raise ValueError("Provide exactly six review files")
    for path in files:
        headers, rows = read_csv(path)
        if headers != fields:
            raise ValueError(f"{path}: headers differ from the reference")
        for row in rows:
            key = row["corpus_id"]
            if key not in expected:
                raise ValueError(f"Unknown or empty corpus_id: {key!r}")
            if key in collected:
                raise ValueError(f"Duplicate corpus_id: {key}")
            for field in fields:
                if field not in HUMAN_FIELDS and row[field] != expected[key][field]:
                    raise ValueError(f"{key}: changed source field {field}")
                if field in HUMAN_FIELDS and expected[key][field] and row[field] != expected[key][field]:
                    raise ValueError(f"{key}: changed existing human entry {field}")
            if row["human_label"] not in ("", *LABELS):
                raise ValueError(f"{key}: invalid human_label {row['human_label']!r}")
            if row["usable_for_matching"] not in ("", "TRUE", "FALSE"):
                raise ValueError(f"{key}: usable_for_matching must be blank, TRUE, or FALSE")
            collected[key] = row
    missing = sorted(set(expected) - set(collected))
    if missing:
        raise ValueError(f"Missing corpus_ids ({len(missing)}): {', '.join(missing)}")
    rows = [collected[row["corpus_id"]] for row in originals]
    labeled = [row for row in rows if row["human_label"]]
    report = {
        "total_rows": len(rows), "labeled_rows": len(labeled),
        "unlabeled_rows": len(rows) - len(labeled),
        "usability_entered_rows": sum(bool(row["usable_for_matching"]) for row in rows),
        "status": "awaiting_labels" if not labeled else ("complete" if len(labeled) == len(rows) else "partial"),
        "scope": "Stratified review sample only; not an estimate of full-corpus performance.",
    }
    if labeled:
        report["metrics_scope"] = "Only rows with human_label; blank labels are excluded. Null means zero denominator."
        report["by_category"] = {}
        for category in LABELS:
            tp = sum(row["human_label"] == category and row["predicted_category"] == category for row in labeled)
            predicted = sum(row["predicted_category"] == category for row in labeled)
            support = sum(row["human_label"] == category for row in labeled)
            report["by_category"][category] = {
                "true_positive": tp, "false_positive": predicted - tp,
                "false_negative": support - tp, "support": support,
                "precision": tp / predicted if predicted else None,
                "recall": tp / support if support else None,
            }
    return fields, rows, report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", default="reports/classification_review.csv")
    commands = parser.add_subparsers(dest="command", required=True)
    split = commands.add_parser("split")
    split.add_argument("--output-dir", default="reports/review_batches")
    combine = commands.add_parser("combine")
    combine.add_argument("files", nargs="+", type=Path)
    combine.add_argument("--output-dir", required=True, type=Path,
                         help="New directory for combined CSV and metrics JSON; existing paths are refused")
    args = parser.parse_args()
    try:
        if args.command == "split":
            report = split_review(args.reference, args.output_dir)
        else:
            fields, rows, report = combine_review(args.reference, args.files)
            args.output_dir.mkdir(parents=True, exist_ok=False)
            write_csv(args.output_dir / "classification_review_combined.csv", fields, rows)
            (args.output_dir / "review_metrics.json").write_text(
                json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8")
        print(json.dumps(report, indent=2, allow_nan=False))
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Review validation failed: {exc}\n")


if __name__ == "__main__":
    main()
