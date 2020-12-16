import requests
import fake_useragent
from bs4 import BeautifulSoup
import time


def _get_photo(res_link: str) -> bytes:
    spl_link = res_link.split('/')
    spl_link[6] = '50'
    fin_link = '/'.join(spl_link)
    image_bytes = requests.get(fin_link).content
    return image_bytes


def parse_table(URL) -> list:
    user = fake_useragent.UserAgent().random
    # URL = 'https://football24.ua/ispaniya_tables_tag50823/'
    HEADERS = {
        'User-Agent': user
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')
    block = soup.find('tbody', class_='tableBodyContainer')
    rows = block.find_all('tr')
    teams = list()
    for row in rows:
        if row.get('class') != ['expandable']:
            # logo = _get_photo(row.find('img').get('src'))
            pos = row.find('span', class_='value').get_text(strip=True)
            name = row.find('span', class_='long').get_text(strip=True)
            points = row.findAll('td')
            points = [point.get_text(strip=True) for point in points]
            points = points[3:9] + points[10:11]
            teams.append({
                'logo': 0,
                'pos': pos,
                'name': name,
                'played': points[0],
                'won': points[1],
                'draw': points[2],
                'lost': points[3],
                'for': points[4],
                'against': points[5],
                'points': points[6]
            })
    return teams


if __name__ == '__main__':
    beg = time.monotonic()
    parse_table('https://www.premierleague.com/tables')
    print(time.monotonic() - beg)
