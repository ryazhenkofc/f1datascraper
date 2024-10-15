# formulascraper #

**What is this?**

This Python library allows you to extract data from various Formula racing websites effortlessly. Get driver standings, race results, team rankings, and fastest laps for Formula 1, F1 Academy, Formula 2, Formula 3 and Formula E.

**Features:**

- Scrape driver standings, race results, team rankings, and fastest laps for multiple Formula racing categories.
- Supports Formula 1, F1 Academy, Formula 2, Formula 3, and Formula E.
- Easy-to-use API for extracting data.
- Configurable and extendable for future updates.

## Table of Contents

1. [Quickstart](#quickstart)
2. [Detailed Examples](#detailed-examples)
3. [Data Availability](#data-availability)
4. [Running Unit Tests](#running-unit-tests)
5. [Contributing](#contributing)
6. [Reporting Issues and Requesting Features](#reporting-issues-and-requesting-features)
7. [License](#license)
8. [Versioning](#versioning)
9. [Author](#author)
10. [Additional Resources](#additional-resources)

## Quickstart ##

**Install**:

	pip install formulascraper

**Import**:

	from formulascraper import Formula1Scraper, get_drivers_data

----------

**Extract Data:**

 Formula 1 data:

	scraper = Formula1Scraper()
	drivers_data = scraper.get_drivers_data(2021)

 Formula 1 Academy data:

	academy_scraper = Formula1AcademyScraper()
	races_data = academy_scraper.get_races_data(2023)

 Formula 2 data:

	f2_scraper = Formula2Scraper()
	teams_data = f2_scraper.get_teams_data(2012)

 Formula 3 data:

	f3_scraper = Formula3Scraper()
	fastest_laps = f3_scraper.get_drivers_data(2021)

 Formula E data:

	fe_scraper = FormulaEScraper()
	fastest_laps = fe_scraper.get_teams_data(2021)

----------

## Detailed Examples

### Formula 1

```python
from formulascraper import Formula1Scraper

scraper = Formula1Scraper()
drivers_data = scraper.get_drivers_data(2021)
print(drivers_data)
```

### Formula 1 Academy

```python
from formulascraper import Formula1AcademyScraper

academy_scraper = Formula1AcademyScraper()
races_data = academy_scraper.get_races_data(2023)
print(races_data)
```

### Formula 2

```python
from formulascraper import Formula2Scraper

f2_scraper = Formula2Scraper()
teams_data = f2_scraper.get_teams_data(2012)
print(teams_data)
```

### Formula 3

```python
from formulascraper import Formula3Scraper

f3_scraper = Formula3Scraper()
fastest_laps = f3_scraper.get_drivers_data(2021)
print(fastest_laps)
```

### Formula E

```python
from formulascraper import FormulaEScraper

fe_scraper = FormulaEScraper()
fastest_laps = fe_scraper.get_teams_data(2021)
print(fastest_laps)
```

## Data Availability

- Formula 1: All categories since 1950 (Teams Standings since 1958)
- Formula 1 Academy: All categories since 2023 (expect fastest_laps)
- Formula 2: All categories since 2017 (expect fastest_laps)
- Formula 3: All categories since 2019 (expect fastest_laps)
- Formula E: All categories since 2015 (expect fastest_laps)

## Running Unit Tests

To run the unit tests, follow these steps:

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Navigate to the `tests` directory:

```bash
cd tests
```

3. Run the tests using `pytest`:

```bash
pytest
```

## Contributing

We welcome contributions to this project! To contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.

For more detailed guidelines, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Reporting Issues and Requesting Features

If you encounter any issues or have feature requests, please report them on the project's issue tracker: [GitHub Issues](https://github.com/ryazhenkofc/formulascraper/issues)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Versioning

This project follows semantic versioning. For a list of changes, see the [CHANGELOG.md](CHANGELOG.md) file.

## Author

ryazhenkofc (GitHub profile: https://github.com/ryazhenkofc)

## Additional Resources

-   Formula 1 Website: [https://www.formula1.com]
-   Formula 1 Academy Website: [https://www.f1academy.com]
-   Formula 2 Website: [https://www.fiaformula2.com]
-   Formula 3 Website: [https://www.fiaformula3.com]
-   Formula E Website: [https://www.fiaformulae.com]

----------

### Version Updates

1.2.2 version update

- small fixes

1.2.1 version update

- added FormulaE scraping
- added valuechecks

1.1.2 version update

- small fixes
- added docstrings

1.1.1 version update

- updated tests
- added categories (Formula 1 Academy, Formula 2, Formula 3)
- updated README.md

1.0.1 version update (Release)

- test samples
- added Formula 1 scraping
