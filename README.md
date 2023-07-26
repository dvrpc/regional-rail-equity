# regional-rail-equity

## project introduction
This project documents work that DVRPC performed for SEPTA from 2021 to 2023.

There is a Makefile which can be run, running every script in the proper order. 

Follow the steps below to run the analysis, keeping in mind that it builds a 40-50gb database.

There is a backup of the database in the project Gdrive for internal use, so DVRPC staff can also restore from there rather than rerun the entire analysis. 


## Database setup

Create a local PostgreSQL database, enable PostGIS, and clone the GitHub repository. 

## Development environment setup

Install a virutal environment with all dependencies using:

```
conda env create -f environment.yml
```

Create a `.env` file that defines `DATABASE_URL` and `GDRIVE_PROJECT_FOLDER`

## Import data

Import all necessary data and run the test suite with:

```
conda activate regional-rail-equity
make data
```

## Assign Path Legs to Park and Ride Zones

```
make parknride-estimations
```

## Generate Analysis Summary

Generates a spreadsheet with different tabs for each scenario and timeframe. Also generates a station-level ridership summary.

```
make analysis
```
