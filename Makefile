.PHONY: data analysis shapefiles test-all
all:
	@echo REGIONAL RAIL EQUITY: options include
	@echo -------------------------------------
	@echo - data
	@echo - analysis
	@echo - shapefiles
	@echo - test-all

data:
	python ./regional_rail_equity/database/load/load_spatial_data.py
	python ./regional_rail_equity/database/load/load_trip_tables.py
	python ./regional_rail_equity/database/load/load_ctpp_tables.py
	python ./regional_rail_equity/database/load/feature_engineering.py
	pytest ./tests/database

analysis:
	python ./regional_rail_equity/zones/queries.py

shapefiles:
	python ./regional_rail_equity/database/export.py

test-all:
	pytest .