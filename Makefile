all:
	@echo REGIONAL RAIL EQUITY
	@echo --------------------
	@echo This command line tool handles the import and feature engineering of data needed for the equity analysis of model outputs

db-setup:
	python ./regional_rail_equity/database/feature_engineering/create_schemas.py
	pytest tests/test_schemas.py -W ignore::DeprecationWarning

census-data:
	python ./regional_rail_equity/database/load/load_ctpp_tables.py
	python ./regional_rail_equity/database/feature_engineering/summarize_ctpp.py
	pytest tests/test_ctpp.py -W ignore::DeprecationWarning

spatial-data:
	python ./regional_rail_equity/database/load/load_spatial_data.py
	python ./regional_rail_equity/database/feature_engineering/clip_counties.py
	pytest tests/test_spatial_data_import.py -W ignore::DeprecationWarning

model-data:
	python ./regional_rail_equity/database/load/load_trip_tables.py
	pytest tests/test_model_import.py -W ignore::DeprecationWarning

station-data:
	python ./regional_rail_equity/database/load/load_station_summary_tables.py
	pytest tests/test_station_data.py -W ignore::DeprecationWarning

parknride-estimations:
	python ./regional_rail_equity/database/feature_engineering/assign_park_and_ride_origins_to_pathlegs.py
	python ./regional_rail_equity/database/feature_engineering/merge_parknride_assignment_to_pathlegs.py

data: db-setup census-data spatial-data model-data
	pytest ./tests/database

analysis:
	python ./regional_rail_equity/analysis/summarize_trip_origins.py
	python ./regional_rail_equity/analysis/summarize_demographic_trends.py
	python ./regional_rail_equity/analysis/summarize_stations_tod.py

test-all:
	pytest .
