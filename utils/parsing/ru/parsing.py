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
    user = fake_useragent.UserAgent().random
    HEADERS = {
        'User-Agent': user
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')
    block = soup.find('table', class_='standings-table')
    block = block.find('tbody')
    rows = block.find_all('tr')
    teams = list()
    for row in rows:
        values = row.findAll('td')
        values = [value.get_text(strip=True) for value in values]
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
            'points': values[9]
        })
    return teams


def parse_scorers(URL, top=10) -> list:
    soup = get_html(URL)
    block = soup.find('table', class_='teams-table')
    block = block.find('tbody')
    rows = block.find_all('tr')
    players = list()
    for row in rows:
        values = row.find_all('td')
        values = [value.get_text(strip=True) for value in values]
        values[2] = values[2].replace('\n', ' ')
        values[3] = values[3][:int(len(values[3]) / 2)]
        if len(values[2].split()) > 1:
            values[2] = values[2] if len(values[2].split()[1].split('-')) == 1 else values[2].split()[1]
        players.append({
            'pos': values[0],
            'name': values[2],
            'team': values[3],
            'goals': values[4],
            'penalty': values[5],
            'played': values[6]
        })
    return players[:top]


# def parse_scorers_fr(URL, top=10) -> list:
#     soup = get_html(URL)
#     block = soup.find('table', class_='bombTable w-100')
#     block = block.find('tbody')
#     rows = block.find_all('tr')
#     players = list()
#     for row in rows:
#         values = row.find_all('td')
#         values = [value.get_text(strip=True) for value in values]
#         values[5] = re.findall(r'(\d+) *.*', values[5])[0]
#         if len(values[2].split()) > 1:
#             values[2] = values[2] if len(values[2].split()[1].split('-')) == 1 else values[2].split()[1]
#         players.append({
#             'pos': values[0],
#             'name': values[2],
#             'team': values[4],
#             'goals': values[5],
#             'played': values[6]
#         })
#     return players[:top]


def parse_scorers_fr(URL, top=10) -> list:
    soup = get_html(URL)
    block = soup.find('table', class_='bombTable w-100')
    block = block.find('tbody')
    rows = block.find_all('tr')
    players = list()
    for row in rows:
        values = row.find_all('td')
        values = [value.get_text(strip=True) for value in values]
        values[5] = re.findall(r'(\d+) *.*', values[5])[0]
        if len(values[2].split()) > 1:
            values[2] = values[2] if len(values[2].split()[1].split('-')) == 1 else values[2].split()[1]
        players.append({
            'pos': values[0],
            'name': values[2],
            'team': values[4],
            'goals': values[5],
            'played': values[6]
        })
    return players[:top]


def parse_assists(URL, top=10) -> list:
    soup = get_html(URL)
    block = soup.find('table', class_='teams-table')
    block = block.find('tbody')
    rows = block.find_all('tr')
    players = list()
    for row in rows:
        values = row.find_all('td')
        values = [value.get_text(strip=True) for value in values]
        values[2] = values[2].replace('\n', ' ')
        if len(values[2].split()) > 1:
            values[2] = values[2] if len(values[2].split()[1].split('-')) == 1 else values[2].split()[1]
        players.append({
            'pos': values[0],
            'name': values[2],
            'team': values[3],
            'assists': values[4],
            'played': values[5]
        })
    return players[:top]


def parse_assists_fr(URL, top=10) -> list:
    soup = get_html(URL)
    block = soup.find('div', class_='row')
    # block = block.find('tbody')
    rows = block.find_all('tr')
    players = list()
    for row in rows:
        values = row.find_all('td')
        values = [value.get_text(strip=True) for value in values]
        if len(values) > 1 and values[0] != '#':
            if len(values[1].split()) > 1:
                values[1] = values[1] if len(values[1].split()[1].split('-')) == 1 else values[1].split()[1]
            players.append({
                'pos': values[0],
                'name': values[1],
                'team': values[2],
                'assists': values[3],
                'played': values[4]
            })
    return players[:top]


def parse_matches(URL) -> list:
    soup = get_html(URL)
    block = soup.find('table', class_='calendar-table')
    block = block.find('tbody')
    rows = block.find_all('tr')
    matches = [soup.find('ul', class_='select-tour').find('a').get_text(strip=True)]
    date = None
    for row in rows:
        values = row.find_all('td')
        values = [value.get_text(strip=True) for value in values]
        if len(values) == 1:
            date = values[0]
            date = date.split('.')
        elif len(values) > 1:
            values[3] = values[3] if values[6] != 'live' else 'Live'
            values[3] = values[3] if values[3] != '- : -' else 'Отменен'
            values[3] = values[3] if values[3].split(':')[0][-1] != ' ' else '-'.join(values[3].split(':'))
            matches.append({
                'day': date[0],
                'month': date[1],
                'year': '20' + date[2],
                'time': values[3],
                'team 1': values[1],
                'team 2': values[5],
            })
    return matches


if __name__ == '__main__':
    beg = time.monotonic()
    print(parse_assists_fr('https://www.ua-football.com/foreign/france/assistants'))
    print(time.monotonic() - beg)
