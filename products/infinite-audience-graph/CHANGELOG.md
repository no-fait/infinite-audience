# Changelog — Infinite Audience Graph

All notable releases, schema evolutions, and coverage changes for the Infinite Audience Graph are documented here.

## [Infinite Audience Graph v1.2.2.0] - September 22, 2026

**Release Tag:** `iag-v1.2.2.0` | **Vintage:** September 2026

### 📊 Coverage & Scale
- **Resolved Individuals:** **215,677,380** *(-1,141,921 / -0.5%)*
- **Household Clusters:** **129,208,600** *(+3,254,771 / +2.6%)*
- **Physical Delivery Addresses:** **110,704,326** *(-404,692 / -0.4%)*
- **Building Footprints:** **92,811,629** *(-252,301 / -0.3%)*
- **Linkage Identifiers (Email, Phone, Address):** **1,053,066,095** *(-8,541,696 / -0.8%)*

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

### 🔄 Modified Attributes (472)
- `emails` (*Identity*): type: `ARRAY<RECORD>` -> `ARRAY<STRUCT<priority INT64, match_level STRING, confidence_score FLOAT64, email STRING, email_domain_type STRING>>`, updated description
- `phones` (*Identity*): type: `ARRAY<RECORD>` -> `ARRAY<STRUCT<priority INT64, match_level STRING, confidence_score FLOAT64, phone STRING, phone_type STRING>>`, updated description
- `age` (*Demographics & Household*): type: `INTEGER` -> `INT64`
- `household_size` (*Demographics & Household*): type: `NUMERIC` -> `INT64`, updated description
- `has_children` (*Demographics & Household*): type: `STRING` -> `BOOL`, updated description
- `home_has_pool` (*Financial & Property*): type: `STRING` -> `BOOL`, updated description
- `political_outlook_score` (*Media & Behavioral*): type: `INTEGER` -> `INT64`
- `tech_attitude_score` (*Media & Behavioral*): type: `INTEGER` -> `INT64`
- `nchs_urban_rural_code` (*Geography*): type: `INTEGER` -> `INT64`
- `primary_ruca_code` (*Geography*): type: `INTEGER` -> `INT64`
- `flag_lives_on_military_base` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_on_reservation` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_on_college_campus` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_off_college_campus` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_on_farmland` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_on_waterfront` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_adjacent_to_park` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_in_commercial_zone` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_on_golf_course` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_on_medical_campus` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_in_industrial_zone` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_adjacent_to_industrial` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_adjacent_to_stadium` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `flag_lives_adjacent_to_mall` (*Land Context*): type: `BOOLEAN` -> `BOOL`
- `dist_commercial_airport_m` (*Land Context*): type: `FLOAT` -> `FLOAT64`
- `dist_convention_center_m` (*Land Context*): type: `FLOAT` -> `FLOAT64`
- `dist_military_base_m` (*Land Context*): type: `FLOAT` -> `FLOAT64`
- `dist_national_park_m` (*Land Context*): type: `FLOAT` -> `FLOAT64`
- `dist_ski_resort_m` (*Land Context*): type: `FLOAT` -> `FLOAT64`
- `dist_stadium_m` (*Land Context*): type: `FLOAT` -> `FLOAT64`
- `dist_subway_station_m` (*Land Context*): type: `FLOAT` -> `FLOAT64`
- `acs_aggregate_travel_time_to_work` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_amerindian_including_hispanic_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_amerindian_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_armed_forces_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_asian_including_hispanic_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_asian_male_45_54_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_asian_male_55_64_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_asian_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_associates_degree_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_bachelors_degree_2_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_bachelors_degree_or_higher_25_64_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_bachelors_degree_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_black_including_hispanic_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_black_male_45_54_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_black_male_55_64_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_black_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_children_in_single_female_hh_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_children_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_civilian_labor_force_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_10_14_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_15_19_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_20_24_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_25_29_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_30_34_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_35_39_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_35_44_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_40_44_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_45_59_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_5_9_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_60_89_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_60_more_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_90_more_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commute_less_10_mins_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commuters_16_over` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commuters_by_bus_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commuters_by_car_truck_van_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commuters_by_carpool_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commuters_by_public_transportation_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commuters_by_subway_or_elevated_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_commuters_drove_alone_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_different_house_year_ago_different_city_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_different_house_year_ago_same_city_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_dwellings_10_to_19_units_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_dwellings_1_units_attached_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_dwellings_1_units_detached_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_dwellings_20_to_49_units_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_dwellings_2_units_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_dwellings_3_to_4_units_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_dwellings_50_or_more_units_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_dwellings_5_to_9_units_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_agriculture_forestry_fishing_hunting_mining_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_arts_entertainment_recreation_accommodation_food_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_construction_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_education_health_social_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_finance_insurance_real_estate_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_information_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_manufacturing_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_other_services_not_public_admin_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_public_administration_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_retail_trade_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_science_management_admin_waste_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_transportation_warehousing_utilities_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_employed_wholesale_trade_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_families_with_young_children` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_family_households` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_father_in_labor_force_one_parent_families_with_young_children_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_father_one_parent_families_with_young_children_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_10_to_14_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_15_to_17_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_18_to_19_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_20_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_21_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_22_to_24_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_25_to_29_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_30_to_34_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_35_to_39_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_40_to_44_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_45_to_49_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_50_to_54_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_55_to_59_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_5_to_9_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_60_to_61_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_62_to_64_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_65_to_66_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_67_to_69_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_70_to_74_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_75_to_79_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_80_to_84_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_85_and_over_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_female_households_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_female_under_5_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_four_more_cars_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_gini_index` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_graduate_professional_degree_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_group_quarters_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_high_school_diploma_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_high_school_including_ged_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_hispanic_any_race_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_hispanic_male_45_54_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_hispanic_male_55_64_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_hispanic_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_households` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_households_public_asst_or_food_stamps_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_households_retirement_income_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_housing_built_1939_or_earlier_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_housing_built_2000_to_2004_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_housing_built_2005_or_later_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_housing_units` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_housing_units_renter_occupied_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_in_grades_1_to_4_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_in_grades_5_to_8_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_in_grades_9_to_12_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_in_school_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_in_undergrad_college_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_100000_124999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_10000_14999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_125000_149999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_150000_199999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_15000_19999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_200000_or_more_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_20000_24999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_25000_29999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_30000_34999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_35000_39999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_40000_44999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_45000_49999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_50000_59999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_60000_74999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_75000_99999_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_less_10000_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_income_per_capita` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_less_one_year_college_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_less_than_high_school_graduate_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_10_to_14_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_15_to_17_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_18_to_19_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_20_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_21_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_22_to_24_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_25_to_29_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_30_to_34_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_35_to_39_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_40_to_44_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_45_64_associates_degree_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_45_64_bachelors_degree_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_45_64_grade_9_12_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_45_64_graduate_degree_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_45_64_high_school_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_45_64_less_than_9_grade_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_45_64_some_college_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_45_to_49_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_45_to_64` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_50_to_54_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_55_to_59_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_5_to_9_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_60_to_61_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_62_to_64_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_65_to_66_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_67_to_69_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_70_to_74_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_75_to_79_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_80_to_84_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_85_and_over_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_male_households_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_male_under_5_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_management_business_sci_arts_employed_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_married_households_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_masters_degree_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_median_age` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_median_income` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_median_rent` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_median_year_structure_built` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_million_dollar_housing_units_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_mobile_homes_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_mortgaged_housing_units_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_no_car_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_no_cars_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_nonfamily_households` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_not_hispanic_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_not_in_labor_force_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_not_us_citizen_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_occupation_management_arts_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_occupation_natural_resources_construction_maintenance_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_occupation_production_transportation_material_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_occupation_sales_office_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_occupation_services_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_occupied_housing_units` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_one_car_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_one_parent_families_with_young_children_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_one_year_more_college_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_other_race_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_owner_occupied_housing_units_lower_value_quartile` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_owner_occupied_housing_units_median_value` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_owner_occupied_housing_units_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_owner_occupied_housing_units_upper_value_quartile` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_percent_income_spent_on_rent` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_pop_16_over` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_pop_25_64` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_pop_25_years_over` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_pop_5_years_over` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_pop_determined_poverty_status` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_pop_in_labor_force` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_population_1_year_and_over` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_population_3_years_over` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_poverty_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_rent_10_to_15_percent_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_rent_15_to_20_percent_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_rent_20_to_25_percent_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_rent_25_to_30_percent_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_rent_30_to_35_percent_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_rent_35_to_40_percent_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_rent_40_to_50_percent_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_rent_burden_not_computed_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_rent_over_50_percent_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_rent_under_10_percent_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_renter_occupied_housing_units_paying_cash_median_gross_rent` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_sales_office_employed_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_some_college_and_associates_degree_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_speak_only_english_at_home_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_speak_spanish_at_home_low_english_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_speak_spanish_at_home_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_three_cars_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_total_pop` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_two_cars_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_two_or_more_races_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_two_parent_families_with_young_children_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_two_parents_father_in_labor_force_families_with_young_children_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_two_parents_in_labor_force_families_with_young_children_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_two_parents_mother_in_labor_force_families_with_young_children_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_two_parents_not_in_labor_force_families_with_young_children_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_unemployed_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_vacant_housing_units_for_rent_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_vacant_housing_units_for_sale_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_vacant_housing_units_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_walked_to_work_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_white_including_hispanic_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_white_male_45_54_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_white_male_55_64_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_white_pop_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_worked_at_home_rate` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `acs_workers_16_and_over` (*Census Demographics & Socioeconomic*): type: `FLOAT` -> `FLOAT64`
- `cdc_access2_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_arthritis_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_binge_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_bphigh_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_bpmed_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_cancer_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_casthma_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_chd_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_checkup_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_cholscreen_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_cognition_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_colon_screen_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_copd_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_csmoking_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_dental_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_depression_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_diabetes_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_disability_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_emotionspt_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_foodinsecu_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_foodstamp_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_ghlth_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_hearing_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_highchol_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_housinsecu_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_indeplive_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_lacktrpt_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_loneliness_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_lpa_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_mammouse_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_mhlth_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_mobility_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_obesity_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_phlth_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_selfcare_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_shututility_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_sleep_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_stroke_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_teethlost_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `cdc_vision_crudeprev` (*Health*): type: `FLOAT` -> `FLOAT64`
- `doe_avg_annual_energy_cost` (*Environment & Risk*): type: `FLOAT` -> `FLOAT64`
- `doe_avg_household_income` (*Environment & Risk*): type: `FLOAT` -> `FLOAT64`
- `doe_energy_burden` (*Environment & Risk*): type: `FLOAT` -> `FLOAT64`
- `fema_eal_score` (*Environment & Risk*): type: `FLOAT` -> `FLOAT64`
- `fema_resl_score` (*Environment & Risk*): type: `FLOAT` -> `FLOAT64`
- `fema_risk_index` (*Environment & Risk*): type: `FLOAT` -> `FLOAT64`
- `fema_sovi_score` (*Environment & Risk*): type: `FLOAT` -> `FLOAT64`
- `bls_employed` (*Economic Indicators*): type: `INTEGER` -> `INT64`
- `bls_labor_force` (*Economic Indicators*): type: `INTEGER` -> `INT64`
- `bls_unemployed` (*Economic Indicators*): type: `INTEGER` -> `INT64`
- `bls_unemployment_rate` (*Economic Indicators*): type: `FLOAT` -> `FLOAT64`
- `fbi_property_crime_rate` (*Economic Indicators*): type: `FLOAT` -> `FLOAT64`
- `fbi_violent_crime_rate` (*Economic Indicators*): type: `FLOAT` -> `FLOAT64`
- `fhfa_hpi2000` (*Economic Indicators*): type: `FLOAT` -> `FLOAT64`
- `fhfa_hpi_annual_change` (*Economic Indicators*): type: `FLOAT` -> `FLOAT64`
- `fhfa_hpi_year` (*Economic Indicators*): type: `INTEGER` -> `INT64`
- `irs_avg_agi_per_return` (*Economic Indicators*): type: `FLOAT` -> `FLOAT64`
- `irs_total_agi_thousands` (*Economic Indicators*): type: `FLOAT` -> `FLOAT64`
- `irs_total_returns` (*Economic Indicators*): type: `INTEGER` -> `INT64`
- `dist_24_hour_fitness_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_7_eleven_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_advance_auto_parts_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_aldi_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_anytime_fitness_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_apple_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_audi_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_autozone_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_bank_of_america_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_bjs_wholesale_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_bmw_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_bp_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_burger_king_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_capital_one_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_caseys_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_chase_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_chevron_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_chick_fil_a_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_chipotle_mexican_grill_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_citibank_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_costco_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_crate_barrel_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_crunch_fitness_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_culvers_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_cvs_pharmacy_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_dairy_queen_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_dollar_general_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_dollar_tree_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_dominos_pizza_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_dunkin_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_equinox_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_exxon_mobil_stations_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_family_dollar_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_fedex_office_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_five_guys_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_gnc_live_well_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_golds_gym_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_h_e_b_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_harris_teeter_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_in_n_out_burger_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_jiffy_lube_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_kfc_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_kroger_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_la_fitness_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_lexus_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_little_caesars_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_lowes_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_lululemon_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_mcdonalds_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_meijer_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_menards_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_mercedes_benz_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_nordstrom_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_orangetheory_fitness_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_oreilly_auto_parts_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_panera_bread_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_papa_johns_pizza_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_peloton_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_pizza_hut_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_planet_fitness_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_pnc_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_popeyes_louisiana_kitchen_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_porsche_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_public_storage_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_publix_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_quiktrip_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_restoration_hardware_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_safeway_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_sephora_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_shake_shack_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_sheetz_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_shell_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_sonic_drive_in_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_soulcycle_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_speedway_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_starbucks_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_stop_shop_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_subway_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_taco_bell_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_target_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_tesla_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_tesla_supercharger_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_the_home_depot_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_the_ups_store_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_trader_joes_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_ufc_gym_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_ulta_beauty_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_us_bank_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_valvoline_instant_oil_change_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_vitamin_shoppe_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_walgreens_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_walmart_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_wawa_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_wegmans_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_wells_fargo_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_wendys_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_whole_foods_market_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `dist_williams_sonoma_m` (*Brand Proximity*): type: `FLOAT` -> `FLOAT64`
- `academic_enrichment_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `academic_enrichment_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `adventure_seeker_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `adventure_seeker_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `auto_dependent_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `auto_dependent_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `care_longevity_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `care_longevity_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `convenience_friction_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `convenience_friction_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `diy_maker_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `diy_maker_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `eco_innovator_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `eco_innovator_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `family_infrastructure_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `family_infrastructure_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `financial_lifecycle_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `financial_lifecycle_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `golf_course_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `golf_course_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `gourmet_artisan_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `gourmet_artisan_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `home_improver_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `home_improver_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `mass_market_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `mass_market_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `nightlife_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `nightlife_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `pet_parent_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `pet_parent_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `quiet_luxury_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `quiet_luxury_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `retail_saturation_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `retail_saturation_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `status_seeker_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `status_seeker_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `urban_vitality_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `urban_vitality_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `wellness_hub_lq` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`
- `wellness_hub_per_1k` (*Neighborhood Lifestyle*): type: `FLOAT` -> `FLOAT64`

