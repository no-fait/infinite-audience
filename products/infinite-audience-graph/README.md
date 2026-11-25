# Infinite Audience Graph (IAG)

[![Latest Release](https://img.shields.io/badge/Release-v1.5.4.0-blue.svg)](https://github.com/no-fait/infinite-audience/releases/tag/iag-v1.5.4.0)
[![Attributes](https://img.shields.io/badge/Attributes-549_Columns-green.svg)](DATA_DICTIONARY.md)
[![Coverage](https://img.shields.io/badge/Resolved_Individuals-243,393,313-purple.svg)](#graph-scale--coverage)

Official public schema documentation, data dictionaries, and release changelogs for the **Infinite Audience Graph (IAG)** — an identity resolution and consumer intelligence graph linking individual, household, and property-level insights across the United States.

---

## 📊 Graph Scale & Coverage (`v1.5.4.0`)

| Entity Dimension | Total Verified Count | Description |
| :--- | :---: | :--- |
| **Resolved Individuals** | **243,393,313** | Persistent person nodes resolved across multi-vendor identity signals |
| **Household Clusters** | **148,091,666** | Resolved co-residency units sharing verified residential addresses |
| **Physical Delivery Addresses** | **115,775,605** | Standardized USPS delivery points and CASS-validated locations |
| **Building Footprints** | **96,877,702** | Unique physical parcels and building structures |
| **Graph Linkage Identifiers** | **1,178,851,444** | Identity traversal nodes (emails, phone numbers, addresses) |

---

## 📚 Documentation & Reference

- **[Data Dictionary](DATA_DICTIONARY.md)**: Full attribute definitions, data types, PII classification, and value codebooks for all 549 attributes.
- **[Changelog](CHANGELOG.md)**: Historical release notes, schema evolutions, and graph coverage changes.
- **[Latest GitHub Release](https://github.com/no-fait/infinite-audience/releases/tag/iag-v1.5.4.0)**: Download machine-readable JSON & CSV schema packages.

---

## 📦 Release Packages & Assets

Every release includes downloadable artifacts attached to GitHub Releases:
- `iag_data_dictionary_v1.5.4.0.json`: Machine-readable attribute metadata and category structures.
- `iag_data_dictionary_v1.5.4.0.csv`: Tabular spreadsheet of all data dictionary attributes.
- `iag_statistics_v1.5.4.0.json`: Exact entity and node topology counts for the release.

---

## 🔔 Subscribing to Release Updates

To receive notifications when new IAG versions and data vintages are published:
1. Click **Watch** at the top of the repository → select **Custom** → check **Releases**.
2. Or subscribe to the RSS / Atom feed in Slack or an RSS reader:
   ```
   https://github.com/no-fait/infinite-audience/releases.atom
   ```
