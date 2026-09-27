# SIH 26099: Phase 1 ? Dataset Foundation, Profiling & Curation

This repository contains **Phase 1** of **SIH26099: AI-Driven Standardization & Harmonization of Material Codes Across CPSEs**.

In accordance with Phase 1 scope requirements:
- **Phase 1A Scope:** Data acquisition, schema auditing, material vs. service filtering assessment, cross-file overlap detection, and statistical profiling.
- **Phase 1B Scope:** Validation of material classification, creation of a stratified review sample (400 records), curation of provisional material candidates (`data/processed/material_candidates.csv`), and deep provenance overlap audit.
- **Out of Scope for Phase 1:** No matching models, APIs, databases, or UIs are built. No synthetic CPSE material codes or hypothetical accuracy metrics are created.

---

## 1. Quick Start (Windows PowerShell)

Open Windows PowerShell in the project directory:

```powershell
# 1. Install required dependencies
py -m pip install -r requirements.txt

# 2. (Optional) Re-download raw files from Hugging Face if needed
py download_data.py

# 3. Run Phase 1A: Master Data Profiler
py profile_data.py

# 4. Run Phase 1B: Material Curation & Stratified Review Pipeline
py curate_material_candidates.py
```

*(Note: On systems where `python` is aliased directly, you can use `python` instead of `py`.)*

---

## 2. Dataset Architecture

### A. Raw Untouched Datasets (`data/raw/huggingface/`)
Preserved byte-for-byte in their original raw format:

| File Name | Rows | Columns | Size | Description |
|---|---|---|---|---|
| `material_description_corpus.csv` | **21,513** | 15 | 6.11 MB | Master working corpus (OIL India, NTPC, IOCL) |
| `ntpc_material_items.csv` | **486** | 7 | 54.4 KB | Granular line items extracted from NTPC tender PDFs |
| `iocl_procurement_plan_items.csv` | **1,224** | 9 | 180.5 KB | Extracted lines from IOCL Future Procurement Plan |

See [SOURCES.md](SOURCES.md) for full licensing details (CC-BY-4.0), download URLs, SHA-256 hashes, and provenance notes.

### B. Curated Working Dataset (`data/processed/`)
- **`data/processed/material_candidates.csv`**: **9,245** provisional individual material records isolated from the main corpus. Each record is enriched with derived major item categories (14 industrial domains) and audited for 6 discrete technical detail dimensions (size, material grade, engineering standard, voltage, pressure class, model/part number).

---

## 3. Human Review & Annotation (`reports/`)

- **`reports/classification_review.csv`**: Stratified sample of **400 records** across all 3 CPSEs, 6 predicted classes, major description kinds, and 7 boundary conditions (e.g. `supply and installation`, `AMC of pumps`, engineering standards). Includes blank columns for `human_label`, `reviewer_note`, and `usable_for_matching`.
- **`LABELING_GUIDE.md`**: Comprehensive human labeling guidelines providing clear definitions, decision boundaries, and concrete examples for annotators.

---

## 4. Reports & Audit Deliverables

1. **`reports/data_profile.json`**: Machine-readable JSON profiling all files, missing values, duplicates, and initial breakdowns.
2. **`reports/data_profile.md`**: Master profiling Markdown report.
3. **`reports/curation_report.md`**: Detailed Phase 1B curation and overlap audit report.
4. **`reports/curation_report.json`**: Machine-readable curation statistics and technical attribute distributions.
5. **`reports/sample_records.csv`**: Initial 42-record representative sample from Phase 1A.

---

## 5. Key Metrics Summary

- **Total Raw Records Across 3 Files:** `23,223`
- **Global Unique Descriptions:** `17,459`
- **Material vs. Service Assessment:**
  - **Individual Materials:** **9,245** (42.97%)
  - **Broad Tenders & Services:** **12,268** (57.03%)
- **Technical Attribute Density:** **2,911** material candidates (31.49%) possess explicit technical engineering attributes (dimensions, grades, standards, ratings, pressure classes, or catalog numbers).
- **Cross-File Overlap Audit:**
  - NTPC Items: 100% provenance in main corpus (462 verbatim, 24 with trailing punctuation stripped). 0 genuinely new items omitted.
  - IOCL Items: 97.39% provenance in main corpus (1,147 verbatim, 45 with trailing punctuation stripped). Exactly 32 valid items were omitted from the main corpus table purely due to an upstream 8-character filter (e.g. `Boiler`, `Valves`, `Filters`, `DG Set`).
  - NTPC vs. IOCL: 0 verbatim common descriptions (completely disjoint domain vocabularies).
