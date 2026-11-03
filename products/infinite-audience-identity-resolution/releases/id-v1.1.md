# Infinite Audience Identity Resolution & Enrichment v1.1

**Release Tag:** `id-v1.1`
**Release Date:** November 2026
**Specification:** v1.1 (independent of Graph and API versions; the production OpenAPI contract governs API requests and responses)

---

### 🎯 What's New in v1.1
**Infinite Audience Identity Resolution & Enrichment v1.1** improves precision when resolving shared household emails, family phone plans, and reassigned mobile numbers across both real-time and file workflows. No request schemas, response fields, `match_level` codes, or `match_type` identifiers (`15` supported match types) have changed.

- **Smarter Disambiguation on Shared Emails & Phones (`I`):** Adds middle-name concordance, generational age separation, and regional proximity tie-breaking when an email address or phone number is shared by multiple family members (such as spouses or parents and adult children).
- **Sharper Household (`H`) vs. Digital (`D`) Attribution:** Ensures records that share a family surname and email/phone with a household member consistently resolve as confirmed **Household (`H`)** matches (`graph_last_name_email_match`, `graph_last_name_phone_match`) rather than unconfirmed **Digital (`D`)** matches.
- **Recycled Phone & Shared Handle Safeguards (`D`):** Prevents false-positive digital-only matches when a customer submits a reassigned phone number or shared email alongside a different full name, allowing the record to safely fall through to physical address or spatial resolution.

---
*Maintained by **Finn** (<finn@infiniteaudience.ai>) • Infinite Audience*

---

### 📦 Downloadable Assets & Specifications
- `resolution_input_contract_v1.1.json`: JSON Schema for recommended input record shapes; the production API remains authoritative.
- `resolution_match_taxonomy_v1.1.json`: Machine-readable reference catalog of match levels, options, and match types; not a validation schema.
- `SPECIFICATION.md`: Complete standalone specification export.
