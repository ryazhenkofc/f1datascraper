import unittest
from formulascraper import *

class FormulaOneScraperTests(unittest.TestCase):

    def setUp(self):
        self.scraper = Formula1Scraper()

    def test_get_drivers_data(self):
        drivers_data = self.scraper.get_drivers_data(2023)
        self.assertEqual(len(drivers_data), 22)

        first_driver = drivers_data[0]
        self.assertEqual(first_driver['position'], '1')
        self.assertEqual(first_driver['name'], 'Max Verstappen')
        self.assertEqual(first_driver['nationality'], 'NED')
        self.assertEqual(first_driver['car'], 'Red Bull Racing Honda RBPT')
        self.assertEqual(first_driver['points'], '575')

    def test_get_races_data(self):
        races_data = self.scraper.get_races_data(2023)
        self.assertEqual(len(races_data), 22)

        first_race = races_data[0]
        self.assertEqual(first_race['grandprix'], 'Bahrain')
        self.assertEqual(first_race['date'], '05 Mar 2023')
        self.assertEqual(first_race['winner'], 'Max Verstappen')
        self.assertEqual(first_race['car'], 'Red Bull Racing Honda RBPT')
        self.assertEqual(first_race['laps'], '57')

    def test_get_teams_data(self):
        teams_data = self.scraper.get_teams_data(2023)
        self.assertEqual(len(teams_data), 10)

        first_team = teams_data[0]
        self.assertEqual(first_team['position'], '1')
        self.assertEqual(first_team['team'], 'Red Bull Racing Honda RBPT')
        self.assertEqual(first_team['points'], '860')

    def test_get_fastest_laps_data(self):
        fastest_laps_data = self.scraper.get_fastest_laps_data(2023)
        self.assertEqual(len(fastest_laps_data), 22)

        first_fastest_lap = fastest_laps_data[0]
        self.assertEqual(first_fastest_lap['grandprix'], 'Bahrain')
        self.assertEqual(first_fastest_lap['driver'], 'Zhou')
        self.assertEqual(first_fastest_lap['team'], 'Alfa Romeo Ferrari')
        self.assertEqual(first_fastest_lap['lap_time'], '1:33.996')


if __name__ == '__main__':
    unittest.main()
