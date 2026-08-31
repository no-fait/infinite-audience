# Infinite Audience Graph — Data Dictionary

**Version:** `v1.0.1.0` | **Generated:** August 30, 2026 | **Total Attributes:** 525

This data dictionary provides comprehensive field definitions, data types, entity levels, PII classifications, and value mappings for the Infinite Audience Graph (IAG).

---

## Table of Contents

- [Identity](#identity) (17 attributes)
- [Demographics & Household](#demographics--household) (9 attributes)
- [Financial & Property](#financial--property) (10 attributes)
- [Media & Behavioral](#media--behavioral) (11 attributes)
- [Geography](#geography) (14 attributes)
- [Land Context](#land-context) (21 attributes)
- [Census Demographics & Socioeconomic](#census-demographics--socioeconomic) (244 attributes)
- [Health](#health) (40 attributes)
- [Environment & Risk](#environment--risk) (8 attributes)
- [Economic Indicators](#economic-indicators) (12 attributes)
- [Brand Proximity](#brand-proximity) (99 attributes)
- [Neighborhood Lifestyle](#neighborhood-lifestyle) (40 attributes)

---

## Identity
*Resolved person and household identifiers, contact information, and physical address derived from cross-source entity resolution*

| Column Name | Type | Level | PII | Description | Value Mappings / Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `iag_schema_major_release_version` | `INT64` | Meta | No | IAG schema major version tracking breaking structural changes. | - |
| `iag_schema_minor_release_version` | `INT64` | Meta | No | IAG schema minor version tracking backwards-compatible field additions. | - |
| `iag_refresh_major_release_version` | `INT64` | Meta | No | IAG refresh major cycle version tracking full warehouse rebuilds. | - |
| `iag_refresh_minor_release_version` | `INT64` | Meta | No | IAG refresh minor cycle version tracking incremental delta updates. | - |
| `iag_person_id` | `STRING` | Individual | No | Unique universal person identifier resolved from all source systems via entity resolution | - |
| `iag_household_id` | `STRING` | Household | No | Household identifier grouping individuals at the same resolved address | - |
| `first_name` | `STRING` | Individual | 🔒 Yes | First name | - |
| `middle_name` | `STRING` | Individual | 🔒 Yes | Middle name | - |
| `last_name` | `STRING` | Individual | 🔒 Yes | Last name | - |
| `name_suffix` | `STRING` | Individual | 🔒 Yes | Name suffix (Jr, Sr, III, etc.) | - |
| `address_1` | `STRING` | Household | 🔒 Yes | Primary address line | - |
| `address_2` | `STRING` | Household | 🔒 Yes | Secondary address line (apartment, suite, unit) | - |
| `city` | `STRING` | Household | No | City | - |
| `state` | `STRING` | Household | No | State | - |
| `zip5` | `STRING` | Household | No | 5-digit ZIP code | - |
| `emails` | `ARRAY<RECORD>` | Individual | 🔒 Yes | Resolved email addresses associated with the person, including confidence score, priority, and match level | - |
| `phones` | `ARRAY<RECORD>` | Individual | 🔒 Yes | Resolved telephone numbers associated with the person, including line type, carrier, and match level | - |

---

## Demographics & Household
*Individual and household-level demographic attributes describing life stage, family composition, and generational cohort*

| Column Name | Type | Level | PII | Description | Value Mappings / Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `gender` | `STRING` | Individual | No | Gender (Male/Female) | `Male`: Male<br>`Female`: Female |
| `dob` | `DATE` | Individual | 🔒 Yes | Date of birth (YYYY-MM-DD) | - |
| `age` | `INTEGER` | Individual | No | Age in years | - |
| `birth_generation` | `STRING` | Individual | No | Generation mapped from birth year (e.g., Millennials, Baby Boomers, Generation X) | `Greatest Generation`: Greatest Generation<br>`Silent Generation`: Silent Generation<br>`Baby Boomers`: Baby Boomers<br>`Generation X`: Generation X<br>`Millennials`: Millennials<br>`Generation Z`: Generation Z |
| `marital_status` | `STRING` | Individual | No | Documented marital status (e.g., Married, Single) | `Married`: Married<br>`Single`: Single |
| `household_size` | `NUMERIC` | Household | No | Number of people in household | - |
| `has_children` | `STRING` | Household | No | Household has children present | - |
| `children_age_ranges` | `ARRAY<STRING>` | Household | No | Child age ranges present in the household (e.g., Under 6, 6-10, 11-15, 16-17) | `Under 6`: Under 6<br>`6-10`: 6–10<br>`11-15`: 11–15<br>`16-17`: 16–17 |
| `number_of_children` | `STRING` | Household | No | Number of children in household (No Children, 1 - 2, 3 - 5, 6+) | `No Children`: No Children<br>`1 - 2`: 1 – 2<br>`3 - 5`: 3 – 5<br>`6+`: 6+ |

---

## Financial & Property
*Estimated financial capacity, property ownership characteristics, and professional profile indicators*

| Column Name | Type | Level | PII | Description | Value Mappings / Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `education_level` | `STRING` | Individual | No | Highest education level attained (e.g., High School, College, Graduate School) | `Some High School`: Some High School<br>`High School`: High School<br>`Some College`: Some College<br>`Vocational`: Vocational<br>`College`: College<br>`Graduate School`: Graduate School |
| `estimated_household_income` | `STRING` | Household | No | Estimated household income bracket (e.g., $50,000 - $59,999, $500,000+) | `Under $20,000`: Under $20,000<br>`$20,000 - $29,999`: $20,000 – $29,999<br>`$30,000 - $39,999`: $30,000 – $39,999<br>`$40,000 - $49,999`: $40,000 – $49,999<br>`$50,000 - $59,999`: $50,000 – $59,999<br>`$60,000 - $74,999`: $60,000 – $74,999<br>`$75,000 - $99,999`: $75,000 – $99,999<br>`$100,000 - $124,999`: $100,000 – $124,999<br>... (+5 more) |
| `net_worth` | `STRING` | Household | No | Composite net worth bracket (e.g., $0 or Less, $100,000 - $149,999, $1,000,000+) | `$0 or Less`: $0 or Less<br>`$1 - $24,999`: $1 – $24,999<br>`$25,000 - $49,999`: $25,000 – $49,999<br>`$50,000 - $74,999`: $50,000 – $74,999<br>`$75,000 - $99,999`: $75,000 – $99,999<br>`$100,000 - $149,999`: $100,000 – $149,999<br>`$150,000 - $249,999`: $150,000 – $249,999<br>`$250,000 - $374,999`: $250,000 – $374,999<br>... (+4 more) |
| `occupation` | `STRING` | Individual | No | Labeled occupation and industry division (e.g., Medical, Finance, Blue Collar) | `Administrative / Managerial`: Administrative / Managerial<br>`Agriculture / Environment`: Agriculture / Environment<br>`Blue Collar`: Blue Collar<br>`Clerical`: Clerical<br>`Education`: Education<br>`Finance`: Finance<br>`Government / Military`: Government / Military<br>`Homemaker`: Homemaker<br>... (+9 more) |
| `homeowner_status` | `STRING` | Household | No | Homeowner/renter status | `Homeowner`: Homeowner<br>`Renter`: Renter |
| `length_of_residence` | `NUMERIC` | Household | No | Estimated number of years at the current address, expressed as an integer from 0 to 15. A value of 0 indicates less than one year; 15 indicates 15 or more years | `0`: Less than 1 Year<br>`1`: 1 Year<br>`2`: 2 Years<br>`3`: 3 Years<br>`4`: 4 Years<br>`5`: 5 Years<br>`6`: 6 Years<br>`7`: 7 Years<br>... (+8 more) |
| `dwelling_type` | `STRING` | Household | No | Dwelling type category (e.g., Single Family, Multi-Family) | `Single Family`: Single Family<br>`Multi-Family`: Multi-Family |
| `market_home_value` | `STRING` | Household | No | Estimated market value of home bracket (e.g., $100,000 - $124,999, $1,000,000+) | `$1,000 - $24,999`: $1,000 – $24,999<br>`$25,000 - $49,999`: $25,000 – $49,999<br>`$50,000 - $74,999`: $50,000 – $74,999<br>`$75,000 - $99,999`: $75,000 – $99,999<br>`$100,000 - $124,999`: $100,000 – $124,999<br>`$125,000 - $149,999`: $125,000 – $149,999<br>`$150,000 - $174,999`: $150,000 – $174,999<br>`$175,000 - $199,999`: $175,000 – $199,999<br>... (+11 more) |
| `home_year_built` | `STRING` | Household | No | Year the home was built (e.g. 1995) | - |
| `home_has_pool` | `STRING` | Household | No | Home has a swimming pool | - |

---

## Media & Behavioral
*Modeled digital behavior, media consumption preferences, and lifestyle engagement signals*

| Column Name | Type | Level | PII | Description | Value Mappings / Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `active_social_networks` | `ARRAY<STRING>` | Individual | No | Active social media networks (used in last 30 days) | `facebook`: Facebook<br>`instagram`: Instagram<br>`linkedin`: LinkedIn<br>`pinterest`: Pinterest<br>`x`: X (Twitter)<br>`youtube`: YouTube |
| `streaming_subscriptions` | `ARRAY<STRING>` | Individual | No | Active streaming media subscriptions | `amazon_prime`: Amazon Prime Video<br>`hulu`: Hulu<br>`netflix`: Netflix<br>`hbo_max`: HBO Max |
| `media_channels` | `ARRAY<STRING>` | Individual | No | Preferred media channels | `magazines`: Magazines<br>`newspapers`: Newspapers<br>`radio`: Radio<br>`public_radio`: Public Radio<br>`television`: Television<br>`internet`: Internet<br>`video_streaming`: Video Streaming |
| `primary_mobile_os` | `STRING` | Individual | No | Primary mobile device operating system (iOS, Android) | `iOS`: iOS<br>`Android`: Android |
| `political_affiliation` | `STRING` | Individual | No | Primary party affiliation (Democrat, Republican, Independent) | `Democrat`: Democrat<br>`Republican`: Republican<br>`Independent`: Independent |
| `political_outlook_score` | `INTEGER` | Individual | No | Political outlook score (1=Very Conservative, 2=Somewhat Conservative, 3=Moderate, 4=Somewhat Liberal, 5=Very Liberal) | `1`: 1 – Very Conservative<br>`2`: 2 – Somewhat Conservative<br>`3`: 3 – Moderate<br>`4`: 4 – Somewhat Liberal<br>`5`: 5 – Very Liberal |
| `shopper_segment` | `STRING` | Individual | No | Shopper segment persona category (e.g. Trendsetter, Bargain Hunter) | `Quality Seeker`: Quality Seeker<br>`Deal Seeker`: Deal Seeker<br>`Straightforward`: Straightforward<br>`Traditional`: Traditional<br>`Offline`: Offline |
| `tech_attitude_score` | `INTEGER` | Individual | No | Technology adoption attitude score (1-5 = low to high) | `1`: 1 – Very Low Tech<br>`2`: 2 – Low Tech<br>`3`: 3 – Moderate<br>`4`: 4 – High Tech<br>`5`: 5 – Very High Tech |
| `interests` | `ARRAY<STRING>` | Individual | No | True hobbies and specific topic interests (e.g., photography, crafts_and_sewing, cooking_and_gourmet) | `accessories`: Accessories<br>`american_history`: American History<br>`apparel`: Apparel<br>`audio`: Audio<br>`automotive`: Automotive<br>`aviation`: Aviation<br>`bargain_shopping`: Bargain Shopping<br>`baseball`: Baseball<br>... (+83 more) |
| `behavioral_propensities` | `ARRAY<STRING>` | Individual | No | Modeled indicators predicting major financial or commercial transactional life-events (e.g., job_seeking, upscale_shopping, credit_report) | `auto_insurance`: Auto Insurance<br>`credit_card_user`: Credit Card User<br>`credit_repair`: Credit Repair<br>`credit_report`: Credit Report<br>`education_seeker`: Education Seeker<br>`food_delivery`: Food Delivery<br>`health_insurance`: Health Insurance<br>`home_office`: Home Office<br>... (+11 more) |
| `charitable_donation_causes` | `ARRAY<STRING>` | Individual | No | Causes the person has donated to (e.g., PBS, Arts, Environment, Health) | `Arts`: Arts<br>`Education`: Education<br>`Environment`: Environment<br>`Health`: Health<br>`Non-Religious`: Non-Religious<br>`NPR`: NPR<br>`PBS`: PBS<br>`Politics`: Politics<br>... (+1 more) |

---

## Geography
*Geographic boundaries and geography-based classifications*

| Column Name | Type | Level | PII | Description | Value Mappings / Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `census_block` | `STRING` | Census_Block | No | 15-digit Census Block identifier. | - |
| `cbsa_name` | `STRING` | Census_Block | No | Core-Based Statistical Area (CBSA) metropolitan/micropolitan area name | - |
| `cnecta_name` | `STRING` | Census_Block | No | Combined New England City and Town Area (CNECTA) name | - |
| `metdiv_name` | `STRING` | Census_Block | No | Metropolitan Division name within major CBSAs | - |
| `congressional_name` | `STRING` | Census_Block | No | U.S. Congressional District identifier | - |
| `county_name` | `STRING` | Census_Block | No | County name | - |
| `urban_area_name` | `STRING` | Census_Block | No | Census Urban Area name | - |
| `census_place_name` | `STRING` | Census_Block | No | Census Incorporated Place or CDP name | - |
| `nchs_urban_rural_code` | `INTEGER` | Census_Block | No | NCHS 6-level county classification: 1=Large central metro, 2=Large fringe metro, 3=Medium metro, 4=Small metro, 5=Micropolitan, 6=Noncore | `1`: Large Central Metro<br>`2`: Large Fringe Metro<br>`3`: Medium Metro<br>`4`: Small Metro<br>`5`: Micropolitan<br>`6`: Noncore |
| `nchs_urban_rural_desc` | `STRING` | Census_Block | No | NCHS Urban-Rural county classification description | - |
| `primary_ruca_code` | `INTEGER` | Census_Block | No | Primary RUCA code (1-10) from USDA ERS | `1`: Metropolitan Core<br>`2`: Metropolitan High Commuting<br>`3`: Metropolitan Low Commuting<br>`4`: Micropolitan Core<br>`5`: Micropolitan High Commuting<br>`6`: Micropolitan Low Commuting<br>`7`: Small Town Core<br>`8`: Small Town High Commuting<br>... (+3 more) |
| `primary_ruca_desc` | `STRING` | Census_Block | No | USDA ERS Rural-Urban Commuting Area classification description | - |
| `ruca_pop_density` | `FLOAT` | Census_Block | No | RUCA tract-level population density (persons per square mile) | - |
| `urbanicity` | `STRING` | Census_Block | No | 6-bucket urbanicity classification | `Dense Urban`: Dense Urban<br>`Urban`: Urban<br>`Suburban`: Suburban<br>`Micropolitan`: Micropolitan<br>`Small Town`: Small Town<br>`Rural`: Rural |

---

## Land Context
*Physical environment surrounding the address — land-use classifications, adjacency to natural and built features, and distance to major infrastructure*

| Column Name | Type | Level | PII | Description | Value Mappings / Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `flag_lives_on_military_base` | `BOOLEAN` | Address | No | Address falls within a military installation | - |
| `flag_lives_on_reservation` | `BOOLEAN` | Address | No | Address falls within a Native American reservation | - |
| `flag_lives_on_college_campus` | `BOOLEAN` | Address | No | Address falls within a university or college campus | - |
| `flag_lives_off_college_campus` | `BOOLEAN` | Address | No | Address falls within 1,500 meters of a university or college campus but outside the campus grounds | - |
| `flag_lives_on_farmland` | `BOOLEAN` | Address | No | Address falls within 50 meters of mapped farmland | - |
| `flag_lives_on_waterfront` | `BOOLEAN` | Address | No | Address falls within 50 meters of a coastline, lake, river, or major waterway | - |
| `flag_lives_adjacent_to_park` | `BOOLEAN` | Address | No | Address falls within 500-1500 meters of a park boundary, but outside the park itself | - |
| `flag_lives_in_commercial_zone` | `BOOLEAN` | Address | No | Address falls within a commercial land-use zone | - |
| `flag_lives_on_golf_course` | `BOOLEAN` | Address | No | Address falls within a golf course | - |
| `flag_lives_on_medical_campus` | `BOOLEAN` | Address | No | Address falls within a hospital or major medical clinic campus | - |
| `flag_lives_in_industrial_zone` | `BOOLEAN` | Address | No | Address falls within an industrial or manufacturing zone | - |
| `flag_lives_adjacent_to_industrial` | `BOOLEAN` | Address | No | Address falls within 500 meters of an industrial zone, but outside the zone itself | - |
| `flag_lives_adjacent_to_stadium` | `BOOLEAN` | Address | No | Address falls within 1,500 meters of a stadium, but outside the stadium itself | - |
| `flag_lives_adjacent_to_mall` | `BOOLEAN` | Address | No | Address falls within 500 meters of a shopping mall, but outside the mall itself | - |
| `dist_commercial_airport_m` | `FLOAT` | Address | No | Distance in meters to the nearest commercial airport. | - |
| `dist_convention_center_m` | `FLOAT` | Address | No | Distance in meters to the nearest Convention Center. | - |
| `dist_military_base_m` | `FLOAT` | Address | No | Distance in meters to the nearest Military Base. | - |
| `dist_national_park_m` | `FLOAT` | Address | No | Distance in meters to the nearest National Park. | - |
| `dist_ski_resort_m` | `FLOAT` | Address | No | Distance in meters to the nearest Ski Resort. | - |
| `dist_stadium_m` | `FLOAT` | Address | No | Distance in meters to the nearest Stadium. | - |
| `dist_subway_station_m` | `FLOAT` | Address | No | Distance in meters to the nearest Subway Station. | - |

---

## Census Demographics & Socioeconomic
*Population characteristics from the American Community Survey covering income distribution, educational attainment, housing stock, commuting patterns, and labor force composition*

| Column Name | Type | Level | PII | Description | Value Mappings / Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `acs_aggregate_travel_time_to_work` | `FLOAT` | Census_Tract | No | Raw: aggregate travel time to work (minutes) | - |
| `acs_amerindian_including_hispanic_rate` | `FLOAT` | Census_Tract | No | P: amerindian_including_hispanic / total_pop | - |
| `acs_amerindian_pop_rate` | `FLOAT` | Census_Tract | No | P: amerindian_pop / total_pop | - |
| `acs_armed_forces_rate` | `FLOAT` | Census_Tract | No | P: armed_forces / pop_in_labor_force | - |
| `acs_asian_including_hispanic_rate` | `FLOAT` | Census_Tract | No | P: asian_including_hispanic / total_pop | - |
| `acs_asian_male_45_54_rate` | `FLOAT` | Census_Tract | No | P: asian_male_45_54 / total_pop | - |
| `acs_asian_male_55_64_rate` | `FLOAT` | Census_Tract | No | P: asian_male_55_64 / total_pop | - |
| `acs_asian_pop_rate` | `FLOAT` | Census_Tract | No | P: asian_pop / total_pop | - |
| `acs_associates_degree_rate` | `FLOAT` | Census_Tract | No | P: associates_degree / pop_25_years_over | - |
| `acs_bachelors_degree_2_rate` | `FLOAT` | Census_Tract | No | P: bachelors_degree_2 / pop_25_years_over | - |
| `acs_bachelors_degree_or_higher_25_64_rate` | `FLOAT` | Census_Tract | No | P: bachelors_degree_or_higher_25_64 / pop_25_64 | - |
| `acs_bachelors_degree_rate` | `FLOAT` | Census_Tract | No | P: bachelors_degree / pop_25_years_over | - |
| `acs_black_including_hispanic_rate` | `FLOAT` | Census_Tract | No | P: black_including_hispanic / total_pop | - |
| `acs_black_male_45_54_rate` | `FLOAT` | Census_Tract | No | P: black_male_45_54 / total_pop | - |
| `acs_black_male_55_64_rate` | `FLOAT` | Census_Tract | No | P: black_male_55_64 / total_pop | - |
| `acs_black_pop_rate` | `FLOAT` | Census_Tract | No | P: black_pop / total_pop | - |
| `acs_children_in_single_female_hh_rate` | `FLOAT` | Census_Tract | No | P: children_in_single_female_hh / children | - |
| `acs_children_rate` | `FLOAT` | Census_Tract | No | P: children / total_pop | - |
| `acs_civilian_labor_force_rate` | `FLOAT` | Census_Tract | No | P: civilian_labor_force / pop_in_labor_force | - |
| `acs_commute_10_14_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_10_14_mins / commuters_16_over | - |
| `acs_commute_15_19_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_15_19_mins / commuters_16_over | - |
| `acs_commute_20_24_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_20_24_mins / commuters_16_over | - |
| `acs_commute_25_29_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_25_29_mins / commuters_16_over | - |
| `acs_commute_30_34_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_30_34_mins / commuters_16_over | - |
| `acs_commute_35_39_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_35_39_mins / commuters_16_over | - |
| `acs_commute_35_44_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_35_44_mins / commuters_16_over | - |
| `acs_commute_40_44_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_40_44_mins / commuters_16_over | - |
| `acs_commute_45_59_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_45_59_mins / commuters_16_over | - |
| `acs_commute_5_9_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_5_9_mins / commuters_16_over | - |
| `acs_commute_60_89_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_60_89_mins / commuters_16_over | - |
| `acs_commute_60_more_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_60_more_mins / commuters_16_over | - |
| `acs_commute_90_more_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_90_more_mins / commuters_16_over | - |
| `acs_commute_less_10_mins_rate` | `FLOAT` | Census_Tract | No | P: commute_less_10_mins / commuters_16_over | - |
| `acs_commuters_16_over` | `FLOAT` | Census_Tract | No | Raw: commuters 16 and over | - |
| `acs_commuters_by_bus_rate` | `FLOAT` | Census_Tract | No | P: commuters_by_bus / commuters_16_over | - |
| `acs_commuters_by_car_truck_van_rate` | `FLOAT` | Census_Tract | No | P: commuters_by_car_truck_van / commuters_16_over | - |
| `acs_commuters_by_carpool_rate` | `FLOAT` | Census_Tract | No | P: commuters_by_carpool / commuters_16_over | - |
| `acs_commuters_by_public_transportation_rate` | `FLOAT` | Census_Tract | No | P: commuters_by_public_transportation / commuters_16_over | - |
| `acs_commuters_by_subway_or_elevated_rate` | `FLOAT` | Census_Tract | No | P: commuters_by_subway_or_elevated / commuters_16_over | - |
| `acs_commuters_drove_alone_rate` | `FLOAT` | Census_Tract | No | P: commuters_drove_alone / commuters_16_over | - |
| `acs_different_house_year_ago_different_city_rate` | `FLOAT` | Census_Tract | No | P: different_house_year_ago_different_city / population_1_year_and_over | - |
| `acs_different_house_year_ago_same_city_rate` | `FLOAT` | Census_Tract | No | P: different_house_year_ago_same_city / population_1_year_and_over | - |
| `acs_dwellings_10_to_19_units_rate` | `FLOAT` | Census_Tract | No | P: dwellings_10_to_19_units / housing_units | - |
| `acs_dwellings_1_units_attached_rate` | `FLOAT` | Census_Tract | No | P: dwellings_1_units_attached / housing_units | - |
| `acs_dwellings_1_units_detached_rate` | `FLOAT` | Census_Tract | No | P: dwellings_1_units_detached / housing_units | - |
| `acs_dwellings_20_to_49_units_rate` | `FLOAT` | Census_Tract | No | P: dwellings_20_to_49_units / housing_units | - |
| `acs_dwellings_2_units_rate` | `FLOAT` | Census_Tract | No | P: dwellings_2_units / housing_units | - |
| `acs_dwellings_3_to_4_units_rate` | `FLOAT` | Census_Tract | No | P: dwellings_3_to_4_units / housing_units | - |
| `acs_dwellings_50_or_more_units_rate` | `FLOAT` | Census_Tract | No | P: dwellings_50_or_more_units / housing_units | - |
| `acs_dwellings_5_to_9_units_rate` | `FLOAT` | Census_Tract | No | P: dwellings_5_to_9_units / housing_units | - |
| `acs_employed_agriculture_forestry_fishing_hunting_mining_rate` | `FLOAT` | Census_Tract | No | P: employed_agriculture / employed_pop | - |
| `acs_employed_arts_entertainment_recreation_accommodation_food_rate` | `FLOAT` | Census_Tract | No | P: employed_arts / employed_pop | - |
| `acs_employed_construction_rate` | `FLOAT` | Census_Tract | No | P: employed_construction / employed_pop | - |
| `acs_employed_education_health_social_rate` | `FLOAT` | Census_Tract | No | P: employed_education / employed_pop | - |
| `acs_employed_finance_insurance_real_estate_rate` | `FLOAT` | Census_Tract | No | P: employed_finance / employed_pop | - |
| `acs_employed_information_rate` | `FLOAT` | Census_Tract | No | P: employed_information / employed_pop | - |
| `acs_employed_manufacturing_rate` | `FLOAT` | Census_Tract | No | P: employed_manufacturing / employed_pop | - |
| `acs_employed_other_services_not_public_admin_rate` | `FLOAT` | Census_Tract | No | P: employed_other / employed_pop | - |
| `acs_employed_pop_rate` | `FLOAT` | Census_Tract | No | P: employed_pop / pop_in_labor_force | - |
| `acs_employed_public_administration_rate` | `FLOAT` | Census_Tract | No | P: employed_public_admin / employed_pop | - |
| `acs_employed_retail_trade_rate` | `FLOAT` | Census_Tract | No | P: employed_retail / employed_pop | - |
| `acs_employed_science_management_admin_waste_rate` | `FLOAT` | Census_Tract | No | P: employed_science / employed_pop | - |
| `acs_employed_transportation_warehousing_utilities_rate` | `FLOAT` | Census_Tract | No | P: employed_transport / employed_pop | - |
| `acs_employed_wholesale_trade_rate` | `FLOAT` | Census_Tract | No | P: employed_wholesale / employed_pop | - |
| `acs_families_with_young_children` | `FLOAT` | Census_Tract | No | Raw: families with children under 6 | - |
| `acs_family_households` | `FLOAT` | Census_Tract | No | Raw: tract family households | - |
| `acs_father_in_labor_force_one_parent_families_with_young_children_rate` | `FLOAT` | Census_Tract | No | P: father_in_labor_force_one_parent / families_with_young_children | - |
| `acs_father_one_parent_families_with_young_children_rate` | `FLOAT` | Census_Tract | No | P: father_one_parent / families_with_young_children | - |
| `acs_female_10_to_14_rate` | `FLOAT` | Census_Tract | No | P: female_10_to_14 / total_pop | - |
| `acs_female_15_to_17_rate` | `FLOAT` | Census_Tract | No | P: female_15_to_17 / total_pop | - |
| `acs_female_18_to_19_rate` | `FLOAT` | Census_Tract | No | P: female_18_to_19 / total_pop | - |
| `acs_female_20_rate` | `FLOAT` | Census_Tract | No | P: female_20 / total_pop | - |
| `acs_female_21_rate` | `FLOAT` | Census_Tract | No | P: female_21 / total_pop | - |
| `acs_female_22_to_24_rate` | `FLOAT` | Census_Tract | No | P: female_22_to_24 / total_pop | - |
| `acs_female_25_to_29_rate` | `FLOAT` | Census_Tract | No | P: female_25_to_29 / total_pop | - |
| `acs_female_30_to_34_rate` | `FLOAT` | Census_Tract | No | P: female_30_to_34 / total_pop | - |
| `acs_female_35_to_39_rate` | `FLOAT` | Census_Tract | No | P: female_35_to_39 / total_pop | - |
| `acs_female_40_to_44_rate` | `FLOAT` | Census_Tract | No | P: female_40_to_44 / total_pop | - |
| `acs_female_45_to_49_rate` | `FLOAT` | Census_Tract | No | P: female_45_to_49 / total_pop | - |
| `acs_female_50_to_54_rate` | `FLOAT` | Census_Tract | No | P: female_50_to_54 / total_pop | - |
| `acs_female_55_to_59_rate` | `FLOAT` | Census_Tract | No | P: female_55_to_59 / total_pop | - |
| `acs_female_5_to_9_rate` | `FLOAT` | Census_Tract | No | P: female_5_to_9 / total_pop | - |
| `acs_female_60_to_61_rate` | `FLOAT` | Census_Tract | No | P: female_60_to_61 / total_pop | - |
| `acs_female_62_to_64_rate` | `FLOAT` | Census_Tract | No | P: female_62_to_64 / total_pop | - |
| `acs_female_65_to_66_rate` | `FLOAT` | Census_Tract | No | P: female_65_to_66 / total_pop | - |
| `acs_female_67_to_69_rate` | `FLOAT` | Census_Tract | No | P: female_67_to_69 / total_pop | - |
| `acs_female_70_to_74_rate` | `FLOAT` | Census_Tract | No | P: female_70_to_74 / total_pop | - |
| `acs_female_75_to_79_rate` | `FLOAT` | Census_Tract | No | P: female_75_to_79 / total_pop | - |
| `acs_female_80_to_84_rate` | `FLOAT` | Census_Tract | No | P: female_80_to_84 / total_pop | - |
| `acs_female_85_and_over_rate` | `FLOAT` | Census_Tract | No | P: female_85_and_over / total_pop | - |
| `acs_female_female_households_rate` | `FLOAT` | Census_Tract | No | P: female_female_households / households | - |
| `acs_female_pop_rate` | `FLOAT` | Census_Tract | No | P: female_pop / total_pop | - |
| `acs_female_under_5_rate` | `FLOAT` | Census_Tract | No | P: female_under_5 / total_pop | - |
| `acs_four_more_cars_rate` | `FLOAT` | Census_Tract | No | P: four_more_cars / occupied_housing_units | - |
| `acs_gini_index` | `FLOAT` | Census_Tract | No | Raw: Gini index of income inequality | - |
| `acs_graduate_professional_degree_rate` | `FLOAT` | Census_Tract | No | P: graduate_professional_degree / pop_25_years_over | - |
| `acs_group_quarters_rate` | `FLOAT` | Census_Tract | No | P: group_quarters / total_pop | - |
| `acs_high_school_diploma_rate` | `FLOAT` | Census_Tract | No | P: high_school_diploma / pop_25_years_over | - |
| `acs_high_school_including_ged_rate` | `FLOAT` | Census_Tract | No | P: high_school_including_ged / pop_25_years_over | - |
| `acs_hispanic_any_race_rate` | `FLOAT` | Census_Tract | No | P: hispanic_any_race / total_pop | - |
| `acs_hispanic_male_45_54_rate` | `FLOAT` | Census_Tract | No | P: hispanic_male_45_54 / total_pop | - |
| `acs_hispanic_male_55_64_rate` | `FLOAT` | Census_Tract | No | P: hispanic_male_55_64 / total_pop | - |
| `acs_hispanic_pop_rate` | `FLOAT` | Census_Tract | No | P: hispanic_pop / total_pop | - |
| `acs_households` | `FLOAT` | Census_Tract | No | Raw: tract total households | - |
| `acs_households_public_asst_or_food_stamps_rate` | `FLOAT` | Census_Tract | No | P: households_public_asst_or_food_stamps / households | - |
| `acs_households_retirement_income_rate` | `FLOAT` | Census_Tract | No | P: households_retirement_income / households | - |
| `acs_housing_built_1939_or_earlier_rate` | `FLOAT` | Census_Tract | No | P: housing_built_1939_or_earlier / housing_units | - |
| `acs_housing_built_2000_to_2004_rate` | `FLOAT` | Census_Tract | No | P: housing_built_2000_to_2004 / housing_units | - |
| `acs_housing_built_2005_or_later_rate` | `FLOAT` | Census_Tract | No | P: housing_built_2005_or_later / housing_units | - |
| `acs_housing_units` | `FLOAT` | Census_Tract | No | Raw: tract total housing units | - |
| `acs_housing_units_renter_occupied_rate` | `FLOAT` | Census_Tract | No | P: housing_units_renter_occupied / housing_units | - |
| `acs_in_grades_1_to_4_rate` | `FLOAT` | Census_Tract | No | P: in_grades_1_to_4 / population_3_years_over | - |
| `acs_in_grades_5_to_8_rate` | `FLOAT` | Census_Tract | No | P: in_grades_5_to_8 / population_3_years_over | - |
| `acs_in_grades_9_to_12_rate` | `FLOAT` | Census_Tract | No | P: in_grades_9_to_12 / population_3_years_over | - |
| `acs_in_school_rate` | `FLOAT` | Census_Tract | No | P: in_school / population_3_years_over | - |
| `acs_in_undergrad_college_rate` | `FLOAT` | Census_Tract | No | P: in_undergrad_college / population_3_years_over | - |
| `acs_income_100000_124999_rate` | `FLOAT` | Census_Tract | No | P: income_100000_124999 / households | - |
| `acs_income_10000_14999_rate` | `FLOAT` | Census_Tract | No | P: income_10000_14999 / households | - |
| `acs_income_125000_149999_rate` | `FLOAT` | Census_Tract | No | P: income_125000_149999 / households | - |
| `acs_income_150000_199999_rate` | `FLOAT` | Census_Tract | No | P: income_150000_199999 / households | - |
| `acs_income_15000_19999_rate` | `FLOAT` | Census_Tract | No | P: income_15000_19999 / households | - |
| `acs_income_200000_or_more_rate` | `FLOAT` | Census_Tract | No | P: income_200000_or_more / households | - |
| `acs_income_20000_24999_rate` | `FLOAT` | Census_Tract | No | P: income_20000_24999 / households | - |
| `acs_income_25000_29999_rate` | `FLOAT` | Census_Tract | No | P: income_25000_29999 / households | - |
| `acs_income_30000_34999_rate` | `FLOAT` | Census_Tract | No | P: income_30000_34999 / households | - |
| `acs_income_35000_39999_rate` | `FLOAT` | Census_Tract | No | P: income_35000_39999 / households | - |
| `acs_income_40000_44999_rate` | `FLOAT` | Census_Tract | No | P: income_40000_44999 / households | - |
| `acs_income_45000_49999_rate` | `FLOAT` | Census_Tract | No | P: income_45000_49999 / households | - |
| `acs_income_50000_59999_rate` | `FLOAT` | Census_Tract | No | P: income_50000_59999 / households | - |
| `acs_income_60000_74999_rate` | `FLOAT` | Census_Tract | No | P: income_60000_74999 / households | - |
| `acs_income_75000_99999_rate` | `FLOAT` | Census_Tract | No | P: income_75000_99999 / households | - |
| `acs_income_less_10000_rate` | `FLOAT` | Census_Tract | No | P: income_less_10000 / households | - |
| `acs_income_per_capita` | `FLOAT` | Census_Tract | No | Raw: per capita income ($) | - |
| `acs_less_one_year_college_rate` | `FLOAT` | Census_Tract | No | P: less_one_year_college / pop_25_years_over | - |
| `acs_less_than_high_school_graduate_rate` | `FLOAT` | Census_Tract | No | P: less_than_high_school_graduate / pop_25_years_over | - |
| `acs_male_10_to_14_rate` | `FLOAT` | Census_Tract | No | P: male_10_to_14 / total_pop | - |
| `acs_male_15_to_17_rate` | `FLOAT` | Census_Tract | No | P: male_15_to_17 / total_pop | - |
| `acs_male_18_to_19_rate` | `FLOAT` | Census_Tract | No | P: male_18_to_19 / total_pop | - |
| `acs_male_20_rate` | `FLOAT` | Census_Tract | No | P: male_20 / total_pop | - |
| `acs_male_21_rate` | `FLOAT` | Census_Tract | No | P: male_21 / total_pop | - |
| `acs_male_22_to_24_rate` | `FLOAT` | Census_Tract | No | P: male_22_to_24 / total_pop | - |
| `acs_male_25_to_29_rate` | `FLOAT` | Census_Tract | No | P: male_25_to_29 / total_pop | - |
| `acs_male_30_to_34_rate` | `FLOAT` | Census_Tract | No | P: male_30_to_34 / total_pop | - |
| `acs_male_35_to_39_rate` | `FLOAT` | Census_Tract | No | P: male_35_to_39 / total_pop | - |
| `acs_male_40_to_44_rate` | `FLOAT` | Census_Tract | No | P: male_40_to_44 / total_pop | - |
| `acs_male_45_64_associates_degree_rate` | `FLOAT` | Census_Tract | No | P: male_45_64_associates_degree / male_45_to_64 | - |
| `acs_male_45_64_bachelors_degree_rate` | `FLOAT` | Census_Tract | No | P: male_45_64_bachelors_degree / male_45_to_64 | - |
| `acs_male_45_64_grade_9_12_rate` | `FLOAT` | Census_Tract | No | P: male_45_64_grade_9_12 / male_45_to_64 | - |
| `acs_male_45_64_graduate_degree_rate` | `FLOAT` | Census_Tract | No | P: male_45_64_graduate_degree / male_45_to_64 | - |
| `acs_male_45_64_high_school_rate` | `FLOAT` | Census_Tract | No | P: male_45_64_high_school / male_45_to_64 | - |
| `acs_male_45_64_less_than_9_grade_rate` | `FLOAT` | Census_Tract | No | P: male_45_64_less_than_9_grade / male_45_to_64 | - |
| `acs_male_45_64_some_college_rate` | `FLOAT` | Census_Tract | No | P: male_45_64_some_college / male_45_to_64 | - |
| `acs_male_45_to_49_rate` | `FLOAT` | Census_Tract | No | P: male_45_to_49 / total_pop | - |
| `acs_male_45_to_64` | `FLOAT` | Census_Tract | No | Raw: male population 45-64 | - |
| `acs_male_50_to_54_rate` | `FLOAT` | Census_Tract | No | P: male_50_to_54 / total_pop | - |
| `acs_male_55_to_59_rate` | `FLOAT` | Census_Tract | No | P: male_55_to_59 / total_pop | - |
| `acs_male_5_to_9_rate` | `FLOAT` | Census_Tract | No | P: male_5_to_9 / total_pop | - |
| `acs_male_60_to_61_rate` | `FLOAT` | Census_Tract | No | P: male_60_to_61 / total_pop | - |
| `acs_male_62_to_64_rate` | `FLOAT` | Census_Tract | No | P: male_62_to_64 / total_pop | - |
| `acs_male_65_to_66_rate` | `FLOAT` | Census_Tract | No | P: male_65_to_66 / total_pop | - |
| `acs_male_67_to_69_rate` | `FLOAT` | Census_Tract | No | P: male_67_to_69 / total_pop | - |
| `acs_male_70_to_74_rate` | `FLOAT` | Census_Tract | No | P: male_70_to_74 / total_pop | - |
| `acs_male_75_to_79_rate` | `FLOAT` | Census_Tract | No | P: male_75_to_79 / total_pop | - |
| `acs_male_80_to_84_rate` | `FLOAT` | Census_Tract | No | P: male_80_to_84 / total_pop | - |
| `acs_male_85_and_over_rate` | `FLOAT` | Census_Tract | No | P: male_85_and_over / total_pop | - |
| `acs_male_male_households_rate` | `FLOAT` | Census_Tract | No | P: male_male_households / households | - |
| `acs_male_pop_rate` | `FLOAT` | Census_Tract | No | P: male_pop / total_pop | - |
| `acs_male_under_5_rate` | `FLOAT` | Census_Tract | No | P: male_under_5 / total_pop | - |
| `acs_management_business_sci_arts_employed_rate` | `FLOAT` | Census_Tract | No | P: management_business / employed_pop | - |
| `acs_married_households_rate` | `FLOAT` | Census_Tract | No | P: married_households / households | - |
| `acs_masters_degree_rate` | `FLOAT` | Census_Tract | No | P: masters_degree / pop_25_years_over | - |
| `acs_median_age` | `FLOAT` | Census_Tract | No | Raw: median age | - |
| `acs_median_income` | `FLOAT` | Census_Tract | No | Raw: median household income ($) | - |
| `acs_median_rent` | `FLOAT` | Census_Tract | No | Raw: median gross rent ($) | - |
| `acs_median_year_structure_built` | `FLOAT` | Census_Tract | No | Raw: median year structure built | - |
| `acs_million_dollar_housing_units_rate` | `FLOAT` | Census_Tract | No | P: million_dollar_housing_units / housing_units | - |
| `acs_mobile_homes_rate` | `FLOAT` | Census_Tract | No | P: mobile_homes / housing_units | - |
| `acs_mortgaged_housing_units_rate` | `FLOAT` | Census_Tract | No | P: mortgaged_housing_units / housing_units | - |
| `acs_no_car_rate` | `FLOAT` | Census_Tract | No | P: no_car / occupied_housing_units | - |
| `acs_no_cars_rate` | `FLOAT` | Census_Tract | No | P: no_cars / occupied_housing_units | - |
| `acs_nonfamily_households` | `FLOAT` | Census_Tract | No | Raw: nonfamily households | - |
| `acs_not_hispanic_pop_rate` | `FLOAT` | Census_Tract | No | P: not_hispanic_pop / total_pop | - |
| `acs_not_in_labor_force_rate` | `FLOAT` | Census_Tract | No | P: not_in_labor_force / pop_in_labor_force | - |
| `acs_not_us_citizen_pop_rate` | `FLOAT` | Census_Tract | No | P: not_us_citizen_pop / total_pop | - |
| `acs_occupation_management_arts_rate` | `FLOAT` | Census_Tract | No | P: occupation_management_arts / employed_pop | - |
| `acs_occupation_natural_resources_construction_maintenance_rate` | `FLOAT` | Census_Tract | No | P: occupation_natural_resources / employed_pop | - |
| `acs_occupation_production_transportation_material_rate` | `FLOAT` | Census_Tract | No | P: occupation_production / employed_pop | - |
| `acs_occupation_sales_office_rate` | `FLOAT` | Census_Tract | No | P: occupation_sales_office / employed_pop | - |
| `acs_occupation_services_rate` | `FLOAT` | Census_Tract | No | P: occupation_services / employed_pop | - |
| `acs_occupied_housing_units` | `FLOAT` | Census_Tract | No | Raw: occupied housing units | - |
| `acs_one_car_rate` | `FLOAT` | Census_Tract | No | P: one_car / occupied_housing_units | - |
| `acs_one_parent_families_with_young_children_rate` | `FLOAT` | Census_Tract | No | P: one_parent / families_with_young_children | - |
| `acs_one_year_more_college_rate` | `FLOAT` | Census_Tract | No | P: one_year_more_college / pop_25_years_over | - |
| `acs_other_race_pop_rate` | `FLOAT` | Census_Tract | No | P: other_race_pop / total_pop | - |
| `acs_owner_occupied_housing_units_lower_value_quartile` | `FLOAT` | Census_Tract | No | Raw: lower quartile home value ($) | - |
| `acs_owner_occupied_housing_units_median_value` | `FLOAT` | Census_Tract | No | Raw: median home value ($) | - |
| `acs_owner_occupied_housing_units_rate` | `FLOAT` | Census_Tract | No | P: owner_occupied_housing_units / housing_units | - |
| `acs_owner_occupied_housing_units_upper_value_quartile` | `FLOAT` | Census_Tract | No | Raw: upper quartile home value ($) | - |
| `acs_percent_income_spent_on_rent` | `FLOAT` | Census_Tract | No | Raw: percent of income spent on rent | - |
| `acs_pop_16_over` | `FLOAT` | Census_Tract | No | Raw: population 16 and over | - |
| `acs_pop_25_64` | `FLOAT` | Census_Tract | No | Raw: population 25-64 | - |
| `acs_pop_25_years_over` | `FLOAT` | Census_Tract | No | Raw: population 25 years and over | - |
| `acs_pop_5_years_over` | `FLOAT` | Census_Tract | No | Raw: population 5 years and over | - |
| `acs_pop_determined_poverty_status` | `FLOAT` | Census_Tract | No | Raw: population for poverty determination | - |
| `acs_pop_in_labor_force` | `FLOAT` | Census_Tract | No | Raw: population in labor force | - |
| `acs_population_1_year_and_over` | `FLOAT` | Census_Tract | No | Raw: population 1 year and over | - |
| `acs_population_3_years_over` | `FLOAT` | Census_Tract | No | Raw: population 3 years and over | - |
| `acs_poverty_rate` | `FLOAT` | Census_Tract | No | P: poverty / pop_determined_poverty_status | - |
| `acs_rent_10_to_15_percent_rate` | `FLOAT` | Census_Tract | No | P: rent_10_to_15_percent / occupied_housing_units | - |
| `acs_rent_15_to_20_percent_rate` | `FLOAT` | Census_Tract | No | P: rent_15_to_20_percent / occupied_housing_units | - |
| `acs_rent_20_to_25_percent_rate` | `FLOAT` | Census_Tract | No | P: rent_20_to_25_percent / occupied_housing_units | - |
| `acs_rent_25_to_30_percent_rate` | `FLOAT` | Census_Tract | No | P: rent_25_to_30_percent / occupied_housing_units | - |
| `acs_rent_30_to_35_percent_rate` | `FLOAT` | Census_Tract | No | P: rent_30_to_35_percent / occupied_housing_units | - |
| `acs_rent_35_to_40_percent_rate` | `FLOAT` | Census_Tract | No | P: rent_35_to_40_percent / occupied_housing_units | - |
| `acs_rent_40_to_50_percent_rate` | `FLOAT` | Census_Tract | No | P: rent_40_to_50_percent / occupied_housing_units | - |
| `acs_rent_burden_not_computed_rate` | `FLOAT` | Census_Tract | No | P: rent_burden_not_computed / occupied_housing_units | - |
| `acs_rent_over_50_percent_rate` | `FLOAT` | Census_Tract | No | P: rent_over_50_percent / occupied_housing_units | - |
| `acs_rent_under_10_percent_rate` | `FLOAT` | Census_Tract | No | P: rent_under_10_percent / occupied_housing_units | - |
| `acs_renter_occupied_housing_units_paying_cash_median_gross_rent` | `FLOAT` | Census_Tract | No | Raw: median gross rent for cash-paying renters ($) | - |
| `acs_sales_office_employed_rate` | `FLOAT` | Census_Tract | No | P: sales_office / employed_pop | - |
| `acs_some_college_and_associates_degree_rate` | `FLOAT` | Census_Tract | No | P: some_college_and_associates_degree / pop_25_years_over | - |
| `acs_speak_only_english_at_home_rate` | `FLOAT` | Census_Tract | No | P: speak_only_english_at_home / pop_5_years_over | - |
| `acs_speak_spanish_at_home_low_english_rate` | `FLOAT` | Census_Tract | No | P: speak_spanish_at_home_low_english / pop_5_years_over | - |
| `acs_speak_spanish_at_home_rate` | `FLOAT` | Census_Tract | No | P: speak_spanish_at_home / pop_5_years_over | - |
| `acs_three_cars_rate` | `FLOAT` | Census_Tract | No | P: three_cars / occupied_housing_units | - |
| `acs_total_pop` | `FLOAT` | Census_Tract | No | Raw: tract total population | - |
| `acs_two_cars_rate` | `FLOAT` | Census_Tract | No | P: two_cars / occupied_housing_units | - |
| `acs_two_or_more_races_pop_rate` | `FLOAT` | Census_Tract | No | P: two_or_more_races_pop / total_pop | - |
| `acs_two_parent_families_with_young_children_rate` | `FLOAT` | Census_Tract | No | P: two_parent / families_with_young_children | - |
| `acs_two_parents_father_in_labor_force_families_with_young_children_rate` | `FLOAT` | Census_Tract | No | P: two_parents_father_in_lf / families_with_young_children | - |
| `acs_two_parents_in_labor_force_families_with_young_children_rate` | `FLOAT` | Census_Tract | No | P: two_parents_in_labor_force / families_with_young_children | - |
| `acs_two_parents_mother_in_labor_force_families_with_young_children_rate` | `FLOAT` | Census_Tract | No | P: two_parents_mother_in_lf / families_with_young_children | - |
| `acs_two_parents_not_in_labor_force_families_with_young_children_rate` | `FLOAT` | Census_Tract | No | P: two_parents_not_in_lf / families_with_young_children | - |
| `acs_unemployed_pop_rate` | `FLOAT` | Census_Tract | No | P: unemployed_pop / pop_in_labor_force | - |
| `acs_vacant_housing_units_for_rent_rate` | `FLOAT` | Census_Tract | No | P: vacant_housing_units_for_rent / housing_units | - |
| `acs_vacant_housing_units_for_sale_rate` | `FLOAT` | Census_Tract | No | P: vacant_housing_units_for_sale / housing_units | - |
| `acs_vacant_housing_units_rate` | `FLOAT` | Census_Tract | No | P: vacant_housing_units / housing_units | - |
| `acs_walked_to_work_rate` | `FLOAT` | Census_Tract | No | P: walked_to_work / workers_16_and_over | - |
| `acs_white_including_hispanic_rate` | `FLOAT` | Census_Tract | No | P: white_including_hispanic / total_pop | - |
| `acs_white_male_45_54_rate` | `FLOAT` | Census_Tract | No | P: white_male_45_54 / total_pop | - |
| `acs_white_male_55_64_rate` | `FLOAT` | Census_Tract | No | P: white_male_55_64 / total_pop | - |
| `acs_white_pop_rate` | `FLOAT` | Census_Tract | No | P: white_pop / total_pop | - |
| `acs_worked_at_home_rate` | `FLOAT` | Census_Tract | No | P: worked_at_home / workers_16_and_over | - |
| `acs_workers_16_and_over` | `FLOAT` | Census_Tract | No | Raw: workers 16 and over | - |

---

## Health
*Community-level health outcomes and risk factors, including chronic disease prevalence, preventive care utilization, and disability rates*

| Column Name | Type | Level | PII | Description | Value Mappings / Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `cdc_access2_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Lack of health insurance among adults 18-64 (0-1 proportion) | - |
| `cdc_arthritis_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Arthritis among adults 18+ (0-1 proportion) | - |
| `cdc_binge_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Binge drinking among adults 18+ (0-1 proportion) | - |
| `cdc_bphigh_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: High blood pressure among adults 18+ (0-1 proportion) | - |
| `cdc_bpmed_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Taking BP medication among adults with high BP (0-1 proportion) | - |
| `cdc_cancer_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Cancer (excl skin) among adults 18+ (0-1 proportion) | - |
| `cdc_casthma_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Current asthma among adults 18+ (0-1 proportion) | - |
| `cdc_chd_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Coronary heart disease among adults 18+ (0-1 proportion) | - |
| `cdc_checkup_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Routine checkup past year among adults 18+ (0-1 proportion) | - |
| `cdc_cholscreen_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Cholesterol screening among adults 18+ (0-1 proportion) | - |
| `cdc_cognition_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Cognitive disability among adults 18+ (0-1 proportion) | - |
| `cdc_colon_screen_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Colorectal cancer screening among adults 45-75 (0-1 proportion) | - |
| `cdc_copd_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: COPD among adults 18+ (0-1 proportion) | - |
| `cdc_csmoking_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Current smoking among adults 18+ (0-1 proportion) | - |
| `cdc_dental_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Dental visit past year among adults 18+ (0-1 proportion) | - |
| `cdc_depression_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Depression among adults 18+ (0-1 proportion) | - |
| `cdc_diabetes_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Diagnosed diabetes among adults 18+ (0-1 proportion) | - |
| `cdc_disability_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Any disability among adults 18+ (0-1 proportion) | - |
| `cdc_emotionspt_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Lack of social/emotional support among adults 18+ (0-1 proportion) | - |
| `cdc_foodinsecu_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Food insecurity among adults 18+ (0-1 proportion) | - |
| `cdc_foodstamp_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Food stamp/SNAP receipt among adults 18+ (0-1 proportion) | - |
| `cdc_ghlth_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Fair or poor self-rated health among adults 18+ (0-1 proportion) | - |
| `cdc_hearing_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Hearing disability among adults 18+ (0-1 proportion) | - |
| `cdc_highchol_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: High cholesterol among screened adults (0-1 proportion) | - |
| `cdc_housinsecu_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Housing insecurity among adults 18+ (0-1 proportion) | - |
| `cdc_indeplive_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Independent living disability among adults 18+ (0-1 proportion) | - |
| `cdc_lacktrpt_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Lack of reliable transportation among adults 18+ (0-1 proportion) | - |
| `cdc_loneliness_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Loneliness among adults 18+ (0-1 proportion) | - |
| `cdc_lpa_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: No leisure-time physical activity among adults 18+ (0-1 proportion) | - |
| `cdc_mammouse_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Mammography use among women 50-74 (0-1 proportion) | - |
| `cdc_mhlth_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Frequent mental distress (14+ days/mo) among adults 18+ (0-1 proportion) | - |
| `cdc_mobility_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Mobility disability among adults 18+ (0-1 proportion) | - |
| `cdc_obesity_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Obesity (BMI >= 30) among adults 18+ (0-1 proportion) | - |
| `cdc_phlth_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Frequent physical distress (14+ days/mo) among adults 18+ (0-1 proportion) | - |
| `cdc_selfcare_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Self-care disability among adults 18+ (0-1 proportion) | - |
| `cdc_shututility_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Utility shutoff threat among adults 18+ (0-1 proportion) | - |
| `cdc_sleep_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Short sleep duration (<7 hrs) among adults 18+ (0-1 proportion) | - |
| `cdc_stroke_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Stroke among adults 18+ (0-1 proportion) | - |
| `cdc_teethlost_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: All teeth lost among adults 65+ (0-1 proportion) | - |
| `cdc_vision_crudeprev` | `FLOAT` | Census_Tract | No | Crude prevalence: Vision disability among adults 18+ (0-1 proportion) | - |

---

## Environment & Risk
*Natural hazard exposure and energy vulnerability metrics from federal risk assessment programs*

| Column Name | Type | Level | PII | Description | Value Mappings / Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `doe_avg_annual_energy_cost` | `FLOAT` | Census_Tract | No | Weighted avg annual energy cost ($) | - |
| `doe_avg_household_income` | `FLOAT` | Census_Tract | No | Weighted avg annual household income ($) | - |
| `doe_energy_burden` | `FLOAT` | Census_Tract | No | Energy burden ratio (energy cost / income). Above 0.06 = high burden per DOE | - |
| `fema_eal_score` | `FLOAT` | Census_Tract | No | Expected Annual Loss score (annualized $ losses from 18 hazard types) | - |
| `fema_resl_score` | `FLOAT` | Census_Tract | No | Community Resilience score | - |
| `fema_risk_index` | `FLOAT` | Census_Tract | No | FEMA NRI composite risk score (0-100) | - |
| `fema_risk_rating` | `STRING` | Census_Tract | No | Categorical risk rating: Very Low to Very High | `Very Low`: Very Low<br>`Relatively Low`: Relatively Low<br>`Relatively Moderate`: Relatively Moderate<br>`Relatively High`: Relatively High<br>`Very High`: Very High |
| `fema_sovi_score` | `FLOAT` | Census_Tract | No | Social Vulnerability Index score | - |

---

## Economic Indicators
*Regional economic conditions — employment dynamics, public safety indicators, housing market trends, and tax-reported income distributions*

| Column Name | Type | Level | PII | Description | Value Mappings / Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `bls_employed` | `INTEGER` | County | No | Most recent monthly employed count | - |
| `bls_labor_force` | `INTEGER` | County | No | Most recent monthly labor force count | - |
| `bls_unemployed` | `INTEGER` | County | No | Most recent monthly unemployed count | - |
| `bls_unemployment_rate` | `FLOAT` | County | No | Most recent monthly unemployment rate (0-1 proportion) | - |
| `fbi_property_crime_rate` | `FLOAT` | State | No | Property crimes per 100k population (most recent year, state-level) | - |
| `fbi_violent_crime_rate` | `FLOAT` | State | No | Violent crimes per 100k population (most recent year, state-level) | - |
| `fhfa_hpi2000` | `FLOAT` | Census_Tract | No | House Price Index rebased to 2000=100 | - |
| `fhfa_hpi_annual_change` | `FLOAT` | Census_Tract | No | Year-over-year change in tract-level HPI (0-1 proportion, e.g. 0.05 = 5% increase) | - |
| `fhfa_hpi_year` | `INTEGER` | Census_Tract | No | Calendar year of the most recent HPI observation | - |
| `irs_avg_agi_per_return` | `FLOAT` | Zip | No | Average AGI per return in the ZIP ($thousands) | - |
| `irs_total_agi_thousands` | `FLOAT` | Zip | No | Total Adjusted Gross Income in the ZIP (thousands of $) | - |
| `irs_total_returns` | `INTEGER` | Zip | No | Total individual income tax returns filed in the ZIP | - |

---

## Brand Proximity
*Physical proximity to tracked anchor brands — continuous distance measurements and an array tracking nearby anchor brands*

| Column Name | Type | Level | PII | Description | Value Mappings / Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `brands_near` | `ARRAY<STRING>` | Address | No | Brands within the targeting radius, factoring in urbanicity and POI type | `Whole Foods Market`: Whole Foods Market<br>`Wegmans`: Wegmans<br>`Apple`: Apple<br>`Tesla`: Tesla<br>`Equinox`: Equinox<br>`Lululemon`: Lululemon<br>`Nordstrom`: Nordstrom<br>`Restoration Hardware`: Restoration Hardware<br>... (+90 more) |
| `dist_24_hour_fitness_m` | `FLOAT` | Address | No | Distance in meters to the nearest 24 Hour Fitness. | - |
| `dist_7_eleven_m` | `FLOAT` | Address | No | Distance in meters to the nearest 7 Eleven. | - |
| `dist_advance_auto_parts_m` | `FLOAT` | Address | No | Distance in meters to the nearest Advance Auto Parts. | - |
| `dist_aldi_m` | `FLOAT` | Address | No | Distance in meters to the nearest Aldi. | - |
| `dist_anytime_fitness_m` | `FLOAT` | Address | No | Distance in meters to the nearest Anytime Fitness. | - |
| `dist_apple_m` | `FLOAT` | Address | No | Distance in meters to the nearest Apple. | - |
| `dist_audi_m` | `FLOAT` | Address | No | Distance in meters to the nearest Audi. | - |
| `dist_autozone_m` | `FLOAT` | Address | No | Distance in meters to the nearest Autozone. | - |
| `dist_bank_of_america_m` | `FLOAT` | Address | No | Distance in meters to the nearest Bank Of America. | - |
| `dist_bjs_wholesale_m` | `FLOAT` | Address | No | Distance in meters to the nearest Bjs Wholesale. | - |
| `dist_bmw_m` | `FLOAT` | Address | No | Distance in meters to the nearest Bmw. | - |
| `dist_bp_m` | `FLOAT` | Address | No | Distance in meters to the nearest Bp. | - |
| `dist_burger_king_m` | `FLOAT` | Address | No | Distance in meters to the nearest Burger King. | - |
| `dist_capital_one_m` | `FLOAT` | Address | No | Distance in meters to the nearest Capital One. | - |
| `dist_caseys_m` | `FLOAT` | Address | No | Distance in meters to the nearest Caseys. | - |
| `dist_chase_m` | `FLOAT` | Address | No | Distance in meters to the nearest Chase. | - |
| `dist_chevron_m` | `FLOAT` | Address | No | Distance in meters to the nearest Chevron. | - |
| `dist_chick_fil_a_m` | `FLOAT` | Address | No | Distance in meters to the nearest Chick-fil-A. | - |
| `dist_chipotle_mexican_grill_m` | `FLOAT` | Address | No | Distance in meters to the nearest Chipotleexican Grill. | - |
| `dist_citibank_m` | `FLOAT` | Address | No | Distance in meters to the nearest Citibank. | - |
| `dist_costco_m` | `FLOAT` | Address | No | Distance in meters to the nearest Costco. | - |
| `dist_crate_barrel_m` | `FLOAT` | Address | No | Distance in meters to the nearest Crate Barrel. | - |
| `dist_crunch_fitness_m` | `FLOAT` | Address | No | Distance in meters to the nearest Crunch Fitness. | - |
| `dist_culvers_m` | `FLOAT` | Address | No | Distance in meters to the nearest Culvers. | - |
| `dist_cvs_pharmacy_m` | `FLOAT` | Address | No | Distance in meters to the nearest Cvs Pharmacy. | - |
| `dist_dairy_queen_m` | `FLOAT` | Address | No | Distance in meters to the nearest Dairy Queen. | - |
| `dist_dollar_general_m` | `FLOAT` | Address | No | Distance in meters to the nearest Dollar General. | - |
| `dist_dollar_tree_m` | `FLOAT` | Address | No | Distance in meters to the nearest Dollar Tree. | - |
| `dist_dominos_pizza_m` | `FLOAT` | Address | No | Distance in meters to the nearest Dominos Pizza. | - |
| `dist_dunkin_m` | `FLOAT` | Address | No | Distance in meters to the nearest Dunkin. | - |
| `dist_equinox_m` | `FLOAT` | Address | No | Distance in meters to the nearest Equinox. | - |
| `dist_exxon_mobil_stations_m` | `FLOAT` | Address | No | Distance in meters to the nearest Exxonobil Stations. | - |
| `dist_family_dollar_m` | `FLOAT` | Address | No | Distance in meters to the nearest Family Dollar. | - |
| `dist_fedex_office_m` | `FLOAT` | Address | No | Distance in meters to the nearest Fedex Office. | - |
| `dist_five_guys_m` | `FLOAT` | Address | No | Distance in meters to the nearest Five Guys. | - |
| `dist_gnc_live_well_m` | `FLOAT` | Address | No | Distance in meters to the nearest Gnc Live Well. | - |
| `dist_golds_gym_m` | `FLOAT` | Address | No | Distance in meters to the nearest Golds Gym. | - |
| `dist_h_e_b_m` | `FLOAT` | Address | No | Distance in meters to the nearest H-E-B. | - |
| `dist_harris_teeter_m` | `FLOAT` | Address | No | Distance in meters to the nearest Harris Teeter. | - |
| `dist_in_n_out_burger_m` | `FLOAT` | Address | No | Distance in meters to the nearest In-N-Out Burger. | - |
| `dist_jiffy_lube_m` | `FLOAT` | Address | No | Distance in meters to the nearest Jiffy Lube. | - |
| `dist_kfc_m` | `FLOAT` | Address | No | Distance in meters to the nearest Kfc. | - |
| `dist_kroger_m` | `FLOAT` | Address | No | Distance in meters to the nearest Kroger. | - |
| `dist_la_fitness_m` | `FLOAT` | Address | No | Distance in meters to the nearest La Fitness. | - |
| `dist_lexus_m` | `FLOAT` | Address | No | Distance in meters to the nearest Lexus. | - |
| `dist_little_caesars_m` | `FLOAT` | Address | No | Distance in meters to the nearest Little Caesars. | - |
| `dist_lowes_m` | `FLOAT` | Address | No | Distance in meters to the nearest Lowes. | - |
| `dist_lululemon_m` | `FLOAT` | Address | No | Distance in meters to the nearest Lululemon. | - |
| `dist_mcdonalds_m` | `FLOAT` | Address | No | Distance in meters to the nearest Mcdonalds. | - |
| `dist_meijer_m` | `FLOAT` | Address | No | Distance in meters to the nearest Meijer. | - |
| `dist_menards_m` | `FLOAT` | Address | No | Distance in meters to the nearest Menards. | - |
| `dist_mercedes_benz_m` | `FLOAT` | Address | No | Distance in meters to the nearest Mercedes Benz. | - |
| `dist_nordstrom_m` | `FLOAT` | Address | No | Distance in meters to the nearest Nordstrom. | - |
| `dist_orangetheory_fitness_m` | `FLOAT` | Address | No | Distance in meters to the nearest Orangetheory Fitness. | - |
| `dist_oreilly_auto_parts_m` | `FLOAT` | Address | No | Distance in meters to the nearest Oreilly Auto Parts. | - |
| `dist_panera_bread_m` | `FLOAT` | Address | No | Distance in meters to the nearest Panera Bread. | - |
| `dist_papa_johns_pizza_m` | `FLOAT` | Address | No | Distance in meters to the nearest Papa Johns Pizza. | - |
| `dist_peloton_m` | `FLOAT` | Address | No | Distance in meters to the nearest Peloton. | - |
| `dist_pizza_hut_m` | `FLOAT` | Address | No | Distance in meters to the nearest Pizza Hut. | - |
| `dist_planet_fitness_m` | `FLOAT` | Address | No | Distance in meters to the nearest Planet Fitness. | - |
| `dist_pnc_m` | `FLOAT` | Address | No | Distance in meters to the nearest Pnc. | - |
| `dist_popeyes_louisiana_kitchen_m` | `FLOAT` | Address | No | Distance in meters to the nearest Popeyes Louisiana Kitchen. | - |
| `dist_porsche_m` | `FLOAT` | Address | No | Distance in meters to the nearest Porsche. | - |
| `dist_public_storage_m` | `FLOAT` | Address | No | Distance in meters to the nearest Public Storage. | - |
| `dist_publix_m` | `FLOAT` | Address | No | Distance in meters to the nearest Publix. | - |
| `dist_quiktrip_m` | `FLOAT` | Address | No | Distance in meters to the nearest Quiktrip. | - |
| `dist_restoration_hardware_m` | `FLOAT` | Address | No | Distance in meters to the nearest Restoration Hardware. | - |
| `dist_safeway_m` | `FLOAT` | Address | No | Distance in meters to the nearest Safeway. | - |
| `dist_sephora_m` | `FLOAT` | Address | No | Distance in meters to the nearest Sephora. | - |
| `dist_shake_shack_m` | `FLOAT` | Address | No | Distance in meters to the nearest Shake Shack. | - |
| `dist_sheetz_m` | `FLOAT` | Address | No | Distance in meters to the nearest Sheetz. | - |
| `dist_shell_m` | `FLOAT` | Address | No | Distance in meters to the nearest Shell. | - |
| `dist_sonic_drive_in_m` | `FLOAT` | Address | No | Distance in meters to the nearest Sonic Drive In. | - |
| `dist_soulcycle_m` | `FLOAT` | Address | No | Distance in meters to the nearest Soulcycle. | - |
| `dist_speedway_m` | `FLOAT` | Address | No | Distance in meters to the nearest Speedway. | - |
| `dist_starbucks_m` | `FLOAT` | Address | No | Distance in meters to the nearest Starbucks. | - |
| `dist_stop_shop_m` | `FLOAT` | Address | No | Distance in meters to the nearest Stop Shop. | - |
| `dist_subway_m` | `FLOAT` | Address | No | Distance in meters to the nearest Subway. | - |
| `dist_taco_bell_m` | `FLOAT` | Address | No | Distance in meters to the nearest Taco Bell. | - |
| `dist_target_m` | `FLOAT` | Address | No | Distance in meters to the nearest Target. | - |
| `dist_tesla_m` | `FLOAT` | Address | No | Distance in meters to the nearest Tesla. | - |
| `dist_tesla_supercharger_m` | `FLOAT` | Address | No | Distance in meters to the nearest Tesla Supercharger. | - |
| `dist_the_home_depot_m` | `FLOAT` | Address | No | Distance in meters to the nearest The Home Depot. | - |
| `dist_the_ups_store_m` | `FLOAT` | Address | No | Distance in meters to the nearest The Ups Store. | - |
| `dist_trader_joes_m` | `FLOAT` | Address | No | Distance in meters to the nearest Trader Joes. | - |
| `dist_ufc_gym_m` | `FLOAT` | Address | No | Distance in meters to the nearest Ufc Gym. | - |
| `dist_ulta_beauty_m` | `FLOAT` | Address | No | Distance in meters to the nearest Ulta Beauty. | - |
| `dist_us_bank_m` | `FLOAT` | Address | No | Distance in meters to the nearest Us Bank. | - |
| `dist_valvoline_instant_oil_change_m` | `FLOAT` | Address | No | Distance in meters to the nearest Valvoline Instant Oil Change. | - |
| `dist_vitamin_shoppe_m` | `FLOAT` | Address | No | Distance in meters to the nearest Vitamin Shoppe. | - |
| `dist_walgreens_m` | `FLOAT` | Address | No | Distance in meters to the nearest Walgreens. | - |
| `dist_walmart_m` | `FLOAT` | Address | No | Distance in meters to the nearest Walmart. | - |
| `dist_wawa_m` | `FLOAT` | Address | No | Distance in meters to the nearest Wawa. | - |
| `dist_wegmans_m` | `FLOAT` | Address | No | Distance in meters to the nearest Wegmans. | - |
| `dist_wells_fargo_m` | `FLOAT` | Address | No | Distance in meters to the nearest Wells Fargo. | - |
| `dist_wendys_m` | `FLOAT` | Address | No | Distance in meters to the nearest Wendys. | - |
| `dist_whole_foods_market_m` | `FLOAT` | Address | No | Distance in meters to the nearest Whole Foodsarket. | - |
| `dist_williams_sonoma_m` | `FLOAT` | Address | No | Distance in meters to the nearest Williams Sonoma. | - |

---

## Neighborhood Lifestyle
*Neighborhood personality profiling through point-of-interest density and concentration indexes across 20 lifestyle themes*

| Column Name | Type | Level | PII | Description | Value Mappings / Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `academic_enrichment_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Academic Enrichment POIs relative to national baseline | - |
| `academic_enrichment_per_1k` | `FLOAT` | Address | No | Density of Academic Enrichment POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `adventure_seeker_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Adventure Seeker POIs relative to national baseline | - |
| `adventure_seeker_per_1k` | `FLOAT` | Address | No | Density of Adventure Seeker POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `auto_dependent_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Auto Dependent POIs relative to national baseline | - |
| `auto_dependent_per_1k` | `FLOAT` | Address | No | Density of Auto Dependent POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `care_longevity_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Care Longevity POIs relative to national baseline | - |
| `care_longevity_per_1k` | `FLOAT` | Address | No | Density of Care Longevity POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `convenience_friction_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Convenience Friction POIs relative to national baseline | - |
| `convenience_friction_per_1k` | `FLOAT` | Address | No | Density of Convenience Friction POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `diy_maker_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Diy Maker POIs relative to national baseline | - |
| `diy_maker_per_1k` | `FLOAT` | Address | No | Density of Diy Maker POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `eco_innovator_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Eco Innovator POIs relative to national baseline | - |
| `eco_innovator_per_1k` | `FLOAT` | Address | No | Density of Eco Innovator POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `family_infrastructure_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Family Infrastructure POIs relative to national baseline | - |
| `family_infrastructure_per_1k` | `FLOAT` | Address | No | Density of Family Infrastructure POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `financial_lifecycle_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Financial Lifecycle POIs relative to national baseline | - |
| `financial_lifecycle_per_1k` | `FLOAT` | Address | No | Density of Financial Lifecycle POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `golf_course_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Golf Course POIs relative to national baseline | - |
| `golf_course_per_1k` | `FLOAT` | Address | No | Density of Golf Course POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `gourmet_artisan_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Gourmet Artisan POIs relative to national baseline | - |
| `gourmet_artisan_per_1k` | `FLOAT` | Address | No | Density of Gourmet Artisan POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `home_improver_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Home Improver POIs relative to national baseline | - |
| `home_improver_per_1k` | `FLOAT` | Address | No | Density of Home Improver POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `mass_market_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Mass Market POIs relative to national baseline | - |
| `mass_market_per_1k` | `FLOAT` | Address | No | Density of Mass Market POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `nightlife_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Nightlife POIs relative to national baseline | - |
| `nightlife_per_1k` | `FLOAT` | Address | No | Density of Nightlife POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `pet_parent_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Pet Parent POIs relative to national baseline | - |
| `pet_parent_per_1k` | `FLOAT` | Address | No | Density of Pet Parent POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `quiet_luxury_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Quiet Luxury POIs relative to national baseline | - |
| `quiet_luxury_per_1k` | `FLOAT` | Address | No | Density of Quiet Luxury POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `retail_saturation_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Retail Saturation POIs relative to national baseline | - |
| `retail_saturation_per_1k` | `FLOAT` | Address | No | Density of Retail Saturation POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `status_seeker_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Status Seeker POIs relative to national baseline | - |
| `status_seeker_per_1k` | `FLOAT` | Address | No | Density of Status Seeker POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `urban_vitality_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Urban Vitality POIs relative to national baseline | - |
| `urban_vitality_per_1k` | `FLOAT` | Address | No | Density of Urban Vitality POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |
| `wellness_hub_lq` | `FLOAT` | Address | No | Location quotient index measuring concentration of Wellness Hub POIs relative to national baseline | - |
| `wellness_hub_per_1k` | `FLOAT` | Address | No | Density of Wellness Hub POIs per 1,000 residents in the surrounding ~1 km² neighborhood area | - |

---
