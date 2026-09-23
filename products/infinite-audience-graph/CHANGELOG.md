# Changelog — Infinite Audience Graph

All notable releases, schema evolutions, and coverage changes for the Infinite Audience Graph are documented here.

## [Infinite Audience Graph v1.2.2.0] - September 23, 2026

**Release Tag:** `iag-v1.2.2.0` | **Vintage:** September 2026

### 📊 Graph Scale
- **Resolved Individuals:** **215,677,380** verified consumer profiles

### 🆕 Added Attributes (21)
- `wildfire_risk_national_rank` (`FLOAT64` • *Environment & Risk*): Wildfire risk to homes percentile rank nationally.
- `wildfire_risk_state_rank` (`FLOAT64` • *Environment & Risk*): Wildfire risk to homes percentile rank within the state.
- `epa_pct_auto_ownership_0` (`FLOAT64` • *Transportation & Mobility*): Percentage of zero-car households.
- `epa_pct_auto_ownership_1` (`FLOAT64` • *Transportation & Mobility*): Percentage of one-car households.
- `epa_pct_auto_ownership_2p` (`FLOAT64` • *Transportation & Mobility*): Percentage of two-or-more car households.
- `epa_street_intersection_density` (`FLOAT64` • *Transportation & Mobility*): Density of multi-modal street intersections per square mile.
- `epa_transit_frequency` (`FLOAT64` • *Transportation & Mobility*): Aggregate peak transit service frequency per square mile.
- `epa_walkability_index` (`FLOAT64` • *Transportation & Mobility*): National Walkability Index score (1-20 scale) based on built environment characteristics.
- `county_subdivision_name` (`STRING` • *Geography*): Census Minor Civil Division (MCD) or Census County Division (CCD) legal/statistical name.
- `hud_fmr_1bed` (`FLOAT64` • *Economic Indicators*): HUD Fair Market Rent for a one-bedroom housing unit.
- `hud_fmr_2bed` (`FLOAT64` • *Economic Indicators*): HUD Fair Market Rent for a two-bedroom housing unit.
- `hud_fmr_3bed` (`FLOAT64` • *Economic Indicators*): HUD Fair Market Rent for a three-bedroom housing unit.
- `hud_fmr_4bed` (`FLOAT64` • *Economic Indicators*): HUD Fair Market Rent for a four-bedroom housing unit.
- `hud_fmr_studio` (`FLOAT64` • *Economic Indicators*): HUD Fair Market Rent for a studio or zero-bedroom housing unit.
- `is_gamer` (`BOOL` • *Media & Behavioral*): Video game enthusiast.
- `is_single_parent` (`BOOL` • *Demographics & Household*): Indicates whether the household is led by a single parent.
- `municipality_name` (`STRING` • *Geography*): Primary municipal government jurisdiction name (City, Borough, Township, or Town).
- `usda_convenience_stores_per_1k` (`FLOAT64` • *Census Demographics & Socioeconomic*): Number of convenience stores per 1,000 residents.
- `usda_grocery_stores_per_1k` (`FLOAT64` • *Census Demographics & Socioeconomic*): Number of grocery stores per 1,000 residents.
- `usda_recreation_facilities_per_1k` (`FLOAT64` • *Census Demographics & Socioeconomic*): Number of recreation and fitness facilities per 1,000 residents.
- `usda_snap_percentage` (`FLOAT64` • *Census Demographics & Socioeconomic*): Percentage of households participating in the Supplemental Nutrition Assistance Program (SNAP).

