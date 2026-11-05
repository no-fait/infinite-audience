# Changelog — Infinite Audience Identity Resolution & Enrichment

All notable releases, matching engine enhancements, and specification updates for Infinite Audience Identity Resolution & Enrichment are documented here.

## [Infinite Audience Identity Resolution & Enrichment v1.1] - November 3, 2026

**Release Tag:** `id-v1.1` | **Specification:** v1.1

### 🎯 What's New in v1.1
**Infinite Audience Identity Resolution & Enrichment v1.1** improves precision when resolving shared household emails, family phone plans, and reassigned mobile numbers across both real-time and file workflows. No request schemas, response fields, `match_level` codes, or `match_type` identifiers (`15` supported match types) have changed.

- **Smarter Disambiguation on Shared Emails & Phones (`I`):** Adds middle-name concordance, generational age separation, and regional proximity tie-breaking when an email address or phone number is shared by multiple family members (such as spouses or parents and adult children).
- **Sharper Household (`H`) vs. Digital (`D`) Attribution:** Ensures records that share a family surname and email/phone with a household member consistently resolve as confirmed **Household (`H`)** matches (`graph_last_name_email_match`, `graph_last_name_phone_match`) rather than unconfirmed **Digital (`D`)** matches.
- **Recycled Phone & Shared Handle Safeguards (`D`):** Prevents false-positive digital-only matches when a customer submits a reassigned phone number or shared email alongside a different full name, allowing the record to safely fall through to physical address or spatial resolution.

### 📦 Release Assets
- `resolution_input_contract_v1.1.json`: JSON Schema for recommended input record shapes; the production API remains authoritative.
- `resolution_match_taxonomy_v1.1.json`: Machine-readable reference catalog of match levels, options, and match types; not a validation schema.
- `SPECIFICATION.md`: Complete standalone specification export.

---
*Maintained by **Finn** (<finn@infiniteaudience.ai>) • Infinite Audience*

## [Infinite Audience Identity Resolution & Enrichment v1.0] - October 7, 2026

**Release Tag:** `id-v1.0` | **Specification:** v1.0 Baseline

### 🎯 Product Release Baseline
Established the official v1.0 baseline specification for **Infinite Audience Identity Resolution & Enrichment** — defining accepted input signals, configurable match options, the three-approach matching cascade (Deterministic, Probabilistic, Spatial), 5 confirmed match levels (`I`, `H`, `D`, `S`, `A`), and 15 supported match types.

- **Universal Multi-Value Input Contract:** Supports multi-touch arrays (`emails`, `phones`, `addresses`), 64-character SHA-256 pre-hashed signals (`email_sha256`, `phone_sha256`), and automatic name/address normalization.
- **Configurable Matching Options:** Supports `residential`, `work`, and `auto` spatial modes alongside `match_level` filtering.
- **Privacy & Customer Continuity:** Organization-scoped salted `iag_person_id` identifiers, Tier 01 vs. Tier 02–05 continuity tiers, and 12-month record licensing.

### 📦 Release Assets
- `resolution_input_contract_v1.0.json`: JSON Schema for recommended input record shapes.
- `resolution_match_taxonomy_v1.0.json`: Machine-readable reference catalog of match levels, options, and match types.
- `SPECIFICATION.md`: Complete standalone specification export.

---
*Maintained by **Finn** (<finn@infiniteaudience.ai>) • Infinite Audience*
