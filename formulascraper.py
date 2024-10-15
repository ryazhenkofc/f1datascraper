"""
Module containing classes for scraping data from Formula websites.
"""
import re
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any
from config import Config


class BaseScraper:
    """
    Base class for scraping data from Formula websites.
    """
    def __init__(self, base_url: str):
        """
        Initialize the class with the base URL for the website.
        """
        self.base_url = base_url

    def get_data(self, url: str) -> BeautifulSoup:
        """
        Make an HTTP request and return the parsed HTML content.

        Args:
            url: The URL to make the request to.

        Returns:
            A BeautifulSoup object containing the parsed HTML content.
        """
        response = requests.get(url, timeout=5)
        return BeautifulSoup(response.text, features="html.parser")

    def _extract_info(self, row: Any, patterns: Dict[str, str]) -> Dict[str, str]:
        """
        Extract information from a table row based on the provided patterns.

        Args:
            row: The table row to extract information from.
            patterns: A dictionary of patterns to use for extraction.

        Returns:
            A dictionary containing the extracted information.
        """
        info = {}
        for key, pattern in patterns.items():
            match = re.findall(pattern, str(row))
            info[key] = match[0].strip() if match else None
        return info


class Formula1Scraper(BaseScraper):
    """
    Class for scraping Formula 1 data from the official website.
    """
    def __init__(self):
        """
        Initialize the class with the base URL for the website.
        """
        super().__init__(Config.BASE_URL_F1)

    def get_drivers_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the driver data for a specific year.

        Args:
            year: The year for which to retrieve driver data.

        Returns:
            A list of dictionaries containing driver information for each driver.
        """
        if year < 1950:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}{year}/drivers.html"
        soup = self.get_data(url)

        drivers_data = []
        for table in soup.find_all('table', class_='resultsarchive-table'):
            for row in table.find_all('tr')[1:]:
                driver_info = self._extract_info(row, Config.DRIVER_PATTERNS_F1)
                drivers_data.append(driver_info)

        return drivers_data

    def get_races_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the race data for a specific year.

        Args:
            year: The year for which to retrieve race data.

        Returns:
            A list of dictionaries containing race information for each race.
        """
        if year < 1950:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}{year}/races.html"
        soup = self.get_data(url)

        races_data = []
        for table in soup.find_all('table', class_='resultsarchive-table'):
            for row in table.find_all('tr')[1:]:
                race_info = self._extract_info(row, Config.RACE_PATTERNS_F1)
                races_data.append(race_info)

        return races_data

    def get_teams_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the team data for a specific year.

        Args:
            year: The year for which to retrieve race data.

        Returns:
            A list of dictionaries containing team information for each team.
        """
        if year < 1958:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}{year}/team.html"
        soup = self.get_data(url)

        teams_data = []
        for table in soup.find_all('table', class_='resultsarchive-table'):
            for row in table.find_all('tr')[1:]:
                team_info = self._extract_info(row, Config.TEAM_PATTERNS_F1)
                teams_data.append(team_info)

        return teams_data

    def get_fastest_laps_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the fastest laps data for a specific year.

        Args:
            year: The year for which to retrieve fastest laps data.

        Returns:
            A list of dictionaries containing team information of fastests for each grandprix.
        """
        if year < 1950:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}{year}/fastest-laps.html"
        soup = self.get_data(url)

        fastest_laps_data = []
        for table in soup.find_all('table', class_='resultsarchive-table'):
            for row in table.find_all('tr')[1:]:
                fastest_lap_info = self._extract_info(row, Config.FASTEST_LAP_PATTERNS_F1)
                fastest_laps_data.append(fastest_lap_info)

        return fastest_laps_data


