# Infinite Audience Identity Resolution & Enrichment — Specification (v1.0)

**Product Specification:** v1.0 Baseline (independent of Graph and API versions; the [production OpenAPI contract](https://github.com/no-fait/infinite-audience/tree/main/products/infinite-audience-platform) governs API requests and responses)  
**Release Tag:** `id-v1.0`  
**Product Directory:** `products/infinite-audience-identity-resolution/`  

---

## 1. Overview & Architecture

Identity resolution connects customer records to durable graph identities. Enrichment adds actionable intelligence attributes to resolved profiles.

The engine processes records through three successive approaches:
1. **Deterministic Matching:** Exact verified connections in the identity graph.
2. **Probabilistic Matching:** Multi-attribute weighted agreement evaluating typos, unit formats, phonetic variations, and neighboring zip codes, guarded by hard veto rules.
3. **Spatial Matching:** Geodesic coordinate proximity and neighborhood density (urbanicity) with dynamic search radius scaling based on name frequency and commuter patterns.

---

## 2. Input Contract

### Accepted Input Fields

<!-- identity-contract:inputs:start -->
| Field | What to send |
| :--- | :--- |
| `row_id` | Your own record ID. It is returned unchanged so you can join results back. |
| `email` | Email address. Capitalization and extra spaces are cleaned up automatically. |
| `phone` | US phone number. Punctuation and a leading `1` are removed automatically. |
| `email_sha256` | A pre-hashed email (see below). |
| `phone_sha256` | A pre-hashed phone (see below). |
| `full_name` | A single name field. If you don't send separate name fields, it is split into first, middle, last, and suffix for you. |
| `first_name` | First name. Nicknames are fine: *Bill* can match *William*. |
| `middle_name` | Middle name or initial. Optional. Used to distinguish otherwise identical people. |
| `last_name` | Last name. Hyphenated and two-part last names are supported. |
| `name_suffix` | Generational suffix such as `Jr`, `Sr`, or `III`. |
| `emails` | Lists of additional values (see below). |
| `emails_sha256` | Lists of additional pre-hashed values. |
| `phones` | Lists of additional values (see below). |
| `phones_sha256` | Lists of additional pre-hashed values. |
| `addresses` | Lists of additional values (see below). |
| `address_1` | Street address, such as `123 Main St`. If your source has a single address line that includes the unit (e.g. `123 Main St Apt 4B`), it can go here. |
| `address_2` | Apartment, unit, or suite, such as `Apt 4B`. |
| `city` | City. |
| `state` | Two-letter state code, such as `CA`. |
| `zip` | 5-digit ZIP code. |
| `dob` | Date of birth as `YYYY-MM-DD`, `MM/DD/YYYY`, `MM-DD-YYYY`, or a birth year `YYYY`. |
| `iag_person_id` | An Infinite Audience Graph Person ID issued to your organization by an earlier match or audience delivery. |
<!-- identity-contract:inputs:end -->

### Multi-Value Inputs

Send all of a customer's known contact points on a single record. Every value is evaluated as its own match point:
- `emails` (`ARRAY<STRING>`): List of additional email addresses.
- `phones` (`ARRAY<STRING>`): List of additional phone numbers.
- `emails_sha256` (`ARRAY<STRING>`): List of additional pre-hashed emails.
- `phones_sha256` (`ARRAY<STRING>`): List of additional pre-hashed phones.
- `addresses` (`ARRAY<OBJECT>`): List of additional addresses (`address_1`, `address_2`, `city`, `state`, `zip`).

### What is Enough to Match

| Signal Combination | Best Possible Match Level |
| :--- | :---: |
| Infinite Audience Graph Person ID previously received | Direct Refresh (Tier 01 ID, no rematching) |
| First Name + Last Name + Street Address + zip | **I** · Individual |
| First Name + Last Name + Email or Phone | **I** · Individual |
| First Name + Last Name + zip + Date of Birth (No street needed) | **I** · Individual |
| First Name + Date of Birth + Street Address + zip (Works across surname changes) | **I** · Individual |
| First Name + Last Name + Physical Proximity Address | **S** · Spatial |
| Email or Phone Alone | **D** · Digital |
| Last Name + Street Address + zip | **H** · Household |
| Street Address + zip Alone | **A** · Address |

---

## 3. Match Options & Quality Safeguards

<!-- identity-contract:options:start -->
| Option | Type | Default | Permitted values |
| :--- | :--- | :--- | :--- |
| `match_level` | array | `["I", "H", "D", "S", "A"]` | `I`, `H`, `D`, `S`, `A` |
| `spatial_mode` | string | `"residential"` | `residential`, `work`, `auto` |
<!-- identity-contract:options:end -->

### Built-In Quality & Confidence Safeguards
- **Diagnostic Confidence Score:** Every returned match reports a `match_confidence` score between `0.00` and `1.00`.
- **Quality Safeguards:** Matching uses phase-specific acceptance rules; spatial matching requires at least `0.80` confidence. Scores are diagnostics, not measured accuracy probabilities.

---

## 4. Match Levels

| Level | What it Confirms | Typical Uses |
| :--- | :--- | :--- |
| **I** · Individual | The specific person, confirmed by name plus address, email, phone, or date of birth. | Personalized outreach, direct mail, CRM cleanup and deduplication. |
| **H** · Household | The home and family, confirmed by last name plus address. | Household offers, direct mail, home services. |
| **D** · Digital | A known email or phone, without a confirmed name. | Digital advertising audiences, newsletter and web enrichment. |
| **S** · Spatial | The person, placed by the spatial engine near the submitted address. | Workplace leads, recent local movers, apartment communities. |
| **A** · Address | The physical address only. | Property and neighborhood insights, territory planning. |

---

## 5. Canonical Match Types Taxonomy

<!-- identity-contract:matches:start -->
| Level | `match_type` | What made the match |
| :--- | :--- | :--- |
| A | `graph_address_match` | Street address + zip code alone (property and location profile) |
| D | `graph_email_match` | Known email alone |
| I | `graph_first_dob_address_match` | First name + date of birth + address (resolves across surname changes) |
| I | `graph_fuzzy_street_match` | Name + street with highway/route alias or minor spelling variation |
| Prior level or empty | `graph_iag_person_id_match` | Recognized ID; preserves prior match provenance |
| H | `graph_last_name_address_match` | Last name + address (household co-resident or family offer) |
| H | `graph_last_name_email_match` | Last name + email |
| H | `graph_last_name_phone_match` | Last name + phone |
| I | `graph_name_address_match` | First name + last name + street address + zip code |
| H / I | `graph_name_email_match` | First name + last name + email (raw or pre-hashed) |
| H / I | `graph_name_phone_match` | First name + last name + phone (raw or pre-hashed) |
| I | `graph_name_zip_dob_match` | First name + last name + zip code + date of birth (no street needed) |
| D | `graph_phone_match` | Known phone number alone |
| I | `probabilistic_name_address_match` | Weighted agreement across name, address, unit, or neighboring zip |
| S | `spatial_match` | Name + physical coordinate proximity within neighborhood or commuter shed |
<!-- identity-contract:matches:end -->

---

## 6. Privacy, Salting & Record Licensing

1. **Organization-Scoped Salting:**
   - Every resolved person receives an `iag_person_id` cryptographically salted to your organization. The same resolved person receives a consistent ID within your organization, but a different ID in another company's workspace.
2. **Real IDs vs. Derived IDs:**
   - **Tier 01 (Resolved Person ID):** Points to a resolved graph identity. Reusable for free refreshes while its 12-month license is active and the ID is supplied.
   - **Tier 02–05 (Derived Continuity ID):** Created from submitted signals on unmatched rows to preserve row continuity in customer files without claiming a graph match.
3. **12-Month Record Licensing:**
   - A new or renewed identity license starts at successful external delivery, including a real-time API response, and lasts 12 months.
   - With a valid, actively licensed Tier 01 ID supplied, refreshes during that period have no identity charge; ID-less resolution can still be billable (`resolution_action: "current"` or `"refreshed"`, `license_action: "none"`).
