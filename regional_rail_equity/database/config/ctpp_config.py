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

# TODO: Minority status


# TODO: remove this one below
# race = {
#     "filepath": "EA_A101108 - Race (5) (All persons)/C13.shp",
#     "sql_tablename": "data.ctpp_race_all_people",
#     "names": [
#         "ctpp_id",
#         "label",
#         "name",
#         "geoid",
#         "est_all_races",
#         "moe_all_races",
#         "est_white_alone",
#         "moe_white_alone",
#         "est_black_alone",
#         "moe_black_alone",
#         "est_asian_alone",
#         "moe_asian_alone",
#         "est_other",
#         "moe_other",
#         "geometry",
#     ],
# }

# TODO: modify the columns for this one and add both NJ and PA tables
english = {
    "filepath": "EA_A117200 - Ability to speak English (3) by Language spoken at home (13) (Persons 5 years old and over in households)/C13.shp",
    "sql_tablename": "data.ctpp_language_at_home",
    "names": [
        "ctpp_id",
        "label",
        "name",
        "geoid",
        "est_total",
        "moe_total",
        "est_english",
        "moe_english",
        "est_spanish",
        "moe_spanish",
        "est_french_hatian_cajun",
        "moe_french_hatian_cajun",
        "est_germanic",
        "moe_germanic",
        "est_russian_slavic",
        "moe_russian_slavic",
        "est_indo_european",
        "moe_indo_european",
        "est_korean",
        "moe_korean",
        "est_chinese",
        "moe_chinese",
        "est_vietnamese",
        "moe_vietnamese",
        "est_tagalog",
        "moe_tagalog",
        "est_other_aapi",
        "moe_other_aapi",
        "est_arabic",
        "moe_arabic",
        "est_other",
        "moe_other",
        "geometry",
    ],
}


# TODO: add vehicles available table for both NJ and PA

ctpp_configurations = [
    poverty,
    english,
]
