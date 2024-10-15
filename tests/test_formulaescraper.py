import pytest
from unittest.mock import patch, Mock
from formulascraper import FormulaEScraper

@pytest.fixture
def scraper():
    return FormulaEScraper()

def test_get_drivers_data(scraper):
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = [
            {
                "driverTeamName": "Team 1",
                "driverPosition": "1",
                "driverFirstName": "Driver",
                "driverLastName": "One",
                "driverCountry": "Country 1",
                "driverPoints": "100"
            }
        ]
        mock_get.return_value = mock_response

        drivers_data = scraper.get_drivers_data(2021)
        assert len(drivers_data) == 1
        assert drivers_data[0]['driverTeamName'] == 'Team 1'
        assert drivers_data[0]['driverPosition'] == '1'
        assert drivers_data[0]['driverFirstName'] == 'Driver'
        assert drivers_data[0]['driverLastName'] == 'One'
        assert drivers_data[0]['driverCountry'] == 'Country 1'
        assert drivers_data[0]['driverPoints'] == '100'

def test_get_teams_data(scraper):
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = [
            {
                "teamName": "Team 1",
                "teamPosition": "1",
                "teamPoints": "200"
            }
        ]
        mock_get.return_value = mock_response

        teams_data = scraper.get_teams_data(2021)
        assert len(teams_data) == 1
        assert teams_data[0]['teamName'] == 'Team 1'
        assert teams_data[0]['teamPosition'] == '1'
        assert teams_data[0]['teamPoints'] == '200'

def test_get_races_data(scraper):
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {
            "races": [
                {
                    "name": "Race 1",
                    "date": "2021-01-01"
                }
            ]
        }
        mock_get.return_value = mock_response

        races_data = scraper.get_races_data(2021)
        assert len(races_data) == 1
        assert races_data[0]['raceName'] == 'Race 1'
        assert races_data[0]['raceDate'] == '2021-01-01'
