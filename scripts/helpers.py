import polars as pl

# Use this file for prototyping in iPython and for the individual scripts themsevles

# Allow Polars to infer all datatypes
# While you could get fancy and specify a schema with fx enums or force the years
# into a date format, for the purposes of this project, it's not worth the effort
pop = pl.read_csv('../data/population-processed.csv')
climate = pl.read_csv('../data/climate-data.csv')
tourists_pivoted = pl.read_csv('../data/tourists-processed.csv')

# "Unpivot" the dataframe so that year repeats for each country code.
# This operation is more intuitive if you start with a pivoted table,
# as I originally did before realizing it was unnecessary.
tourists = tourists_pivoted.unpivot(index='code', variable_name='year', value_name='visitors')

# Constants
COUNTRY_CODES = sorted(
    pop.unique(subset='code')
    .get_column('code')
    .to_list()
)

# I chose to exclude anyone under 15, as the relevant traveling population is in
# these two age ranges, and they likely exhibit different patterns between them.
WORKING = 'Y15T64' # 15 to 64 years old
RETIRED = 'Y_GE65' # 65+ years old

# It might be more efficient to first generate the necessary dataframes when
# I need them, but for this project it makes sense to prioritize ease-of-use.
pop_working = {}
pop_retired = {}
pop_total = {}
for code in COUNTRY_CODES:
    country = pop.filter(pl.col('code') == code)
    country_working = country.filter(pl.col('demo') == WORKING).sort(pl.col('year'))
    country_retired = country.filter(pl.col('demo') == RETIRED).sort(pl.col('year'))

    # pl.over() allows us to group_by and left join the result in the same operation.
    # If we didn't have two nearly identical columns in code and country, then the
    # over() expression below would be a bit more intuitive, as the effect is summing
    # over the code and year (i.e. by code and year). It's just that there is also a
    # 1:1 mapping of code to country, which requires us to include the latter.
    country_total = (
        country.with_columns(       # Add a new column
            pl.col("demo_total")    # Based on demo_total
                .sum()              # Where you sum the rows by country/code and year
                .over(['code', 'country', 'year']) # Quirk of having two similar cols
                .alias('country_total') # And name the new column
            )
            .select(pl.exclude('demo', 'demo_total')) # Remove unnecessary columns
            .unique(subset='year')  # Remove duplicate rows
            .sort(pl.col('year'))   # Sort
    )

    pop_working[code] = country_working
    pop_retired[code] = country_retired
    pop_total[code] = country_total
