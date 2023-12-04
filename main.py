from bs4 import BeautifulSoup
import requests
import re
import csv

def parse_url(url, func, csv_file_name):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, features="html.parser")
    data = soup.find_all('table', class_='resultsarchive-table')

    with open(csv_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for table in data:
            for row in table.find_all('tr')[1:]:
                data = func(row)
                writer.writerow(data)

def drivers_standings(row):
    position = re.findall(r'<td class="dark">(.*?)</td>', str(row))[0].strip()
    driver_name = re.findall(r'<span class="hide-for-tablet">(.*?)</span>', str(row))[0]
    driver_surname = re.findall(r'<span class="hide-for-mobile">(.*?)</span>', str(row))[0].strip()
    nationality = re.findall(r'<td class="dark semi-bold uppercase">(.*?)</td>', str(row))[0].strip()
    car = re.findall(r'.html">(.*?)</a>', str(row))[0].strip()
    points = re.findall(r'<td class="dark bold">(.*?)</td>', str(row))[0].strip()

    return [position, f"{driver_name} {driver_surname}", nationality, car, points]

def races(row):
    grandprix = re.findall(r'html">\n                        (.*?)\n                    </a>', str(row))[0].strip()
    date = re.findall(r'<td class="dark hide-for-mobile">(.*?)</td>', str(row))[0]
    winner_name = re.findall(r'<span class="hide-for-tablet">(.*?)</span>', str(row))[0]
    winner_surname = re.findall(r'<span class="hide-for-mobile">(.*?)</span>', str(row))[0]
    car = re.findall(r'<td class="semi-bold uppercase">(.*?)</td>', str(row))[0]
    laps = re.findall(r'<td class="bold hide-for-mobile">(.*?)</td>', str(row))[0]

    return [grandprix, date, f"{winner_surname}", car, laps]

def teams_standings(row):
    position = re.findall(r'<td class="dark">(.*?)</td>', str(row))[0].strip()
    team = re.findall(r'.html">(.*?)</a>\n</td>\n', str(row))[0].strip()
    points = re.findall(r'<td class="dark bold">(.*?)</td>', str(row))[0].strip()

    return [position, team, points]

def fastest_laps(row):
    grandprix = re.findall(r'<td class="width30 dark">(.*?)</td>', str(row))[0]
    driver_surname = re.findall(r'<span class="hide-for-mobile">(.*?)</span>', str(row))[0]
    team = re.findall(r'<td class="width25 semi-bold uppercase">(.*?)</td>', str(row))[0]
    lap_time = re.findall(r'<td class="dark bold">(.*?)</td>', str(row))[0]

    return [grandprix, f"{driver_surname}", team, lap_time]

def main():
    csv_file_prefix = "f1_results_"
    year = input(f"Enter year: ").strip()

    URL_DRIVERS = f"https://www.formula1.com/en/results.html/{year}/drivers.html"
    URL_RACES = f"https://www.formula1.com/en/results.html/{year}/races.html"
    URL_TEAMS = f"https://www.formula1.com/en/results.html/{year}/team.html"
    URL_FASTEST_LAPS = f"https://www.formula1.com/en/results.html/{year}/fastest-laps.html"

    csv_file_name = f"{csv_file_prefix}{year}_drivers.csv"
    parse_url(URL_DRIVERS, drivers_standings, csv_file_name)

    csv_file_name = f"{csv_file_prefix}{year}_races.csv"
    parse_url(URL_RACES, races, csv_file_name)

    csv_file_name = f"{csv_file_prefix}{year}_teams.csv"
    parse_url(URL_TEAMS, teams_standings, csv_file_name)

    csv_file_name = f"{csv_file_prefix}{year}_fastest_laps.csv"
    parse_url(URL_FASTEST_LAPS, fastest_laps, csv_file_name)


if __name__ == '__main__':
    main()
