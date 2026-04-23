<!-- omit in toc -->
# Tourist data mini-project (2026)

- [Introduction](#introduction)
- [Interactive dashboard](#interactive-dashboard)
- [Current progress](#current-progress)
- [Charts](#charts)
  - [Regional visits scaled by population](#regional-visits-scaled-by-population)
  - [Preliminary findings](#preliminary-findings)
- [Preliminary findings](#preliminary-findings-1)
  - [Regional groupings](#regional-groupings)
  - [Outliers in earlier years of tourist data](#outliers-in-earlier-years-of-tourist-data)
  - [Preliminary regional trends](#preliminary-regional-trends)
  - [UK economic trends](#uk-economic-trends)
  - [Early indications of the role of climate change?](#early-indications-of-the-role-of-climate-change)
  - [Dependency ratio](#dependency-ratio)
- [Research questions](#research-questions)
- [Technical decisions](#technical-decisions)
  - [Choice of dataframe library](#choice-of-dataframe-library)
  - [Development process](#development-process)
  - [Statistics packages to consider](#statistics-packages-to-consider)
- [Data sources](#data-sources)

## Introduction

**This project is still under active development and is subject to frequent changes.**

**Read the current report as a [notebook](./scripts/DataAnalysis.ipynb) or as a [PDF](DataAnalysis.pdf), with commentary and analysis in Danish and English.**

This project is an introductory exploration of a [tourist database](https://www.statistikbanken.dk/TURIST) that tracks overnight stays in Denmark by nationality, time period, country region, and other categories. The goal of this project is to gain a sufficient overview of this data, find insights, propose and test hypotheses, visualize and analyze results, and draw useful conclusions.

The scope is limited to annualized data for a representative sample of Global North countries. Besides the tourist data extract (current through 2025), there is also annual population data for each country via the [OECD](https://data-explorer.oecd.org/vis?lc=en&df[ds]=DisseminateFinalDMZ&df[id]=DSD_POPULATION%40DF_POP_HIST&df[ag]=OECD.ELS.SAE&df[vs]=1.0&dq=FIN%2BISL%2BITA%2BNOR%2BPRT%2BSWE%2BAUT%2BFRA%2BDEU%2BIRL%2BNLD%2BESP%2BCHE%2BGBR%2BUSA%2BCAN%2BBEL..PS._T._T%2BY15T64%2BY_GE65.&pd=1992%2C2024&to[TIME_PERIOD]=false&vw=tb) (current through 2024) and annualized climate proxy data (number of days over 30 degrees Celsius) from the [ERA5](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) dataset (current through 2023).

See [data](data) for the raw and processed files.

The limiting starting year for the data is the tourist dataset, which extends back to 1992. Data normalization to exclude outlier years yields a start year of 2005.

<details>

<summary><b>Show or hide list of countries</b></summary>

- Austria
- Belgium
- Canada
- Finland
- France
- Germany
- Iceland
- Ireland
- Italy
- Netherlands
- Norway
- Portugal
- Spain
- Sweden
- Switzerland
- United Kingdom
- United States

</details>

## Interactive dashboard

[Go to dashboard](https://molab.marimo.io/notebooks/nb_SuhkMpUkmvbTHzRQd2rt21/app)

The dashboard my be expanded in the future with additional functionality, but it is feature complete for now.

![Tourism dashboard](./images/screenshots/tourism-dashboard.png)

## Current progress

- :ballot_box_with_check: Select relevant data
- :ballot_box_with_check: Data extraction
- :ballot_box_with_check: Process initial data
- :ballot_box_with_check: Data normalization
- :ballot_box_with_check: Initial visualization
- :ballot_box_with_check: Initial commentary
- :ballot_box_with_check: (Optional) Notebook to PDF automation
  - [Action repository](https://github.com/amanda-amy-frost/jupyter-to-pdf-action)
- :ballot_box_with_check: (Optional) Marimo toy example
  - [Interactive dashboard](https://molab.marimo.io/notebooks/nb_SuhkMpUkmvbTHzRQd2rt21/app)
  - [GitHub repository](https://github.com/amanda-amy-frost/tourists-dashboard)
- :x: (Optional) Power BI dashboard
  - Blocked from publishing due to Microsoft's account [requirements](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-publish-to-web#prerequisites) (i.e. work email)
  - See [screenshot](./images/screenshots/power-bi.png) for initial experimentation
- :ballot_box_with_check: Preliminary findings
- :ballot_box_with_check: Formulate research questions
- :pause_button: Technical documentation (see [notebook](./scripts/DataAnalysis.ipynb))
- :ballot_box_with_check: Expand dashboard functionality
- :ballot_box: Select statistical tools and methods
- :ballot_box: Statistical analysis
- :ballot_box: Final chart generation
- :ballot_box: Analysis write-up
- :ballot_box: Conclusion write-up
- :ballot_box: Summary write-up in Danish
- :ballot_box: Fix PDF automation bug
- :ballot_box: (Optional) Auto-deploy dashboard

## Charts

### Regional visits scaled by population

<details>

<summary><b>Click to show or hide</b></summary>

**"Big hitters"**

![Big hitters](./images/svg/big_hitters.svg)

**Western EU**

![Western EU](./images/svg/west_eu.svg)

**Nordics (excluding Denmark)**

![Nordics](./images/svg/nordics.svg)

**Southern EU**

![Southern EU](./images/svg/south_eu.svg)

**North America**

![North America](./images/svg/nor_amer.svg)

</details>

### Preliminary findings

<details>

<summary><b>Click to show or hide</b></summary>

**Financial crash (UK)**

![UK financial crash](./images/svg/uk_financial_crash.svg)

![Financial crash table](./images/tables/uk_financial_crash_table.png)

**Additional impact of Brexit**

![Brexit](./images/svg/uk_brexit.svg)

![Brexit table](./images/tables/uk_brexit_table.png)

</details>

<!--
### Potential statistical approach

Curve fitting, regressions, hypothesis testing
-->

## Preliminary findings

<!--TODO reason for choosing hot days as proxy climate measure-->

<details open>

<summary><b>Show or hide section</b></summary>

**NB: I use "visits" to refer to overnight stays for brevity, and "visitors" also signifies people within this set.**

### Regional groupings

I decided to group the 17 countries in my dataset into 5 regions:

- "Big hitters": Germany, Netherlands
- Western EU: Austria, Belgium, France, Ireland, Switzerland, UK
- Nordics: Finland, Iceland, Norway, Sweden
- Southern EU: Italy, Portugal, Spain
- North America: Canada, United States

The "big hitters" are so named because, by portion of the total population, both countries far exceed the other western European countries and make visualization more difficult if they are grouped into the same region. The other groupings should hopefully make reasonable sense without further justification.

### Outliers in earlier years of tourist data

While the tourist data goes back to 1992, some countries such as Iceland, Portugal, and Ireland were clear outliers until the early 2000s due to how few people visited Denmark at the time. I decided to exclude these years entirely (for all countries) to avoid skewing the data and performing an incorrect analysis. For completeness and visualization purposes, those years are still included in the [interactive dsahboard](https://molab.marimo.io/notebooks/nb_SuhkMpUkmvbTHzRQd2rt21/app).

To first find which year to start at though, I needed some process to exclude the outliers. My process for doing this was a bit loose. I wanted to use the standard deviation in some way as my primary indicator for the variability of the data. There are also other metrics worthy of consideration, but I wanted to be straightforward and just find some reasonable start year without considering which would best apply here.

I decided to do the following: I wanted to find some constant to multiply the standard deviation with such that the first year ("starting year") of the filtered dataset would be the year where all countries had visits that were *at minimum* that value below the mean *or above*. In other words:

$\exists x : \forall y \geq y_0 \, \forall c \in C \; v_{yc} \geq \mu(v_{yc}) - x\sigma(v_{yc})$

Where $y_0$ is the "starting year", $c$ is a country from the set of countries $C$ in my dataset, $v_{yc}$ is visits from that country in that year, $\mu$ is the mean, $\sigma$ is the standard deviation, and $x$ is what I want to find for my dataset to look reasonable.

If your eyes glaze over at the sight of the above expression, then the simplified version is:

$v \geq \mu(v) - x\sigma(v)$

For every year and country starting at some base year.

The one caveat is that this was an iterative process, where every iteration set a new potential starting year as the foundation for the data, if the previous iteration still had outlier years. This trial starting year would be the *maximum of the minimum suggested* years of the previous iteration, where the "minimum year" for each country is the first year that lies within the bounds defined by the above inequality.

$F(y) = \min_y : v_y \geq \mu(v_y) - x\sigma(v_y)$

$\text{For }n = 0,1,2,... \text{ while } y_{n+1} \neq y_{n}$

$y_{n+1} = \max_{y_n} F(y_n)$

The standard deviation and mean would then be re-evaluated for each country by only considering data from the trial starting year and above. These would set the new boundary (above some constant $x$ multiple) for determining remaining outliers in the new iteration. When the year stabilized - i.e. went through one full iteration without increasing - then I would choose that as the definitive starting year for the full dataset.

In actuality, I played around with $x$ in order to find a reasonable $y_0$. I ended up settling on a value of 1.2 for $x$, which yielded a starting year of 2005. A sanity check confirms that this year seems like a reasonable start, as Iceland is the final outlier in 2004, and its visits jump more than an order of magnitude from that year to the next.

### Preliminary regional trends

Speaking of, Iceland is one of those interesting countries that is worth highlighting, as I wanted to see if there were any economic trends I could infer from this data. The initial graphs I made charted the the overnight stays in proportion to the each country's population, and Iceland stands out as a country particularly impacted by the 2008 financial crash.

<details>

<summary><b>Show or hide Nordics chart</b></summary>

![Nordics](./images/svg/nordics.svg)

</details>

To be able to see just how much that event affected Icelandic tourism in comparison to related countries was enlightening.

It is also interesting to see the overall decline in tourism from the rest of the Nordics in this data. I don't think I can give any particular insight at this point, but one hypothesis is that the culture, architecture, and variety of experiences and activities to explore is more homogenous between these countries. And if prices become more competitive over time, where for the same price or less you can travel to more "exotic" destinations like Italy (or anywhere else), then there is less likely to be a draw to Denmark from the rest of the Nordics.

In fact, in a different project it would be interesting to look at the spatiotemporal variation in flight ticket prices (or full travel packages) from different starting countries.

### UK economic trends

For both the 2008 financial crash, as well as for Brexit, the UK seems to have been particularly (disproportionately) affected by these two events. The UK left the EU almost exactly when COVID hit, so there are clear visual indications of how UK tourism has been suppressed if one assumes that neighboring countries more or less suffered the same economic effects from COVID. That question is also interesting in itself, namely whether the tourist data can be used as a proxy to suggest which countries were more impacted by COVID.

**UK financial crash**

<details>

<summary><b>Show or hide graphs</b></summary>

![UK financial crash](./images/svg/uk_financial_crash.svg)

![Financial crash table](./images/tables/uk_financial_crash_table.png)

</details>

**Brexit**

<details>

<summary><b>Show or hide graphs</b></summary>

![Brexit](./images/svg/uk_brexit.svg)

![Brexit table](./images/tables/uk_brexit_table.png)

</details>

### Early indications of the role of climate change?

One hypothesis I wanted to test, to the point I decided to find some basic data on it, was whether the ever escalating effects of climate change could play a role in deciding who travels where. As Denmark lies more north and has a reputation for being a more tolerable climate during summer, one would expect that tourism would increase from warmer, more southern climates like in Italy and Spain. Indeed, this is what we see:

<details>

<summary><b>Show or hide Southern EU charts</b></summary>

![Nordics](./images/svg/south_eu.svg)

</details>

While it would be nice to track the monthly or seasonal data to see if the summer months are where we comparatively see higher spikes from these countries, that is unfortunately outside the scope of this project. Regardless, I have the annual data for the number of days over 30 degrees (Celsius) for each country, and this can be used a proxy measure for seeing if there is a meaningful relationship between visits and the climate of each country.

### Dependency ratio

The dependency ratio of a country is measured by the portion of people too old or too young to work compared to the working age population. For the [dataset](https://data-explorer.oecd.org/vis?lc=en&df[ds]=DisseminateFinalDMZ&df[id]=DSD_POPULATION%40DF_POP_HIST&df[ag]=OECD.ELS.SAE&df[vs]=1.0&dq=FIN%2BISL%2BITA%2BNOR%2BPRT%2BSWE%2BAUT%2BFRA%2BDEU%2BIRL%2BNLD%2BESP%2BCHE%2BGBR%2BUSA%2BCAN%2BBEL.DEPEND_RATIO.._T..&pd=1992%2C2024&to[TIME_PERIOD]=false&vw=tb) I used, the working age population was defined as being between 20 and 64 years old. For some countries in my dataset, this number increases by about 10 percentage points over the last 20 years. See Belgium, Finland, and France as examples. For others, this ratio either stays stable or even decreases. See Austria, Canada, and Norway as examples there.

What I am interested in however is the elderly dependency ratio, or the ratio of retired people compared to the rest of the population. This is increasing in all countries in my dataset, but by different amounts. I am curious if there is a correlation between the ratio of elderly people in a country's population and how popular Denmark is as a tourist destination.

However, the total dependency ratio could prove more useful comparatively, but that remains to be seen.

</details>

## Research questions

- How does tourism to Denmark correlate with the elderly and total dependency ratios?
- How much has Brexit meaningfully impacted UK tourism to Denmark compared to similar countries?
- Does the warmth of a country's climate affect tourist visits to Denmark?
- Just how impactful was COVID on overall tourism?
  - Are there still any long-term effects that can be seen? (E.g. Is the increasing demand from countries still suppressed compared to before COVID?)
  - What was the magnitude of the impact of COVID on tourism? In other words, how suppressed was tourism during the peak years of COVID?
- Similarly, what insights can be gleamed about the 2008 financial crash based on the data?
- Can I use the data I have to make predictions about the missing years from my climate and population datasets? And can those predictions be used as a measure for the accuracy of my predictions and underlying analysis?

## Technical decisions

### Choice of dataframe library

I was originally going to do this project with the classic [pandas](https://pandas.pydata.org/) + [matplotlib](https://matplotlib.org/) combo, but there have been some interesting developments over the last several years in the dataframe and data visualization space. The pandas API can be cumbersome and unintuitive, and libraries that accomplish similar goals have exploded in popularity recently, and for good reason.

Among them is [Polars](https://docs.pola.rs/). It seems to be popular, standardized, and mature and feature complete enough to be a full replacement, and I found it extremely easy to start working with. So, I decided to instead learn enough of Polars to make this mini-project. The docs are excellent after all. And while the performance benefits are irrelevant for this project, this seems to be an all-round improvement on pandas by every possible measure, but especially the API.

Polars also has native support for [Altair](https://altair-viz.github.io/index.html), so I used that library to render charts and plots.

TODO: Multiple ways of compatibility between Polars and pandas: functions, Narwhals

### Development process

- Prototype everything in [iPython](https://ipython.org/features/), one step at a time.
- Once I have enough to achieve a particular goal, refactor and add the code to a script. Repeat for the next goal.
- At the end, create a Jupyter notebook with the most important code and results, interspersed with text blocks that explain my thought process. Render that to a PDF as the final main artifact.

### Statistics packages to consider

I haven't yet needed to use these libraries so far, but for statistical analysis, I am considering one or more of the following:

- [scipy](https://docs.scipy.org/doc/scipy/tutorial/index.html#user-guide)
  - [stats module](https://docs.scipy.org/doc/scipy/tutorial/stats.html)
  - [curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)
- [numpy](https://numpy.org/doc/stable/index.html)
  - [statistics](https://numpy.org/doc/stable/reference/routines.statistics.html)
- [scikit-learn](https://scikit-learn.org/stable/)
  - [regressions](https://scikit-learn.org/stable/supervised_learning.html)

<!--
### Local prerequisites

- Jupyter notebook
- LaTex? rendering
- Polars
- Altair
- Anything else?
- Relative file path issues?

### Development environment

- Potential issues with file references (images)
- Windows
- VS code
  - extensions?
- Git
- python packages and versions (and python version)

### Interesting tools for the future

Although outside the scope of this project and a secondary consideration...

- GitHub pages
- Marimo
- Narwhals
- DuckDB
- uv
- Prefect
- WSL
-->

## Data sources

See the images folder for screenshots of how the data was selected from each source.

- [Tourist visits](https://www.statistikbanken.dk/TURIST)
- [Climate data](https://climateknowledgeportal.worldbank.org/download-data)
  - [Sample API call for Denmark](https://cckpapi.worldbank.org/api/v1/era5-x0.25_timeseries_hd30_timeseries_annual_1950-2023_mean_historical_era5_x0.25_mean/DNK?_format=json)
- [Country populations (link goes to exact configuration)](https://data-explorer.oecd.org/vis?lc=en&df[ds]=DisseminateFinalDMZ&df[id]=DSD_POPULATION%40DF_POP_HIST&df[ag]=OECD.ELS.SAE&df[vs]=1.0&dq=FIN%2BISL%2BITA%2BNOR%2BPRT%2BSWE%2BAUT%2BFRA%2BDEU%2BIRL%2BNLD%2BESP%2BCHE%2BGBR%2BUSA%2BCAN%2BBEL..PS._T._T%2BY15T64%2BY_GE65.&pd=1992%2C2024&to[TIME_PERIOD]=false&vw=tb)
  - [Old age dependency ratio](https://data-explorer.oecd.org/vis?lc=en&df[ds]=DisseminateFinalDMZ&df[id]=DSD_POPULATION%40DF_POP_HIST&df[ag]=OECD.ELS.SAE&df[vs]=1.0&dq=FIN%2BISL%2BITA%2BNOR%2BPRT%2BSWE%2BAUT%2BFRA%2BDEU%2BIRL%2BNLD%2BESP%2BCHE%2BGBR%2BUSA%2BCAN%2BBEL.DEPEND_RATIO_OLD.._T..&pd=1992%2C2024&to[TIME_PERIOD]=false&vw=tb)
  - [Total dependency ratio](https://data-explorer.oecd.org/vis?lc=en&df[ds]=DisseminateFinalDMZ&df[id]=DSD_POPULATION%40DF_POP_HIST&df[ag]=OECD.ELS.SAE&df[vs]=1.0&dq=FIN%2BISL%2BITA%2BNOR%2BPRT%2BSWE%2BAUT%2BFRA%2BDEU%2BIRL%2BNLD%2BESP%2BCHE%2BGBR%2BUSA%2BCAN%2BBEL.DEPEND_RATIO.._T..&pd=1992%2C2024&to[TIME_PERIOD]=false&vw=tb)
