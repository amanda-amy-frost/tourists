import polars as pl
from init_dataframes import *

# Constants
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

scaled_by_pop = []
for code in COUNTRY_CODES:
    country = (
        monster_df[code]
            .filter(pl.col('demo') == TOTAL)
            .select(
                pl.col('code', 'year', 'country'),
                scaled=((pl.col('visits') / pl.col('demo_total')) * 100).round(4))
    )
    scaled_by_pop.append(country)

scaled_df = (
    pl.concat(scaled_by_pop)
        .with_columns(pl.col('year').cast(pl.String).name.prefix('str_'))
)

regions_df = {}
for region in REGIONS.keys():
    regions_df[region] = scaled_df.filter(pl.col('code').is_in(REGIONS[region]))
