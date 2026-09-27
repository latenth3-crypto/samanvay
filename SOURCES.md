# Data Sources & Provenance (Phase 1)

This document records the provenance, download information, license, and purpose of all raw dataset files acquired for **SIH 26099: AI-Driven Standardization & Harmonization of Material Codes Across CPSEs**.

---

## 1. Primary Source Repository

- **Repository URL:** [https://huggingface.co/datasets/Prasenjeet25/sih26099-cpse-material-codes](https://huggingface.co/datasets/Prasenjeet25/sih26099-cpse-material-codes)
- **Repository Title:** SIH 26099 ? CPSE Material Code Harmonisation Dataset
- **Stated License:** **CC-BY-4.0** (Creative Commons Attribution 4.0 International)
- **Dataset Collection Date:** 2026-09-08 (by dataset author)
- **Local Download Date:** 2026-09-26T23:01:52+05:30
- **Raw Storage Location:** `data/raw/huggingface/` (preserved byte-for-byte unchanged)

---

## 2. Acquired Files & Specifications

All files were downloaded directly from the `data/processed/extracted_items/` directory of the Hugging Face repository and stored under `data/raw/huggingface/`:

### 2.1 `material_description_corpus.csv`
- **Source Path:** `data/processed/extracted_items/material_description_corpus.csv`
- **Download URL:** [https://huggingface.co/datasets/Prasenjeet25/sih26099-cpse-material-codes/resolve/main/data/processed/extracted_items/material_description_corpus.csv](https://huggingface.co/datasets/Prasenjeet25/sih26099-cpse-material-codes/resolve/main/data/processed/extracted_items/material_description_corpus.csv)
- **Local Path:** `data/raw/huggingface/material_description_corpus.csv`
- **File Size:** 6,257,252 bytes (6,110.6 KB)
- **SHA-256 Checksum:** `58c837ff0dab3336085bc6e7e984d7ed060b175a7df7440ba3dc037d7f107c95`
- **Row Count:** 21,513 rows
- **Columns (15):** `corpus_id`, `organization`, `source_system`, `source_section`, `tender_reference`, `tender_id`, `description`, `description_kind`, `item_type_hint`, `quantity`, `unit`, `location`, `product_category`, `document_url`, `source_url`
- **Purpose:** 
  The primary master working table consolidating public procurement descriptions across three major Indian CPSEs: **Oil India Limited** (18,950 records), **NTPC Limited** (1,843 records), and **Indian Oil Corporation Limited** (720 records). Each row represents a real procurement line with stable identifiers, publisher metadata, provenance URLs, and categorization fields.

### 2.2 `ntpc_material_items.csv`
- **Source Path:** `data/processed/extracted_items/ntpc_material_items.csv`
- **Download URL:** [https://huggingface.co/datasets/Prasenjeet25/sih26099-cpse-material-codes/resolve/main/data/processed/extracted_items/ntpc_material_items.csv](https://huggingface.co/datasets/Prasenjeet25/sih26099-cpse-material-codes/resolve/main/data/processed/extracted_items/ntpc_material_items.csv)
- **Local Path:** `data/raw/huggingface/ntpc_material_items.csv`
- **File Size:** 55,715 bytes (54.41 KB)
- **SHA-256 Checksum:** `a175d7783728e8cff7878b30dbcd401a41fcfe2e4d703d1fdccfe634951ff8bb`
- **Row Count:** 486 rows
- **Columns (7):** `nit_id`, `doc_name`, `pattern`, `item_text`, `quantity`, `unit`, `line_no`
- **Purpose:** 
  Granular line items pulled directly from NTPC Notice Inviting Tender (NIT) PDFs and text files. Contains semi-structured Government e-Marketplace (GeM) catalog strings, specification sentences, and bill-of-quantities (BOQ) lines along with line numbers and source document references.

### 2.3 `iocl_procurement_plan_items.csv`
- **Source Path:** `data/processed/extracted_items/iocl_procurement_plan_items.csv`
- **Download URL:** [https://huggingface.co/datasets/Prasenjeet25/sih26099-cpse-material-codes/resolve/main/data/processed/extracted_items/iocl_procurement_plan_items.csv](https://huggingface.co/datasets/Prasenjeet25/sih26099-cpse-material-codes/resolve/main/data/processed/extracted_items/iocl_procurement_plan_items.csv)
- **Local Path:** `data/raw/huggingface/iocl_procurement_plan_items.csv`
- **File Size:** 184,790 bytes (180.46 KB)
- **SHA-256 Checksum:** `6c132ca99a3181427300f77f73558e501aebba52ae4085af657781a4fe58ae17`
- **Row Count:** 1,224 rows
- **Columns (9):** `page`, `section`, `sl_no`, `item_description`, `quantity`, `unit`, `estimated_value_rs_crores`, `row_raw`, `source_pdf`
- **Purpose:** 
  Structured procurement line items extracted from IOCL's official 104-page Future Procurement Plan (FY 2025?26). Details projected equipment and material requirements (e.g. pressure vessels, pumps, catalysts, pipes, valves) with projected quantities, units, and estimated budgetary values in INR Crores.

---

## 3. Data Integrity & Provenance Policy

1. **Unchanged Raw Storage:** All downloaded files under `data/raw/huggingface/` remain bit-identical to the source Hugging Face repository snapshot.
2. **Provenance Preservation:** Every item retains its original CPSE publisher, document URL, source URL, tender reference, and extraction line identifier wherever provided by the source.
3. **No Synthetic Codes or Metrics:** In strict compliance with Phase 1 boundaries:
   - No CPSE material codes have been invented or assigned.
   - No synthetic ground-truth matches have been generated.
   - No accuracy figures or model predictions have been simulated.
