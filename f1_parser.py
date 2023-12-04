import f1_data_parser

year = input(f"Enter year: ").strip()

drivers_data = f1_data_parser.parse_drivers_data(year)
races_data = f1_data_parser.parse_races_data(year)
teams_data = f1_data_parser.parse_teams_data(year)
fastest_laps_data = f1_data_parser.parse_fastest_laps_data(year)

# Process and save the extracted data