class Formula1AcademyScraper(BaseScraper):
    """
    Class for scraping Formula 1 Academy data from the official website.
    """
    def __init__(self):
        """
        Initialize the class with the base URL for the website.
        """
        super().__init__(Config.BASE_URL_F1A)

    def get_drivers_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the driver data for a specific year from the official Formula 1 website.

        Args:
            year: The year for which to retrieve driver data.

        Returns:
            A list of dictionaries containing driver information for each driver.
        """
        if year != 2023:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}Driver?seasonId=1"
        soup = self.get_data(url)

        drivers_data = []
        for table in soup.find_all('table', class_='table table-bordered'):
            for row in table.find_all("tr")[1:]:
                driver_info = self._extract_info(row, Config.DRIVER_PATTERNS_F1A)
                drivers_data.append(driver_info)

        return drivers_data

    def get_races_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the race data for a specific year.

        Args:
            year: The year for which to retrieve race data.

        Returns:
            A list of dictionaries containing race information for each race.
        """
        if year != 2023:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}Driver?seasonId=1"
        soup = self.get_data(url)

        races_data = []
        for table in soup.find_all('table', class_='table table-bordered'):
            for row in table.find_all("th")[2:]:
                race_info = self._extract_info(row, Config.RACE_PATTERNS_F1A)
                races_data.append(race_info)

        return races_data

    def get_teams_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the team data for a specific year.

        Args:
            year: The year for which to retrieve race data.

        Returns:
            A list of dictionaries containing team information for each team.
        """
        if year != 2023:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}Team?seasonId=1"
        soup = self.get_data(url)

        teams_data = []
        for table in soup.find_all('table', class_='table table-bordered'):
            for row in table.find_all("tr")[1:]:
                team_info = self._extract_info(row, Config.TEAM_PATTERNS_F1A)
                teams_data.append(team_info)

        return teams_data


class Formula2Scraper(BaseScraper):
    """
    Class for scraping Formula 2 data from the official website.
    """
    def __init__(self):
        """
        Initialize the class with the base URL for the website.
        """
        super().__init__(Config.BASE_URL_F2)

    def get_drivers_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the driver data for a specific year from the official Formula 1 website.

        Args:
            year: The year for which to retrieve driver data.

        Returns:
            A list of dictionaries containing driver information for each driver.
        """
        if year < 2017:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}Driver?seasonId={year-1843}"
        soup = self.get_data(url)

        drivers_data = []
        for table in soup.find_all('table', class_='table table-bordered'):
            for row in table.find_all("tr")[1:]:
                driver_info = self._extract_info(row, Config.DRIVER_PATTERNS_F2)
                drivers_data.append(driver_info)

        return drivers_data

    def get_races_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the race data for a specific year.

        Args:
            year: The year for which to retrieve race data.

        Returns:
            A list of dictionaries containing race information for each race.
        """
        if year < 2017:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}Driver?seasonId={year-1843}"
        soup = self.get_data(url)

        races_data = []
        for table in soup.find_all('table', class_='table table-bordered'):
            for row in table.find_all("th")[2:]:
                race_info = self._extract_info(row, Config.RACE_PATTERNS_F2)
                races_data.append(race_info)

        return races_data

    def get_teams_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the team data for a specific year.

        Args:
            year: The year for which to retrieve race data.

        Returns:
            A list of dictionaries containing team information for each team.
        """
        if year < 2017:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}Team?seasonId={year-1843}"
        soup = self.get_data(url)

        teams_data = []
        for table in soup.find_all('table', class_='table table-bordered'):
            for row in table.find_all("tr")[1:]:
                team_info = self._extract_info(row, Config.TEAM_PATTERNS_F2)
                teams_data.append(team_info)

        return teams_data


