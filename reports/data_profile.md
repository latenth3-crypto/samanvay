# SIH 26099: Phase 1 Data Profiling & Quality Assessment Report

> **Dataset Source:** [Prasenjeet25/sih26099-cpse-material-codes](https://huggingface.co/datasets/Prasenjeet25/sih26099-cpse-material-codes)  
> **Stated License:** CC-BY-4.0  
> **Profile Generated:** 2026-09-27T10:16:30.135690  

## 1. Executive Summary & Headline Metrics

This report establishes the Phase 1 dataset foundation for the **AI-Driven Standardization & Harmonization of Material Codes Across CPSEs** (SIH26099). 
In strict conformance with Phase 1 boundaries, no matching models, APIs, databases, or synthetic ground-truth codes are constructed. 
Three primary extracted item datasets were downloaded, verified, and profiled:

| File Name | Role / Description | Rows | Columns | Size | Exact Duplicates | Null / Empty Rates |
|---|---|---|---|---|---|---|
| `material_description_corpus.csv` | Material Description Corpus (Main Table) | **21,513** | 15 | 6110.6 KB | 0 | Max: `unit` (98.15%) |
| `ntpc_material_items.csv` | NTPC Structured Material Items | **486** | 7 | 54.41 KB | 0 | Max: `quantity` (100.0%) |
| `iocl_procurement_plan_items.csv` | IOCL Procurement Plan Items | **1,224** | 9 | 180.46 KB | 0 | Max: `section` (93.95%) |

---

## 2. File-by-File Detailed Profile

### 2.1 `material_description_corpus.csv` (Material Description Corpus (Main Table))
- **Row Count:** 21,513
- **Column Count:** 15
- **File Size:** 6110.6 KB (6,257,252 bytes)
- **SHA-256 Checksum:** `58c837ff0dab3336085bc6e7e984d7ed060b175a7df7440ba3dc037d7f107c95`
- **Exact Duplicate Rows:** 0
- **Unique Descriptions:** 17,400 (4,113 duplicate description occurrences)

**Column Breakdown & Missing Values:**

| Column | Non-Empty Count | Missing / Empty | Missing % | Data Type |
|---|---|---|---|---|
| `corpus_id` | 21,513 | 0 | 0.0% | `object` |
| `organization` | 21,513 | 0 | 0.0% | `object` |
| `source_system` | 21,513 | 0 | 0.0% | `object` |
| `source_section` | 21,513 | 0 | 0.0% | `object` |
| `tender_reference` | 20,557 | 956 | 4.44% | `object` |
| `tender_id` | 2,055 | 19,458 | 90.45% | `object` |
| `description` | 21,513 | 0 | 0.0% | `object` |
| `description_kind` | 21,513 | 0 | 0.0% | `object` |
| `item_type_hint` | 6,349 | 15,164 | 70.49% | `object` |
| `quantity` | 484 | 21,029 | 97.75% | `object` |
| `unit` | 397 | 21,116 | 98.15% | `object` |
| `location` | 9,282 | 12,231 | 56.85% | `object` |
| `product_category` | 12,758 | 8,755 | 40.7% | `object` |
| `document_url` | 4,375 | 17,138 | 79.66% | `object` |
| `source_url` | 20,534 | 979 | 4.55% | `object` |

**Organisations Represented:**

| Organisation | Count | Share |
|---|---|---|
| **Oil India Limited** | 18,950 | 88.09% |
| **NTPC Limited** | 1,843 | 8.57% |
| **Indian Oil Corporation Limited** | 720 | 3.35% |

**Description Kinds / Patterns:**

| Kind / Pattern | Count | Share |
|---|---|---|
| `historical_tender` | 11,183 | 51.98% |
| `tender_detail` | 3,867 | 17.98% |
| `archived_tender` | 3,739 | 17.38% |
| `nit_brief_description` | 1,326 | 6.16% |
| `procurement_plan_item` | 508 | 2.36% |
| `doc_spec_sentence` | 374 | 1.74% |
| `tender_title` | 248 | 1.15% |
| `live_tender` | 138 | 0.64% |
| `doc_spec_string` | 41 | 0.19% |
| `work_description` | 33 | 0.15% |
| `doc_brief_description` | 23 | 0.11% |
| `corrigendum` | 23 | 0.11% |
| `doc_tender_title` | 10 | 0.05% |

**Sample Record:**
```json
{
  "corpus_id": "M000001",
  "organization": "Indian Oil Corporation Limited",
  "source_system": "iocl.com",
  "source_section": "Future Procurement Plan FY2025-26",
  "tender_reference": null,
  "tender_id": null,
  "description": "1236/1231",
  "description_kind": "procurement_plan_item",
  "item_type_hint": null,
  "quantity": "1233",
  "unit": null,
  "location": null,
  "product_category": null,
  "document_url": "data/raw/iocl/tenders/Future_Procurement_Plan25-26.pdf",
  "source_url": null
}
```

### 2.2 `ntpc_material_items.csv` (NTPC Structured Material Items)
- **Row Count:** 486
- **Column Count:** 7
- **File Size:** 54.41 KB (55,715 bytes)
- **SHA-256 Checksum:** `a175d7783728e8cff7878b30dbcd401a41fcfe2e4d703d1fdccfe634951ff8bb`
- **Exact Duplicate Rows:** 0
- **Unique Descriptions:** 445 (41 duplicate description occurrences)

**Column Breakdown & Missing Values:**

| Column | Non-Empty Count | Missing / Empty | Missing % | Data Type |
|---|---|---|---|---|
| `nit_id` | 486 | 0 | 0.0% | `object` |
| `doc_name` | 486 | 0 | 0.0% | `object` |
| `pattern` | 486 | 0 | 0.0% | `object` |
| `item_text` | 486 | 0 | 0.0% | `object` |
| `quantity` | 0 | 486 | 100.0% | `object` |
| `unit` | 0 | 486 | 100.0% | `object` |
| `line_no` | 486 | 0 | 0.0% | `object` |

**Description Kinds / Patterns:**

| Kind / Pattern | Count | Share |
|---|---|---|
| `spec_sentence` | 412 | 84.77% |
| `spec_string` | 41 | 8.44% |
| `brief_description` | 23 | 4.73% |
| `tender_title` | 10 | 2.06% |

**Sample Record:**
```json
{
  "nit_id": "28811",
  "doc_name": "28811_NIT_Download.txt",
  "pattern": "spec_sentence",
  "item_text": "11KV DG Sets, Fire Water Pump House, 33KV and 11KV Transmission Line,",
  "quantity": null,
  "unit": null,
  "line_no": "28"
}
```

### 2.3 `iocl_procurement_plan_items.csv` (IOCL Procurement Plan Items)
- **Row Count:** 1,224
- **Column Count:** 9
- **File Size:** 180.46 KB (184,790 bytes)
- **SHA-256 Checksum:** `6c132ca99a3181427300f77f73558e501aebba52ae4085af657781a4fe58ae17`
- **Exact Duplicate Rows:** 0
- **Unique Descriptions:** 522 (702 duplicate description occurrences)

**Column Breakdown & Missing Values:**

| Column | Non-Empty Count | Missing / Empty | Missing % | Data Type |
|---|---|---|---|---|
| `page` | 1,224 | 0 | 0.0% | `object` |
| `section` | 74 | 1,150 | 93.95% | `object` |
| `sl_no` | 1,224 | 0 | 0.0% | `object` |
| `item_description` | 1,224 | 0 | 0.0% | `object` |
| `quantity` | 1,123 | 101 | 8.25% | `object` |
| `unit` | 928 | 296 | 24.18% | `object` |
| `estimated_value_rs_crores` | 929 | 295 | 24.1% | `object` |
| `row_raw` | 1,224 | 0 | 0.0% | `object` |
| `source_pdf` | 1,224 | 0 | 0.0% | `object` |

**Description Kinds / Patterns:**

| Kind / Pattern | Count | Share |
|---|---|---|
| `(missing)` | 1,150 | 93.95% |
| `Capex Procurement Projected` | 58 | 4.74% |
| `Refineries` | 16 | 1.31% |

**Sample Record:**
```json
{
  "page": "1",
  "section": "Refineries",
  "sl_no": "1",
  "item_description": "Vessels/Drums/Tanks",
  "quantity": "99",
  "unit": "Nos.",
  "estimated_value_rs_crores": "108.06",
  "row_raw": "Vessels/Drums/Tanks | 99 | Nos. | 108.06",
  "source_pdf": "Future_Procurement_Plan25-26.pdf"
}
```

---

## 3. Main Corpus Detailed Breakdowns

### 3.1 Distribution by Organisation

| Organisation | Count | Percentage |
|---|---|---|
| **Oil India Limited** | 18,950 | 88.09% |
| **NTPC Limited** | 1,843 | 8.57% |
| **Indian Oil Corporation Limited** | 720 | 3.35% |

### 3.2 Distribution by Description Kind

| Description Kind | Count | Percentage | Provenance / Role |
|---|---|---|---|
| `historical_tender` | 11,183 | 51.98% | OIL India historical tender archives (dense material text) |
| `tender_detail` | 3,867 | 17.98% | OIL India scraped tender detail specifications |
| `archived_tender` | 3,739 | 17.38% | OIL India archived tender listings |
| `nit_brief_description` | 1,326 | 6.16% | NTPC Notice Inviting Tender summary descriptions |
| `procurement_plan_item` | 508 | 2.36% | IOCL Future Procurement Plan FY25-26 item lines |
| `doc_spec_sentence` | 374 | 1.74% | NTPC PDF-extracted technical specification sentences |
| `tender_title` | 248 | 1.15% | NTPC / IOCL portal listing titles |
| `live_tender` | 138 | 0.64% | OIL India live active tender notices |
| `doc_spec_string` | 41 | 0.19% | NTPC PDF-extracted GeM catalogue & BOQ spec strings |
| `work_description` | 33 | 0.15% | IOCL portal work descriptions distinct from title |
| `doc_brief_description` | 23 | 0.11% | NTPC PDF-extracted NIT brief description text |
| `corrigendum` | 23 | 0.11% | OIL India tender corrigenda / addenda notices |
| `doc_tender_title` | 10 | 0.05% | NTPC PDF-extracted document header tender titles |

### 3.3 Coarse Item Type Hints (`item_type_hint`)

The corpus includes coarse classification hints across 34 industrial equipment vocabularies:

| Item Type Hint | Count | Percentage |
|---|---|---|
| `(no_hint)` | 15,164 | 70.49% |
| `pipe` | 1,210 | 5.62% |
| `pump` | 925 | 4.3% |
| `tank` | 580 | 2.7% |
| `cable` | 330 | 1.53% |
| `steel` | 322 | 1.5% |
| `instrument` | 259 | 1.2% |
| `spares` | 246 | 1.14% |
| `chemical` | 236 | 1.1% |
| `valve` | 226 | 1.05% |
| `pipe fitting` | 200 | 0.93% |
| `compressor` | 184 | 0.86% |
| `safety valve` | 183 | 0.85% |
| `crane` | 181 | 0.84% |
| `transformer` | 150 | 0.7% |
| `motor` | 148 | 0.69% |
| `flange` | 141 | 0.66% |
| `gate valve` | 125 | 0.58% |
| `boiler` | 112 | 0.52% |
| `turbine` | 79 | 0.37% |
| *...other hints (15 categories)* | - | - |

---

## 4. Assessment: Individual Material vs. Broad Tender Titles & Services

### 4.1 Methodology & Filtering Rules

To determine which rows represent discrete physical materials suitable for code harmonisation versus administrative titles or services, 
an objective multi-stage classification hierarchy was evaluated. 
**Crucially, no raw rows have been deleted or filtered out; all 21,513 raw records remain preserved.**

1. **Rule 1 ? Administrative Notices:** Flags corrigenda, amendments, tender cancellations, pre-bid notices, or EOI notices lacking physical items.
2. **Rule 2 ? Multi-Scope Packages:** Flags comprehensive turnkey EPC packages, balance of plant (BOP), and composite works spanning entire facilities.
3. **Rule 3 ? Service / Works Contracts:** Identifies contracts for labor, maintenance (AMC/ARC), overhauls, civil works, hiring, security, catering, consultancy, and drilling services. A contextual exception retains phrases like `Supply of valves for service water system`.
4. **Rule 4 ? Extracted Document & Plan Lines:** Flags discrete specification sentences, GeM strings, and procurement plan items extracted directly from tender schedules.
5. **Rule 5 ? Coarse Taxonomy Hints:** Flags items possessing verified equipment hints (`pipe`, `valve`, `pump`, `cable`, etc.).
6. **Rule 6 ? Material Lexicon & Engineering Specifications:** Identifies items containing physical equipment keywords (tubing, casing, fasteners, bearings, tools, etc.) or technical engineering standards (ASTM, API, ASME, IS, mm, KV, HP, Class, PN, GeM `(Q3)` tags).
7. **Rule 7 ? Direct Supply Verbs:** Captures procurement descriptions starting with `Supply of`, `Procurement of`, or `Purchase of` for physical goods.
8. **Rule 8 ? Broad Tender Titles:** Identifies high-level tender titles and brief descriptions lacking granular material specifications.

### 4.2 Classification Results

| Category | Classification Meaning | Count | Share |
|---|---|---|---|
| **`individual_material`** | Individual Material | 9,245 | 42.97% |
| **`service_or_works`** | Service Or Works | 7,696 | 35.77% |
| **`unclassified_or_other`** | Unclassified Or Other | 3,463 | 16.1% |
| **`administrative_notice`** | Administrative Notice | 577 | 2.68% |
| **`broad_tender_title`** | Broad Tender Title | 429 | 1.99% |
| **`broad_tender_package`** | Broad Tender Package | 103 | 0.48% |

**Binary Material Suitability Assessment:**

| Assessment | Description | Count | Percentage |
|---|---|---|---|
| **Individual Material** | Discrete equipment, components, spare parts, chemicals, commodities | **9,245** | **42.97%** |
| **Broad Tender / Service** | Services, works, AMC/ARC, hiring, turnkey packages, administrative notices | **12,268** | **57.03%** |

---

## 5. Overlap & Provenance Audit

### 5.1 Cross-File Relationship & Double-Counting Check

The three raw files represent different extraction stages. To prevent double-counting during downstream analysis, the overlap structure was explicitly audited:

- **Total Raw Rows across the 3 files:** `23,223`  
- **Global Unique Descriptions:** `17,459`  
- **NTPC items in Main Corpus:** `462` of `486` (95.06%) match corpus descriptions directly. The corpus contains **448** deduplicated `doc_*` rows originating from NTPC tender PDFs.  
- **IOCL Procurement Plan items in Main Corpus:** `1,147` of `1,224` (93.71%) match corpus descriptions directly. The corpus contains **508** deduplicated `procurement_plan_item` records.  
- **Direct Cross-Intersection (NTPC vs. IOCL):** Exactly **0** common descriptions. NTPC power generation items and IOCL refinery items share zero verbatim descriptions.  

### 5.2 Provenance & Ground-Truth Integrity

- **URL & Document Links:** Fully preserved across all tables (`source_url`, `document_url`).
- **Original Identifiers:** Stable identifiers preserved including `corpus_id`, `tender_reference`, `tender_id`, `nit_id`, `doc_name`, `line_no`, `page`, `section`, and `sl_no`.
- **Integrity Guarantee:** In accordance with Phase 1 constraints, **no synthetic CPSE codes, ground-truth matches, or hypothetical accuracy scores have been invented**.

---

## 6. Generated Artifacts

1. `reports/data_profile.json`: Full machine-readable profiling statistics and distributions.
2. `reports/data_profile.md`: This comprehensive Markdown summary report.
3. `reports/sample_records.csv`: Representative dataset sample preserving all provenance columns.