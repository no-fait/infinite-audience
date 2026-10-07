# Infinite Audience — Products Catalog

Official public developer documentation, schemas, manifests, data dictionaries, and release changelogs for **Infinite Audience** products.

---

## 📦 Available Products

| Product | Latest Release | Documentation | Description |
| :--- | :---: | :--- | :--- |
| **[Infinite Audience Graph](products/infinite-audience-graph/)** | [`v1.3.2.1`](https://github.com/no-fait/infinite-audience/releases/tag/iag-v1.3.2.1) | [Overview](products/infinite-audience-graph/README.md) • [Data Dictionary](products/infinite-audience-graph/DATA_DICTIONARY.md) • [Changelog](products/infinite-audience-graph/CHANGELOG.md) | Identity graph of US adult consumers featuring hundreds of attributes across many categories like Demographics & Household, Financial & Property, Media & Behavioral, Land Context, Brand Proximity, Neighborhood Lifestyle, etc. |
| **[Infinite Audience Identity Resolution & Enrichment](products/infinite-audience-identity-resolution/)** | [`v1.0`](https://github.com/no-fait/infinite-audience/releases/tag/id-v1.0) | [Overview](products/infinite-audience-identity-resolution/README.md) • [Specification](products/infinite-audience-identity-resolution/SPECIFICATION.md) • [Documentation](https://docs.infiniteaudience.ai/product/identity-resolution) | Deterministic, probabilistic, and spatial identity resolution matching engine connecting customer records to durable identities and actionable intelligence. |
| **[Infinite Audience Platform](products/infinite-audience-platform/)** | Production API | [API Reference](https://docs.infiniteaudience.ai/api/) • [How-to Guides](https://docs.infiniteaudience.ai/) • [OpenAPI YAML](products/infinite-audience-platform/openapi.yaml) • [OpenAPI JSON](products/infinite-audience-platform/openapi.json) | Resolve and enrich customer identities, build audiences, connect destinations, and automate Infinite Audience workflows. |

---

## 🗂 Repository Structure

This repository is organized as a multi-product catalog:

```
infinite-audience/
├── README.md                              # Master Product Catalog (this file)
└── products/
    ├── infinite-audience-graph/           # Core identity resolution & consumer graph
    │   ├── README.md                      # Graph scale, coverage, and quick reference
    │   ├── DATA_DICTIONARY.md             # Complete attribute dictionary & codebooks
    │   └── CHANGELOG.md                   # Single running chronological version history
    ├── infinite-audience-identity-resolution/ # Identity resolution & matching engine
    │   ├── README.md                      # Product overview & quick start
    │   ├── SPECIFICATION.md               # Complete baseline specification
    │   ├── resolution_input_contract_v1.0.json # Recommended input record schema
    │   ├── resolution_match_taxonomy_v1.0.json # Reference taxonomy of match types & levels
    │   └── releases/                      # Release notes per version (id-v1.0.md)
    ├── infinite-audience-platform/        # Customer-facing platform API contract
    │   ├── README.md                      # API overview and documentation links
    │   ├── openapi.yaml                   # Machine-readable production API (YAML)
    │   └── openapi.json                   # Machine-readable production API (JSON)
    └── ...                                # Additional Infinite Audience products
```

---

## 🔔 Subscribing to Product Releases

To receive notifications when new product versions, schemas, and releases are published:
1. Click **Watch** at the top of this repository → select **Custom** → check **Releases**.
2. Or subscribe to the public Atom feed in Slack, Microsoft Teams, or an RSS reader:
   ```
   https://github.com/no-fait/infinite-audience/releases.atom
   ```

---

*Maintained by **Finn** (<finn@infiniteaudience.ai>) • Infinite Audience*
