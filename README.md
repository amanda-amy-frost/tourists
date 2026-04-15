# Tourist data mini-project (2026)

- [Executive summary](#executive-summary)
- [Introduction](#introduction)
- [Choice of dataframe library](#choice-of-dataframe-library)
- [Development process](#development-process)
- [Interesting questions](#interesting-questions)
- [Scope and granularity of data](#scope-and-granularity-of-data)
- [Data sources](#data-sources)
- [Misc notes](#misc-notes)

## Executive summary

This project uses a few publicly available data sources, based primarily around overnight stays in Denmark from various Global North countries, to perform some data analysis on interesting questions that arise from combining those sources.

The main product of this project is a Jupyter notebook that tells the full story, from data extraction, to transformation, to charts and statistics. The scripts, data, and other useful artifacts that were used to build this project can be found in their respective folders.

- Key questions
- Main conclusions
- A few charts

## Introduction

The goal of this project is to use open source data to perform some introductory analysis on various questions related to tourist visits - specifically overnight stays - in Denmark. That data forms the foundation that everything else is based around. Along with an extract of that data, I

- Executive summary
- Basic ideas
- Hypotheses and testing
- Analysis and charts
- Conclusions
- Open questions

## Choice of dataframe library

I was originally going to do this project with the classic pandas + matplotlib combo, but there have been some interesting developments over the last several years in the dataframe and data visualization space. Pandas' API can be cumbersome and unintuitive, and libraries that accomplish similar goals have exploded in popularity recently, and for good reason.

Among them is [Polars](https://docs.pola.rs/). It seems to be popular, standarized, and mature and feature complete enough to be a full replacement, and I found it extremely easy to start working with. So, I decided to instead learn enough of Polars to make this mini-project. The docs are excellent after all. And while the performance benefits are irrelevant for this project, this seems to be an all-round improvement on pandas by every possible measure, but especially the API.

Polars also has native support for [Altair](https://altair-viz.github.io/index.html), so I used that library to render charts and plots.

## Development process

- Prototype everything in iPython, one step at a time.
- Once I have enough to acheive a particular goal, refactor and add the code to a script. Repeat for the next goal.
- At the end, create a Jupyter notebook with the most important code and results, interspersed with text blocks that explain my thought process. Render that to an HTML file as the final main artifact.

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

See the images folder for screenshots of how the data was selected from each source.

- [Tourist visits](https://www.statistikbanken.dk/TURIST)
- [Climate data](https://climateknowledgeportal.worldbank.org/download-data)
  - [Sample API call for Spain](https://cckpapi.worldbank.org/api/v1/era5-x0.25_timeseries_hd30_timeseries_annual_1950-2023_mean_historical_era5_x0.25_mean/ESP?_format=json)
- [Country populations (link goes to exact configuration)](https://data-explorer.oecd.org/vis?lc=en&df[ds]=DisseminateFinalDMZ&df[id]=DSD_POPULATION%40DF_POP_HIST&df[ag]=OECD.ELS.SAE&df[vs]=1.0&dq=FIN%2BISL%2BITA%2BNOR%2BPRT%2BSWE%2BAUT%2BFRA%2BDEU%2BIRL%2BNLD%2BESP%2BCHE%2BGBR%2BUSA%2BCAN%2BBEL..PS._T._T%2BY15T64%2BY_GE65.&pd=1992%2C2024&to[TIME_PERIOD]=false&vw=tb)

## Misc notes

The tourist data was small and well-formatted enough that it made sense to manually edit the file.
