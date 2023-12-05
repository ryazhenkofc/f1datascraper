from f1datascraper import *
import prettytable as pt

parser = FormulaOneParser()
table = pt.PrettyTable()

table.title = 'Formula 1 2023 Season'

drivers_data = parser.parse_drivers_data(2023)
table.field_names = ['Position', 'Name', 'Nationality', 'Car', 'Points']


for driver in drivers_data:
    table.add_row([driver['position'], driver['name'], driver['nationality'], driver['car'], driver['points']])

print(table)
table.clear()

races_data = parser.parse_races_data(2023)
table.field_names = ['Grand Prix', 'Date', 'Winner', 'Car', 'Laps']

for race in races_data:
    table.add_row([race['grandprix'], race['date'], race['winner'], race['car'], race['laps']])
    
print(table)
table.clear()

teams_data = parser.parse_teams_data(2023)

table.field_names = ['Position', 'Team', 'Points']


for team in teams_data:
    table.add_row([team['position'],team['team'], team['points']])
    
print(table)
table.clear()

fastest_laps_data = parser.parse_fastest_laps_data(2023)

table.field_names = ['Grand Prix', 'Driver', 'Team', 'Lap Time']


for lap in fastest_laps_data:
    table.add_row([lap['grandprix'], lap['driver'], lap['team'], lap['lap_time']])
    
print(table)
table.clear()