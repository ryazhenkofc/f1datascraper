import pytest
from unittest.mock import patch, Mock
from formulascraper import Formula3Scraper

@pytest.fixture
def scraper():
    return Formula3Scraper()

def test_get_drivers_data(scraper):
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.text = '<html><table class="table table-bordered"><tr></tr><tr><td>Driver 1</td></tr></table></html>'
        mock_get.return_value = mock_response

        drivers_data = scraper.get_drivers_data(2021)
        assert len(drivers_data) == 1
        assert drivers_data[0]['driver'] == 'Driver 1'

def test_get_races_data(scraper):
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.text = '<html><table class="table table-bordered"><tr></tr><tr><td>Race 1</td></tr></table></html>'
        mock_get.return_value = mock_response

        races_data = scraper.get_races_data(2021)
        assert len(races_data) == 1
        assert races_data[0]['race'] == 'Race 1'

def test_get_teams_data(scraper):
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.text = '<html><table class="table table-bordered"><tr></tr><tr><td>Team 1</td></tr></table></html>'
        mock_get.return_value = mock_response

        teams_data = scraper.get_teams_data(2021)
        assert len(teams_data) == 1
        assert teams_data[0]['team'] == 'Team 1'
