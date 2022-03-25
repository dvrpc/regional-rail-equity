# regional-rail-equity

Import CTPP and regional travel demand model data into a PostgreSQL database to support an equity-oriented analysis of a variety of model scenarios.

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
