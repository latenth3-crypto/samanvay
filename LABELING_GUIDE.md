# SIH 26099: Dataset Labeling & Review Guide
## Phase 1B: Material Classification & Curation Guidelines

This document establishes the official labeling definitions, decision rules, and boundary criteria for human review of procurement item descriptions in **SIH26099: AI-Driven Standardization & Harmonization of Material Codes Across CPSEs**.

---

## 1. Overview & Objectives

In Phase 1, automated rule heuristics classified 21,513 raw descriptions from three CPSEs (**Oil India Limited**, **NTPC Limited**, and **Indian Oil Corporation Limited**) into functional procurement types. 

The review sample (`reports/classification_review.csv`, 400 rows) is designed for human validation. Human annotators will evaluate the automated predictions by completing three blank columns:
- `human_label`: The true category of the record.
- `usable_for_matching`: Boolean (`TRUE` or `FALSE`) indicating whether this record should be included in the downstream material-matching and entity-resolution models.
- `reviewer_note`: Optional explanation of edge cases, ambiguities, or reasoning.

---

## 2. Category Definitions

### 2.1 `individual_material` (Physical Goods & Materials)
- **Definition:** The record describes a discrete physical good, piece of industrial equipment, component, spare part, bulk commodity, chemical, consumable, or tool.
- **Scope:**
  - Loose equipment: Pumps, valves, compressors, transformers, motors, generators, boilers, heat exchangers, vessels, tanks.
  - Piping and tubulars: Line pipes, casing, tubing, drill pipes, flanges, fittings (elbows, tees, reducers), gaskets, mechanical seals.
  - Electrical & Instrumentation: Cables, conductors, switchgear, breakers (VCB/MCCB), busbars, transmitters, pressure gauges, flow meters, sensors, thermocouples.
  - Raw materials & consumables: Structural steel (plates, angles, beams), fasteners (bolts, nuts, studs), cement, welding electrodes, greases, lube oils, chemicals, catalysts, drilling mud additives.
  - Catalog and GeM strings: Standardized item codes, specification strings with dimensions or ASTM/API/IS standards.
- **Criteria for `usable_for_matching = TRUE`:**
  - The description specifies an identifiable physical material or equipment item, even if short (e.g. `GATE VALVE - STEEL`, `Line Pipe 2" ERW`, `SODIUM HYDROXIDE`).
  - It contains sufficient semantic substance to align with standard taxonomy codes (e.g. UNSPSC or CPSE material master).
- **Positive Examples:**
  - `Line Pipe, 2" , ERW Galvanised, Screwed (Q3)`
  - `API 610 Centrifugal Pump`
  - `CABLE, PWR, 240MM2, 1C, STRANDED, AL, 11KV`
  - `SEAMLESS, SS, A312-TP304L, 80S, 15MM, PIPE`
  - `Procurement of Capital Spare, Complete Trip and Throttle valve`
  - `Supply of Stage cementing collars`

---

### 2.2 `service_or_works` (Services, Maintenance, Civil Works, Operations)
- **Definition:** The primary scope of the tender/contract is the provision of human labor, operational expertise, ongoing maintenance, equipment rental/hiring, civil construction, or transport.
- **Scope:**
  - Maintenance & Support: Annual Maintenance Contracts (AMC), Annual Rate Contracts (ARC), routine servicing, overhauling, troubleshooting.
  - Hiring / Rental: Hiring of vehicles, cranes, earthmoving machinery, manpower, security guards, transport equipment.
  - Civil & Structural Works: Construction of roads, boundary walls, foundations, buildings, grass cutting, horticulture, site leveling.
  - Specialized Industrial Services: Drilling services, mud logging, wireline logging, well testing, catering, housekeeping, courier, chartered accountancy, environmental survey.
- **Criteria for `usable_for_matching = FALSE`:**
  - Services are NOT physical materials and must not be assigned a material commodity code (e.g., UNSPSC Segment 14-49).
- **Positive Examples:**
  - `AMC for micro gas chromatograph`
  - `Biennial Maintenance Contract for Ash Pipe Lines Maintenance`
  - `Hiring of Services for Operation and Maintenance of Effluent Treatment Plant`
  - `Civil works for construction of Approach Road at Drill Site`
  - `Overhauling of 250 MW BHEL Steam Turbine`
  - `Security services for Central Godown`

---

### 2.3 `broad_tender_package` (Multi-Scope EPC & Facility Packages)
- **Definition:** High-level composite packages spanning an entire facility, multiple major subsystems, or turnkey engineering-procurement-construction (EPC) scopes.
- **Scope:**
  - Turnkey EPC contracts: `EPC Package for Development of 800MW/3200MWh Battery Energy Storage System (BESS)`
  - Balance of Plant (BOP) packages: `Balance of Plant (BOP) package for 2x660MW Supercritical Thermal Power Station`
  - Composite utility packages: `Turnkey execution of Solar PV Plant with 33KV pooling substation`
