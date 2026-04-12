import polars as pl
from init_dataframes import *

# Define a metric for determining the starting year for our analysis, as there are
# a lot of very low outliers in the first several years of visits from multiple
# countries. One quick way for this is finding the earliest year where the minimum
# number of visits is at least equal to some multiple of the STD below the mean,
# as the data can be quite variable due to the initial outliers. We don't need to
# worry about accidentally removing the COVID years, as this filter is only used
# to calculate the starting year. A couple countries (e.g. Iceland and Portugal)
# are so extreme that their starting STD is larger than the mean.
start_year = 1992
stable = False
count = 0
while not stable:
    stable = True # Assume stable until proven otherwise
    print('start_year', start_year)
    print('count', count)
    for code in COUNTRY_CODES:
        visits = pl.col('visits')
        # Polars makes it very efficient to perform queries like this,
        # as it uses lazy execution under the hood and can plan ahead
        # for operations by taking advantage of predicate and projection
        # pushdown. For the code below, that means there is very little
        # sacrifice to performance by repeating the same year calculation
        # each loop, as the number of actual lookups will be minimal.
        # So instead of having to consider whether to copy a filtered
        # df_by_country every loop and sacrifice memory for more performance
        # in future iterations, you can naively repeat the same operations
        # on the full dataframe, at least in this case.
        year = df_by_country[code].filter(
            # First filter out the years, as applying both filters
            # concurrently defeats the purpose of the second one.
            pl.col('year') >= start_year
        ).filter(
            # Use the population standard deviation as the baseline.
            # 1.2 is a "magic number" - I picked it more so that the
            # start_year would end somewhere reasonable, but a more
            # systematic and reasoned approach would likely be needed
            # under different circumstances. 2005 ends up being the
            # start_year, as the last outliers from 2004 - Iceland and
            # Portugal - both jump by an order of magnitude from 2004
            # to 2005, and after that the changes are smoother.
            visits >= (visits.mean() - (visits.std(ddof=0) * 1.2))
        ).select(
            pl.min('year')
        ).item()
        if year > start_year:
            start_year = year
            stable = False
            count += 1
            print(code)
            print(year)
            print('count:', count)