### 🎯 Highlights
# Infinite Audience Graph — Release v1.2.2.0 (September 2026)

**Release Tag:** `iag-v1.2.2.0` / `v1.2.2.0`  
**Schema Version:** `1.2.2.0` (`schema_major=1`, `schema_minor=2`, `refresh_major=2`, `refresh_minor=0`)  
**Data Vintage:** September 2026  
**Release Date:** September 22, 2026  

---

## 🌟 Executive Summary

**Infinite Audience Graph v1.2.2.0** represents a major quarterly data warehouse release delivering significant expansions to local municipal geography, contact point intelligence, demographic modeling, and federal environmental attributes. 

This release rematerializes nationwide addresses to strict **USPS Publication 28 standardizations**, introduces **unit-gated household clustering** (capped at $\le 8$ members), establishes **symmetrical contact point STRUCT arrays** (`phones`, `emails`) with verification scores and priority ranking, and enriches every consumer record with authoritative **EPA Smart Location walkability**, **USDA food environment**, and **HUD fair market rents**.

---

## 📊 Verified Graph Scale & Topology

All metrics are physically verified from production `marts.iag` and identity registry tables:

| Entity Dimension | Total Verified Count | Description |
| :--- | :---: | :--- |
| **Resolved Individuals** | **215,677,380** | Active, non-churned adult consumer profiles |
| **Household Clusters** | **129,208,600** | Unit-gated residential household clusters ($\le 8$ members) |
| **Physical Delivery Addresses** | **110,704,326** | USPS Publication 28 standardized rooftop delivery points |
| **Building Footprints** | **92,811,629** | Unique physical parcels and building structures |
| **Graph Node Identifiers** | **1,053,066,095** | Traversable identity touchpoints (emails, phones, addresses) |

