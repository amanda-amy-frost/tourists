import polars as pl

# Use this file for prototyping in iPython and for the individual scripts themsevles

# Allow Polars to infer all datatypes
# While you could get fancy and specify a schema with fx enums or force the years
# into a date format, for the purposes of this project, it's not worth the effort
pop = pl.read_csv('../data/population-processed.csv')
climate = pl.read_csv('../data/climate-data.csv')
tourists_pivoted = pl.read_csv('../data/tourists-processed.csv')
tourists = tourists_pivoted.unpivot(index='code', variable_name='year', value_name='visitors')

COUNTRY_CODES = sorted(
    pop.unique(subset='code')
    .get_column('code')
    .to_list())
