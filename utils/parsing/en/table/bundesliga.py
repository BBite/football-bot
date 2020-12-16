import requests
import fake_useragent
from bs4 import BeautifulSoup
import re

import time


def parse_table(URL) -> list:
    user = fake_useragent.UserAgent().random
    # URL = 'https://football24.ua/ispaniya_tables_tag50823/'
    HEADERS = {
        'User-Agent': user
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')
    block = soup.find('table, class_='leaguetable sortable table detailed-table)
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
            'points': values[10]
        })
    return teams


if __name__ == '__main__':
    beg = time.monotonic()
    parse_table('https://int.soccerway.com/national/germany/bundesliga/20202021/regular-season/r58871/')
    print(time.monotonic() - beg)
