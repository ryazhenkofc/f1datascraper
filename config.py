class Config:
    BASE_URL_F1 = "https://www.formula1.com/en/results.html/"
    BASE_URL_F1A = "https://www.f1academy.com/"
    BASE_URL_F2 = "https://www.fiaformula2.com/"
    BASE_URL_F3 = "https://www.fiaformula3.com/"
    BASE_URL_FE = "https://www.fiaformulae.com/"

    DRIVER_PATTERNS_F1 = {
        "driver": r'<a href="/en/drivers/.*?">(.*?)</a>',
        "team": r'<a href="/en/teams/.*?">(.*?)</a>',
        "points": r'<td class="dark bold">(.*?)</td>',
    }

    RACE_PATTERNS_F1 = {
        "grand_prix": r'<a href="/en/results.html/(.*?)/races.html">.*?</a>',
        "date": r'<td class="dark hide-for-mobile">(.*?)</td>',
        "winner": r'<a href="/en/drivers/.*?">(.*?)</a>',
        "car": r'<a href="/en/teams/.*?">(.*?)</a>',
        "laps": r'<td class="bold">(.*?)</td>',
        "time": r'<td class="dark bold">(.*?)</td>',
    }

    TEAM_PATTERNS_F1 = {
        "team": r'<a href="/en/teams/.*?">(.*?)</a>',
        "points": r'<td class="dark bold">(.*?)</td>',
    }

    FASTEST_LAP_PATTERNS_F1 = {
        "grand_prix": r'<a href="/en/results.html/(.*?)/fastest-laps.html">.*?</a>',
        "driver": r'<a href="/en/drivers/.*?">(.*?)</a>',
        "car": r'<a href="/en/teams/.*?">(.*?)</a>',
        "time": r'<td class="dark bold">(.*?)</td>',
    }

    DRIVER_PATTERNS_F1A = {
        "driver": r'<td>(.*?)</td>',
    }

    RACE_PATTERNS_F1A = {
        "race": r'<th>(.*?)</th>',
    }

    TEAM_PATTERNS_F1A = {
        "team": r'<td>(.*?)</td>',
    }

    DRIVER_PATTERNS_F2 = {
        "driver": r'<td>(.*?)</td>',
    }

    RACE_PATTERNS_F2 = {
        "race": r'<th>(.*?)</th>',
    }

    TEAM_PATTERNS_F2 = {
        "team": r'<td>(.*?)</td>',
    }

    DRIVER_PATTERNS_F3 = {
        "driver": r'<td>(.*?)</td>',
    }

    RACE_PATTERNS_F3 = {
        "race": r'<th>(.*?)</th>',
    }

    TEAM_PATTERNS_F3 = {
        "team": r'<td>(.*?)</td>',
    }

    SEASON_IDS_FE = {
        2015: 1,
        2016: 2,
        2017: 3,
        2018: 4,
        2019: 5,
        2020: 6,
        2021: 7,
        2022: 8,
        2023: 9,
    }
