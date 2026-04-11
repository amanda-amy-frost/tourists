# Tourist data mini-project

TODO: Add an introduction

## Choice of dataframe library

I was originally going to do this project with the classic pandas + matplotlib combo, but after remembering how unintuitive and cumbersome it can be to use pandas, I found out there's a new kid on the block: polars (https://docs.pola.rs/). It seems to be popular, standarized, and mature and feature complete enough to be a full replacement, and I found it extremely easy to start working with. So, I decided to instead learn enough of polars to make this mini-project. The docs are excellent after all. And while the performance benefits are irrelevant for this project, this seems to be an all-round improvement on pandas by every possible measure, but especially the API.

## Development process

- Prototype everything in iPython, one step at a time.
- Once I have enough to acheive a particular goal, refactor and add the code to a script. Repeat for the next goal.
- At the end, create a Jupyter notebook with the most important code and results, interspersed with text blocks that describe my thought process. Render that to an HTML file as the final main product.

## Interesting questions

- How do tourist visits correlate with the working and retired populations of each country?
- How do they correlate with climate - using a proxy measure of 30+ degree days?
- Are there any interesting tourist trends within the Nordic countries?
- Has Brexit affected tourism from the UK long-term?
- How impactful was COVID on tourism?
- Has the first year of the fascist presidency in USA depressed tourism compared to previous years?
- Can I make any predictions that fill in data for the missing years of some of the datasets?

## Scope and granularity of data

As this is meant to be a small project, the data for all sources is very coarse-grained. For example, while it is possible to extract much more detailed tourist data, from monthly figures, to different regions within Denmark, to where people stayed the night, I wanted to limit how much data I based my analysis on. All data tables are therefore based on annualized figures and relatively few columns.

The tourist data is complete through 2025, the population data through 2024, and the climate data through 2023. All extracted data goes as far back as 1992, as that is the earliest available year for the tourist dataset.

## Data sources

Tourist visits:
https://www.statistikbanken.dk/TURIST

Climate data:
https://climateknowledgeportal.worldbank.org/download-data

Country populations:
https://data-explorer.oecd.org/vis?lc=en&df[ds]=DisseminateFinalDMZ&df[id]=DSD_POPULATION%40DF_POP_HIST&df[ag]=OECD.ELS.SAE&df[vs]=1.0&dq=FIN%2BISL%2BITA%2BNOR%2BPRT%2BSWE%2BAUT%2BFRA%2BDEU%2BIRL%2BNLD%2BESP%2BCHE%2BGBR%2BUSA%2BCAN%2BBEL..PS._T.Y15T64%2BY_GE65.&pd=2014%2C2024&to[TIME_PERIOD]=false&vw=tb

The URL parameters for the country populations encode the exact settings for the table I generated and saved as a raw .csv.

## Misc notes

The tourist data was small and well-formatted enough that it made sense to manually edit the file.
