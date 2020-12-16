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
    block = soup.find('tbody')
    rows = block.find_all('tr')
    teams = list()
    for row in rows:
        values = row.find_all('td')
        values = [value.get_text(strip=True) for value in values]
        values = values[0:6] + values[14:16]
        pos, name = re.findall(r'(\d{1,2})(\w+).*', values[0])[0]
        teams.append({
            'logo': 0,
            'pos': pos,
            'name': name,
            'played': values[2],
            'won': values[3],
            'draw': values[4],
            'lost': values[5],
            'for': values[6],
            'against': values[7],
            'points': values[1]
        })
    return teams


if __name__ == '__main__':
    beg = time.monotonic()
    parse_table('http://www.legaseriea.it/en/serie-a/league-table')
    print(time.monotonic() - beg)
