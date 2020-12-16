import requests
import fake_useragent
from bs4 import BeautifulSoup
import re

import time


def get_html(URL) -> BeautifulSoup:
    user = fake_useragent.UserAgent().random
    HEADERS = {
        'User-Agent': user
    }
    response = requests.get(URL, headers=HEADERS)
    return BeautifulSoup(response.content, 'lxml')


def parse_table(URL) -> list:
    soup = get_html(URL)
    block = soup.find('table', class_='leaguetable sortable table detailed-table')
    block = block.find('tbody')
    rows = block.find_all('tr')
    teams = list()
    for row in rows:
        values = row.findAll('td')
        values = [value.get_text(strip=True) for value in values]
        values[2] = row.find('td', class_='text team large-link').find('a').get('title')
        if values[2].endswith("'"):
            values[2] = values[2][:-1]
        teams.append({
            'logo': 0,
            'pos': values[0],
            'name': values[2],
            'played': values[3],
            'won': values[4],
            'draw': values[5],
            'lost': values[6],
            'for': values[7],
            'against': values[8],
            'points': values[10]
        })
    return teams


def parse_scorers(URL, top=10) -> list:
    soup = get_html(URL)
    block = soup.find('table')
    block = block.find('tbody')
    rows = block.find_all('tr')
    players = list()
    for pos, row in enumerate(rows):
        values = row.find_all('td')
        values[1] = [value.find('span').find('span').get_text(strip=True)
                     for value in values[1].find('div').find_all('div')]
        values = [value.get_text(strip=True) if i != 1 else values[1] for i, value in enumerate(values)]
        if len(values[1][0].split()) > 1:
            values[1][0] = values[1][0] if len(values[1][0].split()[1].split('-')) == 1 else values[1][0].split()[1]
        players.append({
            'pos': values[0],
            'name': values[1][0],
            'team': values[1][1],
            'goals': values[2],
            'assists': values[3],
            'played': values[4],
            'total shots': values[7],
            'goal conversion': values[8],
            'shot accuracy': values[9]
        })
    return players[:top]


def parse_scorers_uk(URL, top=10) -> list:
    soup = get_html(URL)
    block = soup.find('table', class_='standing-table')
    block = block.find('tbody')
    rows = block.find_all('tr')
    players = list()
    cur_pos = None
    for pos, row in enumerate(rows):
        values = row.find_all('td')
        values = [value.get_text(strip=True) for value in values]
        if values[0] != '-':
            cur_pos = values[0]
        values[1] = values[1][:len(values[1]) - len(values[2])]
        first_letters = re.findall(r'[A-Z]', values[1])
        words = re.split(r'[A-Z]', values[1])
        name = [first_letters[i] + words[i + 1] for i in range(len(first_letters))]
        name = ' '.join(name)
        if len(name.split()) > 1:
            name = name if len(name.split()[1].split('-')) == 1 else name.split()[1]
        players.append({
            'pos': cur_pos,
            'name': name,
            'team': values[2],
            'goals': values[4],
            'played': values[3],
        })
    return players[:top]


def parse_assists(URL, top=10) -> list:
    soup = get_html(URL)
    block = soup.find('table')
    block = block.find('tbody')
    rows = block.find_all('tr')
    players = list()
    for pos, row in enumerate(rows):
        values = row.find_all('td')
        values[1] = [value.find('span').find('span').get_text(strip=True)
                     for value in values[1].find('div').find_all('div')]
        values = [value.get_text(strip=True) if i != 1 else values[1] for i, value in enumerate(values)]
        if len(values[1][0].split()) > 1:
            values[1][0] = values[1][0] if len(values[1][0].split()[1].split('-')) == 1 else values[1][0].split()[1]
        players.append({
            'pos': values[0],
            'name': values[1][0],
            'team': values[1][1],
            'assists': values[2],
            'goals': values[3],
            'played': values[4],
            'chances created': values[5],
            'total passes': values[7],
            'passes complete': values[8],
            'pass accuracy': values[10]
        })
    return players[:top]


def parse_matches(URL) -> list:
    soup = get_html(URL)
    block = soup.find('table')
    block = block.find('tbody')
    rows = block.find_all('tr')
    matches = ['Matchweek ' + soup.find('select', class_='page-dropdown').
                                  find('option', selected='selected').get_text(strip=True)[:-2]]
    date = None
    weekday = None
    live_matches = list()
    live_flag = False
    for row in rows:
        values = row.find_all('td')
        values = [value.get_text(strip=True) for value in values]
        if live_flag:
            live_flag = False
            live_matches.append({
                'day': None,
                'month': None,
                'year': None,
                'weekday': None,
                'time': 'Live',
                'score': '-',
                'team 1': values[1].replace('\'', ''),
                'team 2': values[3].replace('\'', '')
            })
            continue
        if values == ['Live']:
            live_flag = True
            continue
        elif len(values) == 1:
            weekday, date = re.findall(r'(.+)(\d{2}/\d{2}/\d{2})', values[0])[0]
            date = date.split('/')
        elif len(values) > 1:
            values[0] = str(int(values[0][:2]) + 1) + str(values[0][2:]) if values[0] != 'FT' else 'FT'
            if values[0] != 'FT' and live_matches:
                for i in range(len(live_matches)):
                    live_matches[i]['day'] = str(int(date[0]))
                    live_matches[i]['month'] = str(int(date[1]))
                    live_matches[i]['year'] = '20' + date[2]
                    live_matches[i]['weekday'] = weekday
                matches.extend(live_matches)
                live_matches = None
            matches.append({
                'day': str(int(date[0])),
                'month': str(int(date[1])),
                'year': '20' + date[2],
                'weekday': weekday,
                'time': values[0] if values[2] != 'PSTP' else 'Canceled',
                'score': values[2],
                'team 1': values[1].replace('\'', ''),
                'team 2': values[3].replace('\'', ''),
            })
    return matches


def parse_prices(URL) -> list:
    soup = get_html(URL)
    block = soup.find('table', class_='items')
    block = block.find('tbody')
    rows = block.find_all('tr')
    prices = list()
    for row in rows:
        values = row.find_all('td')
        values = [value.get_text(strip=True) for value in values]
        if len(values) > 2:
            values[8] = values[8][:-1]
            prices.append({
                'pos': values[0],
                'name': values[3],
                'age': values[5],
                'price': values[8]
            })
    return prices


if __name__ == '__main__':
    beg = time.monotonic()
    print(parse_scorers(
        'https://www.bbc.com/sport/football/premier-league/top-scorers'))
    print(time.monotonic() - beg)
