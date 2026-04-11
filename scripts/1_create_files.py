import polars as pl
import requests
import json
import csv

POPULATION_COLS = {
    'REF_AREA': 'code',
    'Reference area': 'country',
    'AGE': 'demo', # Short for "demographic"
    'TIME_PERIOD': 'year',
    'OBS_VALUE': 'demo_total',
}

pop = pl.read_csv(
    source='../data/population-raw.csv',
    columns=list(POPULATION_COLS.keys()),
    schema_overrides={'OBS_VALUE': pl.Float64}, # Avoid parsing errors
)
pop = pop.rename(POPULATION_COLS)

# In the rows for Portugal, the population numbers have a few non-whole number entries.
# By default, Polars will try to infer a column's datatype based on the first 100 rows.
# As Polars cannot retroactively cast integers to floating points when reading in data,
# the easiest fix is to override the schema for the affected column, as it would have
# to be a float anyway to read in the data as-is. After reading in the data, force cast
# the column to integers.
#
# The reason for doing this fix programmatically rather than manually editing the raw file
# is to reduce the chance of errors due to the inherent unreliability and unrepeatability
# of editing things in that way. It also wouldn't scale if the problem affected more rows.
fixed_demo_count = pl.Series(
    'demo_total',
    pop.select(pl.col('demo_total').cast(pl.Int64)),
)
pop.replace_column(pop.get_column_index('demo_total'), fixed_demo_count)
pop.write_csv('../data/population-processed.csv')

# I used these codes to manually edit tourists-processed.csv
COUNTRY_CODES = sorted(
    pop.unique(subset='code')
    .get_column('code')
    .to_list()
)

# The dataset ends in 2023
# The year consistently uses July ('-07') as its reference point throughout
YYYY_MM = [(str(year) + '-07') for year in range(1992, 2024)]
# Specify newline to avoid empty lines when writing to the file
with open('../data/climate-data.csv', 'w', newline='\n') as f:
    w = csv.writer(f)
    w.writerow(['code', 'year', 'hot_days'])
    for code in COUNTRY_CODES:
        # The API request encodes the exact data to extract,
        # with only the country code needing to be modified.
        climate_link = f'https://cckpapi.worldbank.org/api/v1/era5-x0.25_timeseries_hd30_timeseries_annual_1950-2023_mean_historical_era5_x0.25_mean/{code}?_format=json'

        json_data = json.loads(requests.get(climate_link).text)
        extract = {
            year: hot_days for year, hot_days
            in json_data['data'][code].items()
            if year in YYYY_MM
        }
        # Truncate the year back to just a YYYY format
        extract_with_code = [
            (code, year[:4], hot_days) for year, hot_days in extract.items()
        ]
        w.writerows(extract_with_code)