### 🔄 Modified Attributes (5)
- `emails` (*Identity*): type: `ARRAY<STRUCT<priority INT64, match_level STRING, email STRING>>` -> `ARRAY<STRUCT<priority INT64, match_level STRING, confidence_score FLOAT64, email STRING, email_domain_type STRING>>`, updated description
- `phones` (*Identity*): type: `ARRAY<STRUCT<priority INT64, match_level STRING, phone_type STRING, phone STRING>>` -> `ARRAY<STRUCT<priority INT64, match_level STRING, confidence_score FLOAT64, phone STRING, phone_type STRING>>`, updated description
- `household_size` (*Demographics & Household*): type: `NUMERIC` -> `INT64`, updated description
- `has_children` (*Demographics & Household*): type: `STRING` -> `BOOL`, updated description
- `home_has_pool` (*Financial & Property*): type: `STRING` -> `BOOL`, updated description

## 🚀 What's New in v1.2.2.0

### 1. Municipal Geography & Minor Civil Divisions (MCDs)
- **Township & Municipal Resolution**: Added `county_subdivision_name` to core geography, enabling sub-county targeting across 35,629 Minor Civil Divisions (MCDs), towns, and incorporated municipalities from US Census TIGER 2026.
- **Sub-County Granularity**: Marketers can now target local government jurisdictions, New England towns, and Midwestern townships with legal administrative boundaries.

### 2. Behavioral & Lifestyle Profiles
- **Gamer Profile**: Added the `is_gamer` boolean attribute within the Media & Behavioral category, identifying active video game and interactive media enthusiasts.

### 3. Contact Point Intelligence & Ranked Priority
- **Harmonized Contact STRUCTs**: Standardized `phones` and `emails` contact point arrays to symmetrical STRUCT schemas (`priority`, `match_level`, `confidence_score`, `value`, `domain_type`/`phone_type`).
- **Email Domain Classification**: Enriched emails with `email_domain_type` classification (`government`, `education`, `military`, `corporate`, `personal`) via deterministic rule engine.
- **Dynamic Priority & Confidence Ranking**: Applied confidence scoring and dynamic priority ordering so primary reachability points appear first in candidate arrays.

### 4. Environmental, Housing & Walkability Insights
- **EPA Smart Location & Mobility**: Integrated the EPA Smart Location Database into neighborhood metrics, featuring `epa_walkability_index`, `epa_transit_frequency`, `epa_street_intersection_density`, and auto-ownership distributions.
- **USDA Food Environment & Community**: Added grocery store density, convenience store density, recreation facility density, and SNAP participation rates.
- **HUD Fair Market Rents**: Integrated Section 8 50th percentile Fair Market Rents across Studio, 1-Bed, 2-Bed, 3-Bed, and 4-Bed units for local rental affordability modeling.
- **Wildfire Risk**: Enriched with national and state wildfire hazard risk percentiles (`wildfire_risk_national_rank`, `wildfire_risk_state_rank`).

---

## 🛠️ Graph & Platform Improvements

- **Unit-Gated Household Clustering**: Remediated commercial drop-point overclustering by gating household grouping on secondary unit numbers (`unit_norm`) and capping household clusters at 8 members.
- **Child Attribute Harmonization**: Harmonized child count, age bracket ranges, and presence flags across consumer profiles, converting boolean vendor fields to native SQL booleans.

---

## 🛡️ Data Quality & Outlier Sanitization

- **Census Rate Denominators**: Corrected ACS labor-force participation and vehicle ownership rate denominators to prevent sentinel division-by-zero or values $>1.0$.
- **FEMA NRI & DOE LEAD Outliers**: Sanitized FEMA National Risk Index sentinels (`-9999`) and DOE LEAD energy-burden ratio outliers.

---
*Maintained by **Finn** (<finn@infiniteaudience.ai>) • Infinite Audience*
## [Infinite Audience Graph v1.0.1.0] - August 31, 2026

**Release Tag:** `iag-v1.0.1.0` | **Vintage:** August 2026

### 🚀 Product Release Baseline
- **Active Schema**: 525 customer-facing attributes across 12 core categories.
- **National Linkage Graph**: Complete nation-wide US consumer graph connecting individual, household, and property insights.

---
*Maintained by **Finn** (<finn@infiniteaudience.ai>) • Infinite Audience*
