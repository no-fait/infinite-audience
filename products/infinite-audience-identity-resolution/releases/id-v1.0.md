# Infinite Audience Identity Resolution & Enrichment v1.0

**Release Tag:** `id-v1.0`
**Release Date:** October 2026
**Specification:** v1.0 Baseline (independent of Graph and API versions; the production OpenAPI contract governs API requests and responses)

---

### 🎯 Product Release Baseline
We are proud to establish the official v1.0 baseline specification for **Infinite Audience Identity Resolution & Enrichment** — the deterministic, probabilistic, and spatial matching engine that connects customer records to durable identities and actionable intelligence across the Infinite Audience ecosystem.

This specification establishes the public product baseline, defining accepted input signals, configurable match options, the three-approach matching cascade, confirmed match levels, and 15 supported match types.

---

### 📥 Universal Multi-Value Input Contract
- **Multi-Touch Ingestion:** Send all known emails, phones, and addresses on a single customer record (`emails`, `phones`, `addresses`). Each value is evaluated as its own match point so no signal is left behind.
- **Privacy-Safe Pre-Hashed Signals:** Native support for 64-character SHA-256 hexadecimal hashes (`email_sha256`, `phone_sha256`) for environments that never expose raw contact information.
- **Smart Normalization:** Automatic handling of standard nicknames (*Bill* → *William*), compound first names (*Mary Beth*), generational suffixes (*Jr*, *III*), and highway/route naming variations (*Highway 42* vs. *NC-42*).
- **Life Stage & Name-Change Resilience:** Resolves adult individuals across post-marriage surname changes when first name, date of birth, and address agree.

---

### ⚙️ Configurable Matching Options
- **Context-Aware Spatial Modes:** Switch between `residential` (neighborhood and apartment complex moves), `work` (workplace-to-home commuter sheds), and `auto` (automatic commercial address routing).
- **Match Level Filtering:** Restrict accepted outcomes to specific levels (`I`, `H`, `D`, `S`, `A`) to match campaign standards.
- **Quality Safeguards:** Matching uses phase-specific acceptance rules; spatial matching requires at least `0.80` confidence. Scores are diagnostics, not measured accuracy probabilities.

---

### 🧠 Three-Approach Matching Cascade
1. **Deterministic Matching (Exact Links):** Rapid verification against linked identities in the graph, with smart handling of nicknames, address formatting, and date-of-birth verification.
2. **Probabilistic Matching (Weighted Agreement):** Weighs multi-attribute agreement across noisy data (typos, unit formats, neighboring zip codes) with strict veto guardrails preventing conflicting house numbers or generational mix-ups.
3. **Spatial Engine (Geographic Proximity):** Uses real-world geography and neighborhood density (urbanicity) to locate individuals who moved locally or submitted a workplace address, dynamically calibrated by name frequency.

---

### 🏷️ Match Levels & 15 Match Types Taxonomy
- **5 Confirmed Levels:** **I** (Individual), **H** (Household), **D** (Digital), **S** (Spatial), **A** (Address).
- **15 Supported Match Types:** Diagnostic reporting describing matching or direct ID lookup, including `graph_iag_person_id_match`, `graph_name_address_match`, `graph_name_email_match`, `graph_name_phone_match`, `graph_name_zip_dob_match`, `graph_first_dob_address_match`, `graph_fuzzy_street_match`, `probabilistic_name_address_match`, `graph_last_name_address_match`, `graph_email_match`, `graph_phone_match`, `spatial_match`, `graph_address_match`, `graph_last_name_email_match`, and `graph_last_name_phone_match`.

---

### 🛡️ Privacy & Customer Continuity
- **Organization-Scoped Salting:** Every resolved identity receives an `iag_person_id` salted to your organization, preventing direct ID comparison across organizations.
- **Tier 01 vs. Tier 02–05 IDs:** Clear distinction between resolved graph identities (Tier 01) and derived file-continuity labels (Tier 02–05).
- **12-Month Record Licensing:** Supply a valid, actively licensed Tier 01 ID for free refreshes during its 12-month license; ID-less resolution can still be billable.

---
*Maintained by **Finn** (<finn@infiniteaudience.ai>) • Infinite Audience*

---

### 📦 Downloadable Assets & Specifications
- `resolution_input_contract_v1.0.json`: JSON Schema for recommended input record shapes; the production API remains authoritative.
- `resolution_match_taxonomy_v1.0.json`: Machine-readable reference catalog of match levels, options, and match types; not a validation schema.
- `SPECIFICATION.md`: Complete standalone specification export.
