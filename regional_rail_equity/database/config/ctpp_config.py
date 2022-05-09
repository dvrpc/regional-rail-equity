poverty = {
    "filepath": "EA_A113100 - Poverty status (4) (Households for which poverty status is determined)/C13.shp",
    "sql_tablename": "data.ctpp_poverty_by_household",
    "names": [
        "ctpp_id",
        "label",
        "name",
        "geoid",
        "est_total_poverty_status",
        "moe_total_poverty_status",
        "est_below_100pct_poverty_status",
        "moe_below_100pct_poverty_status",
        "est_100_to_149pct_poverty_status",
        "moe_100_to_149pct_poverty_status",
        "est_at_or_above_150pct_poverty_status",
        "moe_at_or_above_150pct_poverty_status",
        "geometry",
    ],
}

minority = {
    "filepath": "EA_A101105 - Minority Status (3) (All Persons)/C13.shp",
    "sql_tablename": "data.ctpp_minority_by_person",
    "names": [
        "ctpp_id",
        "label",
        "name",
        "geoid",
        "est_total_persons",
        "moe_total_persons",
        "est_white_alone_non_hispanic",
        "moe_white_alone_non_hispanic",
        "est_other",
        "moe_other",
        "geometry",
    ],
}
english_column_names = [
    "ctpp_id",
    "label",
    "name",
    "geoid",
    "est_total_persons",
    "est_english_speakers_five_over",
    "geometry",
]

english_nj = {
    "filepath": "NJ - EA_A117200 - Ability to speak English (3) by Language spoken at home (13) (Persons 5 years old and over in households)/C13.shp",
    "sql_tablename": "data.nj_language_at_home",
    "names": english_column_names,
}

english_pa = {
    "filepath": "PA - EA_A117200 - Ability to speak English (3) by Language spoken at home (13) (Persons 5 years old and over in households)/C13.shp",
    "sql_tablename": "data.pa_language_at_home",
    "names": english_column_names,
}

vehicles_available_column_names = [
    "ctpp_id",
    "label",
    "name",
    "geoid",
    "est_total_vehicles_available",
    "moe_total_vehicles_available",
    "est_zero_vehicles_available",
    "moe_zero_vehicles_available",
    "est_one_vehicles_available",
    "moe_one_vehicles_available",
    "est_two_vehicles_available",
    "moe_two_vehicles_available",
    "est_three_vehicles_available",
    "moe_three_vehicles_available",
    "est_four_plus_vehicles_available",
    "moe_four_plus_vehicles_available",
    "geometry",
]

vehicles_available_nj = {
    "filepath": "NJ - EA_A104201 - Vehicles available (6) by Poverty status (4) (Workers 16 years and over in households for whom poverty status is determined)/C13.shp",
    "sql_tablename": "data.nj_vehicles_available",
    "names": vehicles_available_column_names,
}

vehicles_available_pa = {
    "filepath": "PA - EA_A104201 - Vehicles available (6) by Poverty status (4) (Workers 16 years and over in households for whom poverty status is determined)/C13.shp",
    "sql_tablename": "data.pa_vehicles_available",
    "names": vehicles_available_column_names,
}

ctpp_configurations = [
    poverty,
    minority,
    english_nj,
    english_pa,
    vehicles_available_nj,
    vehicles_available_pa,
]