- **Criteria for `usable_for_matching = FALSE`:**
  - A broad package represents a multi-million-dollar capital facility rather than a single harmonizable material item code.

---

### 2.4 `administrative_notice` (Tender Procedural Updates)
- **Definition:** Procedural, legal, or administrative communications regarding tender milestones that do not describe materials or services.
- **Scope:**
  - Corrigenda, amendments, addenda: `Corrigendum No. 04 to GeM Tender GEM/2023/B/4051650`
  - Cancellations / Extensions: `Tender Cancellation Notice for Tender 9874563`, `Extension of Bid Submission Due Date`
  - Pre-bid meeting notices, Expression of Interest (EOI) calls, vendor empanelment notices.
- **Criteria for `usable_for_matching = FALSE`:**
  - Administrative records must be excluded from material harmonisation.

---

### 2.5 `broad_tender_title` (Generic High-Level Headings)
- **Definition:** Portal tender titles or NIT brief descriptions that are too high-level, vague, or multi-item to represent a specific material item.
- **Positive Examples:**
  - `Procurement of Mechanical Items for Refinery Shutdown 2026`
  - `Miscellaneous Hardware for Maintenance`
  - `1st Perpetual WSA WA Empanelment`
- **Criteria for `usable_for_matching = FALSE`:**
  - Too broad to map to a single commodity code.

---

### 2.6 `unclassified_or_other` (Residual / Uncertain / Ambiguous)
- **Definition:** Descriptions that cannot be reliably categorized due to severe truncation, raw table parsing artifacts, or extreme ambiguity.
- **Positive Examples:**
  - `1236/1231` (PDF table column misalignments)
  - `(1) TRANSPORE 5 CM (1) TRANSPORE 5 CM` (repetition noise)
  - Isolated numbers or uninterpretable abbreviations.
- **Criteria for `usable_for_matching = FALSE`:**
  - Corrupt or ambiguous strings should not be matched.

---

## 3. Boundary Resolution Guidelines

When a description sits on the boundary between two categories, use these decision rules:

### Boundary 1: "Supply and Installation" / "Supply and Commissioning"
- **Rule:**
  - If the tender is for a **discrete equipment item** where installation is an incidental vendor obligation (e.g. `Procurement & Installation of 98 Inch Display`, `Supply and Installation of 11KV Switchgear Panel`), label as **`individual_material`** and set `usable_for_matching = TRUE`.
  - If the tender is a **broad engineering/civil contract** involving major site fabrication or multi-system construction (e.g. `Design, fabrication, supply and erection of Geodesic Aluminum Dome Roof`, `Design, Supply and Erection of Prefabricated Closed Store including all Civil work`), label as **`service_or_works`** or **`broad_tender_package`** and set `usable_for_matching = FALSE`.

### Boundary 2: "AMC / Maintenance / Repair of [Equipment]"
- **Rule:**
  - Although equipment words like "pump", "valve", "turbine", or "pipeline" are present, the transaction is **purchasing maintenance labor/service**, not the physical machine itself.
  - Label as **`service_or_works`** and set `usable_for_matching = FALSE`.

### Boundary 3: "Supply of [Material] for [Service Water / Utility System]"
- **Rule:**
  - Distinguish between the **service industry noun** and **utility system names**. "Service water", "service air", and "service valve" are standard utility systems in thermal power plants and refineries.
  - If the procurement verb is `Supply of valves for service water system`, the item is **valves** (physical material).
  - Label as **`individual_material`** and set `usable_for_matching = TRUE`.

### Boundary 4: Engineering Standards & Technical Attributes
- **Rule:**
  - If a description contains recognized engineering standards (API, ASTM, ASME, IS, DIN, ANSI) or dimensions/grades (e.g. `API 6D Ball Valves`, `Seamless SS A312-TP304L Pipe`), this is a strong positive signal of a genuine material item.
  - Label as **`individual_material`** and set `usable_for_matching = TRUE`.

---

## 4. Review Workflow Instructions

1. Open `reports/classification_review.csv` in Excel, LibreOffice Calc, or your preferred CSV editor.
2. For each row:
   - Read `description`, `organization`, `source_url`, and `rule_fired`.
   - In `human_label`, enter one of: `individual_material`, `service_or_works`, `broad_tender_package`, `administrative_notice`, `broad_tender_title`, or `unclassified_or_other`.
   - In `usable_for_matching`, enter `TRUE` if the record is suitable for training/evaluating the material code harmonizer, or `FALSE` otherwise.
   - In `reviewer_note`, add brief notes if the case is borderline or illustrates a recurring issue.
3. Save the completed file back to `reports/classification_review.csv`.
