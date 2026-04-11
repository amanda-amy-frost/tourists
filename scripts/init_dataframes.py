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
# We need to force cast the year to an int after pivoting to allow for joins
int_year = pl.Series('year', tourists.select(pl.col('year').cast(pl.Int64)))
tourists.replace_column(tourists.get_column_index('year'), int_year)

# Constants
COUNTRY_CODES = sorted(
    pop.unique(subset='code')
    .get_column('code')
    .to_list()
)
# I chose to exclude anyone under 15, as the relevant traveling population is in
# these two age ranges, and they likely exhibit different patterns between them.
# The total population is still needed to compare against however, as only knowing
# the working and retired populations doesn't account for the younger generations
# that will replace the people who age out.
WORKING = 'Y15T64'  # 15 to 64 years old
RETIRED = 'Y_GE65'  # 65+ years old
TOTAL = '_T'        # Total population, including those under 15

# Use explicit type hint for code completion
df_by_country: dict[str, pl.DataFrame] = {}

for code in COUNTRY_CODES:
    # Get a scalar of the total population, rather than a series
    pop_total_expr = pl.col('demo_total').filter(pl.col('demo') == TOTAL).first()

    # pl.over() allows us to group by and left join the result in the same operation.
    # The call to pl.over() below expands (broadcasts) pop_total_expr to fill the rows
    # for that particular country code and year. E.g. AUT 1992 will have 3 identical
    # entries for country_total, once each for the WORKING, RETIRED, and TOTAL demos.
    pop_with_stats = (
        pop.filter(pl.col('code') == code)
            .with_columns(
                pop_total_expr
                    .over(['code', 'year'])
                    .alias('country_total')
            ).with_columns( # Need a second call, as country_total must first exist
                (pl.col('demo_total') / pl.col('country_total') * 100)
                    .round(2)
                    .alias('pop_percent')
            ).sort(pl.col('year'))
    )

    full_df = (
        tourists.filter(pl.col('code') == code)
            .join(climate.filter(pl.col('code') == code), on=['code', 'year'], how='left')
            .join(pop_with_stats, on=['code', 'year'], how='left', validate='1:m')
    )
    fixed_countries = pl.Series(
        'country',
        full_df.select(pl.col('country').fill_null(strategy='forward'))
    )
    full_df.replace_column(full_df.get_column_index('country'), fixed_countries)
    df_by_country[code] = full_df
