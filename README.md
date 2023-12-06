# formulascraper #

## What is this? ##
This module extract Formula 1, F1 Academy, Formula 2, Formula 3 data, encompassing drivers, races, teams, and fastest laps, through a parser.

Categories from which you can pull data:

- Drivers Standings (`drivers`)
- Race Results (`races`)
- Teams Standing (`teams`)
- Fastest Laps Results (`fastest_laps`)

> **Formula 1**
> 
> Each category is since 1950, but Teams Standings only since 1958

> **Formula 1 Academy**
> 
> Each category is since 2023

> **Formula 2**
> 
> Each category is since 2017

> **Formula 3**
> 
> Each category is since 2019

**Quick Guide**

The module is based on the following structure:

    
    from formulascraper import Formula1Scraper, get_drivers_data

	scraper = Formula1Scraper()
	drivers_data = scraper.get_drivers_data({YEAR})


----------




## Getting Started ##
**Installation**

Using the library is as simple and convenient as possible:
Installing the package with `pip`:

	pip install formulascraper

**Classes and functions that available:**

> Formula1Scraper:

	get_drivers_data(year)
	get_races_data(year)
	get_teams_data(year)
	get_fastest_laps_data(year)

> Formula1AcademyScraper:

	get_drivers_data(year)
	get_races_data(year)
	get_teams_data(year)

> Formula2Scraper:

	get_drivers_data(year)
	get_races_data(year)
	get_teams_data(year)

> Formula3Scraper:

	get_drivers_data(year)
	get_races_data(year)
	get_teams_data(year)

## Using ##

Examples of all operations:

Import the `Formula1Scraper` class:

	from formulascraper import Formula1Scraper

Initialize a `scraper` object:

	scraper = Formula1Scraper()

Scraping Data
Call the parsing methods on the parser object, passing in the year:

**`get_{category}_data` takes as an argument only one argument which is `{year}`**

	drivers_data = scraper.get_drivers_data(2021)
	races_data = scraper.get_races_data(2023)
	teams_data = scraper.get_teams_data(2018) 
	fastest_laps = scraper.get_fastest_laps_data(1999)


----------

## Developer ##
My profile: [ryazhenkofc](https://github.com/ryazhenkofc) 
