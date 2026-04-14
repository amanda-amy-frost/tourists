import polars as pl
from init_dataframes import *

# Constants
# TODO better name for big hitters
BIG_HITTERS = ['DEU', 'NLD']
WEST_EU     = ['AUT', 'BEL', 'CHE', 'FRA', 'GBR', 'IRL']
NORDICS     = ['FIN', 'ISL', 'NOR', 'SWE']
SOUTH_EU    = ['ESP', 'ITA', 'PRT']
NOR_AMER    = ['CAN', 'USA']

REGIONS = {
    'big_hitters': BIG_HITTERS,
    'west_eu': WEST_EU,
    'nordics': NORDICS,
    'south_eu': SOUTH_EU,
    'nor_amer': NOR_AMER
}

# We only need this list to concat all the dataframes together,
# so there's no need for a dict like I have been using.
_scaled_by_pop = []
for iso_code in COUNTRY_ISO_CODES:
    country = (
        monster_df[iso_code]
            .filter(pl.col('demo') == TOTAL)
            .select(
                # Keep the country names so we can use them in graphs and plots
                pl.col('iso_code', 'year', 'country'),
                scaled=((pl.col('visits') / pl.col('demo_total')) * 100).round(4))
    )
    _scaled_by_pop.append(country)

# In order to render the years properly in Altair, we need them as strings
scaled_df = (
    pl.concat(_scaled_by_pop)
        .with_columns(pl.col('year').cast(pl.String).name.prefix('str_'))
)

regions_df = {}
for region in REGIONS.keys():
    regions_df[region] = scaled_df.filter(pl.col('iso_code').is_in(REGIONS[region]))
