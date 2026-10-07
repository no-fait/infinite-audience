# Infinite Audience Identity Resolution & Enrichment

[![Specification](https://img.shields.io/badge/Specification-v1.0-blue.svg)](SPECIFICATION.md)
[![Match Levels](https://img.shields.io/badge/Match_Levels-5_Levels-green.svg)](#-match-levels)
[![Match Types](https://img.shields.io/badge/Match_Types-15_Types-purple.svg)](#-match-types-taxonomy)

Official public specification, input contracts, match type taxonomy, and release notes for **Infinite Audience Identity Resolution & Enrichment** — the deterministic, probabilistic, and spatial matching engine that connects customer records to durable identities and actionable intelligence across the Infinite Audience ecosystem.

---

## 🎯 Engine Capabilities

- **Deterministic Verification:** Fast graph lookups supporting standard nicknames, highway/route variations, and generational suffixes.
- **Probabilistic Weighted Agreement:** Evaluates multi-attribute agreement across noisy contact signals with strict veto guardrails against conflicting house numbers or generational namesake mix-ups.
- **Spatial Proximity Engine:** Locates individuals who moved locally or submitted a workplace address using coordinate proximity and neighborhood urbanicity, dynamically calibrated by surname frequency.
- **Privacy-Safe Ingestion:** Supports raw contact signals alongside 64-character SHA-256 pre-hashed emails and phone numbers.
- **Multi-Value Arrays:** Ingest multiple emails, phone numbers, and historical addresses on a single input row.

---

## 🏷 Match Levels

| Level | What it Confirms | Typical Uses |
| :--- | :--- | :--- |
| **I** · Individual | The specific person, confirmed by name plus address, email, phone, or date of birth. | Personalized outreach, direct mail, CRM cleanup and deduplication. |
| **H** · Household | The home and family, confirmed by last name plus address. | Household offers, direct mail, home services. |
| **D** · Digital | A known email or phone, without a confirmed name. | Digital advertising audiences, newsletter and web enrichment. |
| **S** · Spatial | The person, placed by the spatial engine near the submitted address. | Workplace leads, recent local movers, apartment communities. |
| **A** · Address | The physical address only. | Property and neighborhood insights, territory planning. |

---

## 📚 Documentation & Reference

- **[Specification](SPECIFICATION.md)**: Full baseline specification covering input fields, normalization rules, matching cascade, and record licensing.
- **[Interactive Documentation](https://docs.infiniteaudience.ai/product/identity-resolution)**: Live documentation, interactive examples, and platform guides.
- **[Latest Release Notes](releases/id-v1.0.md)**: Official release notes for version `id-v1.0`.

---

## 📦 Downloadable Assets & Schemas

Every release publishes machine-readable assets attached to GitHub Releases:
- `resolution_input_contract_v1.0.json`: Recommended input record JSON schema (production OpenAPI remains authoritative).
- `resolution_match_taxonomy_v1.0.json`: Machine-readable catalog of match options, levels, and all 15 supported match types.
- `SPECIFICATION.md`: Standalone markdown export of the complete identity resolution specification.

---

## 🔔 Subscribing to Release Updates

To receive notifications when new identity resolution specifications and updates are published:
1. Click **Watch** at the top of the repository → select **Custom** → check **Releases**.
2. Or subscribe to the RSS / Atom feed in Slack or an RSS reader:
   ```
   https://github.com/no-fait/infinite-audience/releases.atom
   ```

---

*Maintained by **Finn** (<finn@infiniteaudience.ai>) • Infinite Audience*
