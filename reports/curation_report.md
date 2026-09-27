# SIH 26099: Phase 1B Material Candidate Curation & Classification Audit Report

> **Dataset Foundation:** [Prasenjeet25/sih26099-cpse-material-codes](https://huggingface.co/datasets/Prasenjeet25/sih26099-cpse-material-codes)  
> **Scope:** Phase 1B Material Validation, Overlap Audit & Stratified Review Sample  
> **Generated At:** 2026-09-27T10:16:59.967417  

## 1. Executive Summary

In Phase 1B, the classification heuristics were validated across boundary cases and applied to isolate a **provisional working dataset of individual material candidates** (`data/processed/material_candidates.csv`). 
Crucially, all original raw records remain untouched in `data/raw/huggingface/`. 
A stratified human review sample of **400 records** (`reports/classification_review.csv`) has been produced alongside a standardized labeling guide (`LABELING_GUIDE.md`).

### Key Deliverable Figures:
- **Provisional Material Candidates:** **9,245** rows (42.97% of main corpus)
- **Stratified Review Sample:** **400** rows across all 3 CPSEs and 7 boundary conditions
- **Candidates with Technical Details:** **2,911** rows (31.49%)

---

## 2. Provisional Material Candidates Profile (`material_candidates.csv`)

### 2.1 Distribution by Organisation

| Organisation | Material Candidate Count | Share of Candidates |
|---|---|---|
| **Oil India Limited** | 7,763 | 83.97% |
| **NTPC Limited** | 897 | 9.7% |
| **Indian Oil Corporation Limited** | 585 | 6.33% |

### 2.2 Distribution by Description Kind

| Description Kind | Count | Share | Provenance Note |
|---|---|---|---|
| `historical_tender` | 4,493 | 48.6% | Main working corpus record |
| `tender_detail` | 1,633 | 17.66% | Main working corpus record |
| `archived_tender` | 1,581 | 17.1% | Main working corpus record |
| `procurement_plan_item` | 498 | 5.39% | Main working corpus record |
| `nit_brief_description` | 465 | 5.03% | Main working corpus record |
| `doc_spec_sentence` | 361 | 3.9% | Main working corpus record |
| `tender_title` | 97 | 1.05% | Main working corpus record |
| `live_tender` | 56 | 0.61% | Main working corpus record |
| `doc_spec_string` | 41 | 0.44% | Main working corpus record |
| `work_description` | 13 | 0.14% | Main working corpus record |
| `doc_brief_description` | 5 | 0.05% | Main working corpus record |
| `doc_tender_title` | 2 | 0.02% | Main working corpus record |

### 2.3 Major Item Categories (Lexical Domain Analysis)

Rather than relying on coarse hints alone, each description was categorized into standard industrial equipment domains:

| Major Item Category | Count | Percentage |
|---|---|---|
| **General / Unspecified Material** | 2,438 | 26.37% |
| **Pipes, Tubes & Casings** | 1,200 | 12.98% |
| **Electrical, Cables & Switchgear** | 1,138 | 12.31% |
| **Chemicals, Catalysts & Lubricants** | 1,072 | 11.6% |
| **Pumps & Pumping Systems** | 510 | 5.52% |
| **Structural Steel & Fasteners** | 467 | 5.05% |
| **Valves & Actuators** | 440 | 4.76% |
| **Tanks, Pressure Vessels & Heat Transfer** | 347 | 3.75% |
| **Instrumentation & Automation** | 339 | 3.67% |
| **Pipe Fittings & Flanges** | 338 | 3.66% |
| **Rotating Equipment, Turbines & Compressors** | 277 | 3.0% |
| **Safety, PPE & Workshop Tools** | 249 | 2.69% |
| **Drilling, Downhole & Wellhead** | 194 | 2.1% |
| **IT, Telecom & Office Equipment** | 167 | 1.81% |
| **Gaskets, Seals & Packings** | 69 | 0.75% |

### 2.4 Technical Specification Richness Audit

To support downstream entity resolution and material matching, records were audited for discrete technical attributes:

| Technical Attribute | Records with Attribute | Percentage of Candidates |
|---|---|---|
| **Size / Dimensions (mm, inch, NB, DN, OD)** | **1,219** | **13.19%** |
| **Material Grade (ASTM, API, IS, SS316, Corten)** | **143** | **1.55%** |
| **Engineering Standard (API, ASME, DIN, IS, ANSI, IEC, ISO)** | **513** | **5.55%** |
| **Voltage / Electrical Rating (KV, KVA, V, KW, HP)** | **683** | **7.39%** |
| **Pressure Class / Rating (Class 150/300, PN, bar, psi)** | **158** | **1.71%** |
| **Model / Part Number / Brand / Q-Tag** | **768** | **8.31%** |
| **ANY Useful Technical Detail Present** | **2,911** | **31.49%** |

---

## 3. Stratified Review Sample (`reports/classification_review.csv`)

A stratified set of **400** records was compiled for human review, incorporating quotas for difficult boundary cases:

### Breakdown by Boundary Flag:

| Boundary / Stratum Group | Sample Count | Review Purpose |
|---|---|---|
| `stratum:standard_record` | 231 | Validation of category boundaries |
| `boundary:engineering_standard` | 39 | Validation of category boundaries |
| `boundary:supply_and_installation` | 28 | Validation of category boundaries |
| `boundary:amc_or_maintenance_of_equipment` | 27 | Validation of category boundaries |
| `boundary:administrative_notice` | 24 | Validation of category boundaries |
| `boundary:short_or_numeric` | 24 | Validation of category boundaries |
| `boundary:turnkey_epc_package` | 20 | Validation of category boundaries |
| `boundary:service_utility_system` | 7 | Validation of category boundaries |

---

## 4. Deep Overlap & Provenance Audit

### 4.1 NTPC Material Items Overlap
- **Total Rows in File:** `486`
- **Exact Matches:** `462` (95.06%)
- **Matches after trailing punctuation strip:** `24` (4.94%)
- **Genuinely New Records:** `0` (0.0%)
- **Conclusion:** 100% of NTPC items (462 verbatim + 24 with trailing punctuation) have direct source provenance in the corpus. Zero genuinely new records were omitted.

### 4.2 IOCL Procurement Plan Items Overlap
- **Total Rows in File:** `1224`
- **Exact Matches:** `1147` (93.71%)
- **Matches after trailing punctuation strip:** `45` (3.68%)
- **Genuinely New Records:** `32` (2.61%)
- **Conclusion:** Exactly 32 records (2.61%) were excluded from the corpus purely because their description string length was < 8 characters (e.g. 'Boiler', 'Valves', 'Filters', 'GC-FID'). These are valid item lines with quantities and budget figures.

### 4.3 Cross-File Overlap (NTPC vs. IOCL)
- **Verbatim Common Descriptions:** `0`
- **Conclusion:** 0 common descriptions between NTPC and IOCL items; vocabularies represent distinct power vs refinery domains.

---

## 5. Limitations & Surprising Examples

1. **PDF Column Alignment Artifacts:** A small number of records (e.g. `1236/1231`) resulted from misaligned column headers in IOCL PDF tables. These are preserved in the raw data but isolated in `unclassified_or_other`.
2. **Medical & Hospital Procurement in CPSEs:** Both Oil India and NTPC operate internal hospitals and townships. Records like `Haemodialysis Machine (Q2)` and `(1) TRANSPORE 5 CM` are genuine public procurement items published by these CPSEs, not scraping errors.
3. **Incidental Installation Clauses:** Descriptions such as `Procurement & Installation of 98 Inch Display System` represent physical assets where installation is secondary. Our refined rules classify them as individual materials while routing turnkey capital packages (`EPC Package for Battery Storage`) to `broad_tender_package`.
4. **Character Cutoff Boundary:** Exactly 32 valid IOCL procurement plan records (e.g. `Boiler`, `Valves`, `Filters`, `DG Set`, `GC-FID`) were omitted from the main corpus table purely due to the upstream 8-character filter. Downstream models should ingest these directly from `iocl_procurement_plan_items.csv`.