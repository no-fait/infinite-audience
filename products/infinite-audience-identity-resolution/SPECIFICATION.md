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

### Accepted Single-Value Fields

| Field | Type | Description & Normalization |
| :--- | :--- | :--- |
| `row_id` | `STRING` | Caller-supplied unique record ID. Returned unchanged for joining results back. |
| `first_name` | `STRING` | First name. Nicknames are recognized automatically (e.g., *Bill* matches *William*, *Barb* matches *Barbara*). |
| `middle_name` | `STRING` | Middle name or initial. Used to distinguish otherwise identical people without penalizing matches when omitted. |
| `last_name` | `STRING` | Last name. Hyphenated and multi-part surnames are supported. |
| `name_suffix` | `STRING` | Generational suffix such as `Jr`, `Sr`, or `III`. Separates parent/child namesakes at the same address. |
| `full_name` | `STRING` | Single full name field. Automatically parsed into first, middle, last, and suffix if discrete fields are not sent. |
| `address_1` | `STRING` | Street address (e.g., `123 Main St`). May include secondary units (e.g., `123 Main St Apt 4B`). |
| `address_2` | `STRING` | Apartment, unit, or suite (e.g., `Apt 4B`, `Suite 200`). |
| `city` | `STRING` | City or municipality name. |
| `state` | `STRING` | Two-letter state code (e.g., `CA`, `NY`). |
| `zip` | `STRING` | 5-digit US zip code. |
| `email` | `STRING` | Raw email address. Whitespace and casing are normalized automatically. |
| `phone` | `STRING` | US phone number. Punctuation and leading `1` are removed automatically. |
| `dob` | `STRING` | Date of birth as `YYYY-MM-DD`, `MM/DD/YYYY`, `MM-DD-YYYY`, or birth year `YYYY`. |
| `email_sha256`| `STRING` | Pre-hashed email sent as a 64-character lowercase hexadecimal SHA-256 string. |
| `phone_sha256`| `STRING` | Pre-hashed phone sent as a 64-character lowercase hexadecimal SHA-256 string. |
| `iag_person_id`| `STRING`| Previously issued Tier 01 Person ID for instant recognition and refresh without rematching. |

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

| Option | Type | Default | Permitted Values | Description |
| :--- | :--- | :---: | :--- | :--- |
| `spatial_mode` | `STRING` | `'residential'` | `'residential'`, `'work'`, `'auto'` | Sets the spatial search strategy based on address context. |
| `match_level` | `ARRAY<STRING>`| `['I','H','D','S','A']` | `'I'`, `'H'`, `'D'`, `'S'`, `'A'` | Filter allowed match levels. Records that do not meet an allowed level return unmatched. |

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

| Match Level | `match_type` | What Confirmed the Match |
| :--- | :--- | :--- |
| Prior level or empty | `graph_iag_person_id_match` | Recognized ID; preserves prior match provenance |
| **I** | `graph_name_address_match` | First name + last name + street address + zip code |
| **I** | `graph_fuzzy_street_match` | Name + street with highway/route alias or minor spelling variation |
| **I** or **H** | `graph_name_email_match` | First name + last name + email (raw or pre-hashed) |
| **I** or **H** | `graph_name_phone_match` | First name + last name + phone (raw or pre-hashed) |
| **I** | `graph_name_zip_dob_match` | First name + last name + zip code + date of birth (no street needed) |
| **I** | `graph_first_dob_address_match` | First name + date of birth + address (resolves across surname changes) |
| **D** | `graph_email_match` | Known email alone |
| **D** | `graph_phone_match` | Known phone number alone |
| **H** | `graph_last_name_address_match` | Last name + address (household co-resident or family offer) |
| **H** | `graph_last_name_email_match` | Last name + email |
| **H** | `graph_last_name_phone_match` | Last name + phone |
| **A** | `graph_address_match` | Street address + zip code alone (property and location profile) |
| **I** | `probabilistic_name_address_match` | Weighted agreement across name, address, unit, or neighboring zip |
| **S** | `spatial_match` | Name + physical coordinate proximity within neighborhood or commuter shed |

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