---

## 🚀 What's New in v1.2.2.0

### 1. Municipal Geography & Minor Civil Divisions (MCDs)
- **Township & Municipal Resolution**: Added `county_subdivision_name` to core geography, enabling sub-county targeting across 35,629 Minor Civil Divisions (MCDs), towns, and incorporated municipalities from US Census TIGER 2026 ([IAG-7](https://linear.app/no-fait/issue/IAG-7)).
- **Sub-County Granularity**: Marketers can now target local government jurisdictions, New England towns, and Midwestern townships with legal administrative boundaries.

### 2. Behavioral & Lifestyle Profiles
- **Gamer Profile Restored**: Re-introduced the `is_gamer` boolean attribute within the Media & Behavioral category, identifying active video game and interactive media enthusiasts ([IAG-12](https://linear.app/no-fait/issue/IAG-12)).
- **Streaming Subscription Audit**: Sanitized subscription video-on-demand arrays to reflect verified source attributes ([IAG-11](https://linear.app/no-fait/issue/IAG-11)).

### 3. Contact Point Intelligence & Ranked Priority
- **Harmonized Contact STRUCTs**: Standardized `phones` and `emails` contact point arrays to symmetrical STRUCT schemas (`value`, `type`, `primary`, `active`, `verification_status`, `score`, `email_domain_type`) ([IAG-38](https://linear.app/no-fait/issue/IAG-38)).
- **Email Domain Classification**: Enriched emails with `email_domain_type` classification (`government`, `education`, `military`, `corporate`, `personal`) via deterministic rule engine ([IAG-2](https://linear.app/no-fait/issue/IAG-2)).
- **Dynamic Priority & Confidence Ranking**: Applied confidence scoring and dynamic priority ordering so primary reachability points appear first in candidate arrays ([IAG-4](https://linear.app/no-fait/issue/IAG-4), [IAG-6](https://linear.app/no-fait/issue/IAG-6)).

### 4. Environmental, Housing & Walkability Insights
- **EPA Smart Location & Mobility**: Integrated the EPA Smart Location Database into neighborhood metrics, featuring `epa_walkability_index`, `epa_transit_frequency`, `epa_street_intersection_density`, and auto-ownership distributions ([IAG-27](https://linear.app/no-fait/issue/IAG-27)).
- **USDA Food Environment & Community**: Added grocery store density, convenience store density, recreation facility density, and SNAP participation rates.
- **HUD Fair Market Rents**: Integrated Section 8 50th percentile Fair Market Rents across Studio, 1-Bed, 2-Bed, 3-Bed, and 4-Bed units for local rental affordability modeling.
- **Wildfire Risk**: Enriched with national and state wildfire hazard risk percentiles (`wildfire_risk_national_rank`, `wildfire_risk_state_rank`).

---

## 🛠️ Graph & Platform Improvements

- **USPS Publication 28 Address Parity**: Executed full warehouse address re-standardization enforcing USPS Pub 28 rules across street suffixes, directionals, and secondary unit designators. Excluded Puerto Rico (`state = 'PR'`) to focus on 50 states + DC ([IAG-19](https://linear.app/no-fait/issue/IAG-19), [IAG-3](https://linear.app/no-fait/issue/IAG-3)).
- **Unit-Gated Household Clustering**: Remediated commercial drop-point overclustering by gating household grouping on secondary unit numbers (`unit_norm`) and capping household clusters at 8 members ([IAG-39](https://linear.app/no-fait/issue/IAG-39)).
- **Dynamic Active Universe Booleans**: Implemented dynamic lifecycle flags (`active`, `delete`) in `iag_core`, completely nullifying personal attributes for churned vendor records while preserving anonymous linkage lookup shells ([IAG-36](https://linear.app/no-fait/issue/IAG-36)).
- **Child Attribute Harmonization**: Harmonized child count, age bracket ranges, and presence flags across consumer profiles, converting boolean vendor fields to native SQL booleans ([IAG-16](https://linear.app/no-fait/issue/IAG-16), [IAG-17](https://linear.app/no-fait/issue/IAG-17)).
- **Spatial Partition Alignment**: Standardized `state_fips_int` range partitioning across spatial and census support tables (`RANGE_BUCKET(state_fips_int, GENERATE_ARRAY(0, 80, 1))`) and enforced join equality for Dynamic Partition Pruning ([IAG-28](https://linear.app/no-fait/issue/IAG-28)).
- **Redundant Federal Column Deprecation**: Dropped 14 physical RUCA and NCHS descriptor columns from physical schemas in favor of catalog-backed enum codebooks ([IAG-22](https://linear.app/no-fait/issue/IAG-22)).
- **Anchor Brand Proximity**: Expanded commercial airport and anchor brand aliases for nationwide spatial proximity matching ([IAG-8](https://linear.app/no-fait/issue/IAG-8)).

---

## 🛡️ Data Quality & Outlier Sanitization

- **Geocoding Sanitization**: Constrained building number regex parsing and sanitized malformed Overture postcodes to eliminate negative and out-of-range postcodes ([IAG-9](https://linear.app/no-fait/issue/IAG-9), [IAG-41](https://linear.app/no-fait/issue/IAG-41), [IAG-43](https://linear.app/no-fait/issue/IAG-43)).
- **Census Rate Denominators**: Corrected ACS labor-force participation and vehicle ownership rate denominators to prevent sentinel division-by-zero or values $>1.0$ ([IAG-42](https://linear.app/no-fait/issue/IAG-42), [IAG-43](https://linear.app/no-fait/issue/IAG-43)).
- **FEMA NRI & DOE LEAD Outliers**: Sanitized FEMA National Risk Index sentinels (`-9999`) and DOE LEAD energy-burden ratio outliers ([IAG-10](https://linear.app/no-fait/issue/IAG-10), [IAG-13](https://linear.app/no-fait/issue/IAG-13)).
- **Downstream Views Validation**: Verified zero-breaking changes across all dependent marketplace views (`marts.iag_preview_100k`, `marts.iag_sample_1pct`, `marts.iag_geo_summary`) ([IAG-40](https://linear.app/no-fait/issue/IAG-40)).

---

## 🏛️ Authoritative Data Provenance

| Domain / Category | Authoritative Primary Source | Vintage / Benchmark |
| :--- | :--- | :--- |
| **Consumer Identity & Linkage** | Multi-Vendor Identity Consortia | `2026-09-17` |
| **Rooftop & Parcel Geocoding** | Overture Maps Foundation | `2026-08` Snapshot |
| **Census Demographics & Socioeconomics** | US Census Bureau ACS 5-Year Estimates | `2022` 5-Year Vintage |
| **Municipal Boundaries & MCDs** | US Census Bureau TIGER/Line | `2026` Vintage |
| **Smart Location & Walkability** | US Environmental Protection Agency (EPA) | SLD `2021` |
| **Food Environment Atlas** | USDA Economic Research Service | `2020` / `2023` |
| **Fair Market Rents** | US Dept. of Housing & Urban Development (HUD) | `FY 2026` 50th Percentile |
| **Broadband & Connectivity** | Federal Communications Commission (FCC) | National Broadband Map `2026` |

---
*Maintained by **Finn** (<finn@infiniteaudience.ai>) • Infinite Audience*

---

## [Infinite Audience Graph v1.0.1.0] - August 31, 2026

**Release Tag:** `iag-v1.0.1.0` | **Vintage:** August 2026

### 🚀 Product Release Baseline
- **Active Schema**: 525 customer-facing attributes across 12 core categories.
- **National Linkage Graph**: Complete nation-wide US consumer graph connecting individual, household, and property insights.

---
*Maintained by **Finn** (<finn@infiniteaudience.ai>) • Infinite Audience*
