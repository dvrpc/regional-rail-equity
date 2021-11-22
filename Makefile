.PHONY: data
all:
	@echo REGIONAL RAIL EQUITY: options include
	@echo -------------------------------------
	@echo - data

data:
	python ./regional_rail_equity/database/load_spatial_data.py
	python ./regional_rail_equity/database/load_trip_tables.py
	python ./regional_rail_equity/database/load_ctpp_tables.py