import polars as pl
from helpers import *

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
print(sorted(pop.unique(subset='code').get_column('code')))
print(sorted(climate.unique(subset='code').get_column('code')))
print(sorted(tourists.unique(subset='code').get_column('code')))

# Check that the rows look how we expect
print(pop.glimpse(return_type='string'))
print(climate.glimpse(return_type='string'))
print(tourists.glimpse(return_type='string'))
