all:
	@echo REGIONAL RAIL EQUITY
	@echo --------------------
	@echo This command line tool handles the import and feature engineering of data needed for the equity analysis of model outputs

db-setup:
	python ./regional_rail_equity/database/feature_engineering/create_schemas.py
	pytest tests/test_schemas.py 

census-data:
	python ./regional_rail_equity/database/load/load_ctpp_tables.py
	python ./regional_rail_equity/database/feature_engineering/summarize_ctpp.py

spatial-data:
	python ./regional_rail_equity/database/load/load_spatial_data.py
	python ./regional_rail_equity/database/feature_engineering/clip_counties.py
	pytest tests/test_spatial_data_import.py 

model-data:
	python ./regional_rail_equity/database/load/load_trip_tables.py
	pytest tests/test_model_import.py 

data: db-setup census-data spatial-data model-data
	pytest ./tests/database

# analysis:
# 	python ./regional_rail_equity/zones/queries.py

# shapefiles:
# 	python ./regional_rail_equity/database/export.py

test-all:
	pytest .
