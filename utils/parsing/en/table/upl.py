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
    block = soup.find('div', class_='body-content')
    block = block.find('tbody')
    rows = block.find_all('tr')
    teams = list()
    for row in rows:
        values = row.find_all('td')
        values = [value.get_text(strip=True) for value in values]
        name = re.findall(r'«(.+)» .+', values[1])[0]
        teams.append({
            'logo': 0,
            'pos': values[0],
            'name': name,
            'played': values[2],
            'won': values[3],
            'draw': values[4],
            'lost': values[5],
            'for': values[7],
            'against': values[8],
            'points': values[9]
        })
    return teams


if __name__ == '__main__':
    beg = time.monotonic()
    parse_table('https://upl.ua/en/tournaments/championship/410?id=410')
    print(time.monotonic() - beg)
