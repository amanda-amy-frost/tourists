import polars as pl
from init_dataframes import *

# Quick and dirty ways to check that everything looks as it should

# Show the dataframes themselves
print('pop')
print(pop)
print('climate')
print(climate)
print('tourists')
print(tourists)
print('tourists_pivoted')
print(tourists_pivoted)

# Make sure all the countries are there
print(COUNTRY_CODES)
assert COUNTRY_CODES == sorted(pop.unique(subset='code').get_column('code'))
assert COUNTRY_CODES == sorted(climate.unique(subset='code').get_column('code'))
assert COUNTRY_CODES == sorted(tourists.unique(subset='code').get_column('code'))

# Check that the rows look how we expect
print(pop.glimpse(return_type='string'))
print(climate.glimpse(return_type='string'))
print(tourists.glimpse(return_type='string'))

# Make sure we have all population years for all demos
for code in COUNTRY_CODES:
    for demo in [WORKING, RETIRED, TOTAL]:
        assert list(range(1992, 2025)) == sorted(
            df_by_country[code]
                .filter(pl.col('demo') == demo)
                .get_column('year')
                .to_list()
        )
    # There should be exactly 8 null entries per country
    # 4 for hot_days -> 3 missing from 2024, 1 from 2025
    # 1 each for demo, demo_total, country_total, and pop_percent
    assert df_by_country[code].null_count().sum_horizontal().item() == 8

# Check one of the country's dataframes
with pl.Config(tbl_rows=100, tbl_cols=9):
    print(df_by_country['AUT'])