class Formula3Scraper(BaseScraper):
    """
    Class for scraping Formula 3 data from the official website.
    """
    def __init__(self):
        """
        Initialize the class with the base URL for the website.
        """
        super().__init__(Config.BASE_URL_F3)

    def get_drivers_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the driver data for a specific year from the official Formula 1 website.

        Args:
            year: The year for which to retrieve driver data.

        Returns:
            A list of dictionaries containing driver information for each driver.
        """
        if year < 2019:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}Driver?seasonId={year-1843}"
        soup = self.get_data(url)

        drivers_data = []
        for table in soup.find_all('table', class_='table table-bordered'):
            for row in table.find_all("tr")[1:]:
                driver_info = self._extract_info(row, Config.DRIVER_PATTERNS_F3)
                drivers_data.append(driver_info)

        return drivers_data

    def get_races_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the race data for a specific year.

        Args:
            year: The year for which to retrieve race data.

        Returns:
            A list of dictionaries containing race information for each race.
        """
        if year < 2019:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}Driver?seasonId={year-1843}"
        soup = self.get_data(url)

        races_data = []
        for table in soup.find_all('table', class_='table table-bordered'):
            for row in table.find_all("th")[2:]:
                race_info = self._extract_info(row, Config.RACE_PATTERNS_F3)
                races_data.append(race_info)

        return races_data

    def get_teams_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the team data for a specific year.

        Args:
            year: The year for which to retrieve race data.

        Returns:
            A list of dictionaries containing team information for each team.
        """
        if year < 2019:
            raise ValueError(f"Invalid year: {year}")
        url = f"{self.base_url}Team?seasonId={year-1843}"
        soup = self.get_data(url)

        teams_data = []
        for table in soup.find_all('table', class_='table table-bordered'):
            for row in table.find_all("tr")[1:]:
                team_info = self._extract_info(row, Config.TEAM_PATTERNS_F3)
                teams_data.append(team_info)

        return teams_data


class FormulaEScraper(BaseScraper):
    """
    Class for scraping Formula E data from the official website.
    """
    def __init__(self):
        """
        Initialize the class with the base URL for the website and seasonsId.
        """
        super().__init__(Config.BASE_URL_FE)
        self.season_ids = Config.SEASON_IDS_FE

    def get_drivers_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the driver data for a specific year.

        Args:
            year: The year for which to retrieve driver data.

        Returns:
            A list of dictionaries containing driver information for each driver.
        """
        if year not in self.season_ids:
            raise ValueError(f"Invalid year: {year}")

        url = f"{self.base_url}standings/drivers?championshipId={self.season_ids[year]}"
        response = requests.get(url, timeout=5)
        data = response.json()

        drivers_data = self._extract_driver_data(data)

        return drivers_data

    def get_teams_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the team data for a specific year.

        Args:
            year: The year for which to retrieve race data.

        Returns:
            A list of dictionaries containing team information for each team.
        """
        if year not in self.season_ids:
            raise ValueError(f"Invalid year: {year}")

        url = f"{self.base_url}standings/teams?championshipId={self.season_ids[year]}"
        response = requests.get(url, timeout=5)
        data = response.json()

        teams_data = [self._extract_team_data(team_data) for team_data in data]

        return teams_data

    def get_races_data(self, year: int) -> List[Dict[str, str]]:
        """
        Scrape the race data for a specific year.

        Args:
            year: The year for which to retrieve race data.

        Returns:
            A list of dictionaries containing race information for each race.
        """
        if year not in self.season_ids:
            raise ValueError(f"Invalid year: {year}")

        url = f"{self.base_url}races?championshipId={self.season_ids[year]}"
        response = requests.get(url, timeout=5)
        data = response.json()["races"]

        races_data = [self._extract_race_data(race_data) for race_data in data]

        return races_data

    def _extract_driver_data(self, driver_data: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        extracted_data = []

        for driver in driver_data:
            driver_info = {
                "driverTeamName": driver["driverTeamName"],
                "driverPosition": driver["driverPosition"],
                "driverFirstName": driver["driverFirstName"],
                "driverLastName": driver["driverLastName"],
                "driverCountry": driver["driverCountry"],
                "driverPoints": driver["driverPoints"],
            }

            extracted_data.append(driver_info)

        return extracted_data

    def _extract_team_data(self, team_data: Dict[str, Any]) -> Dict[str, str]:
        teams_data = {
            "teamName": team_data["teamName"],
            "teamPosition": team_data["teamPosition"],
            "teamPoints": team_data["teamPoints"],
        }

        return teams_data

    def _extract_race_data(self, race_data: Dict[str, Any]) -> Dict[str, str]:
        races_data = {
            "raceName": race_data["name"],
            "raceDate": race_data["date"],
        }

        return races_data
