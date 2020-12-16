from time import time


def fill_tables():
    from utils.render.Bundesliga import render_table as render_b
    from utils.render.EPL import render_table as render_epl
    from utils.render.La_Liga import render_table as render_ll
    from utils.render.Ligue_1 import render_table as render_l1
    from utils.render.Serie_A import render_table as render_sa
    from utils.render.UPL import render_table as render_upl

    from utils.parsing.uk import parse_table as parse_uk
    from utils.parsing.ru import parse_table as parse_ru
    from utils.parsing.en import parse_table as parse_en

    # global parser

    url_uk = {
        'b': 'https://football24.ua/nimechchina_tables_tag50829/',
        'epl': 'https://football24.ua/angliya_tables_tag50820/',
        'll': 'https://football24.ua/ispaniya_tables_tag50823/',
        'l1': 'https://football24.ua/frantsiya_tables_tag50826/',
        'sa': 'https://football24.ua/italiya_tables_tag50822/',
        'upl': 'https://football24.ua/ukrayina_tables_tag50819/',
    }

    url_ru = {
        'b': 'https://football24.ua/ru/germanija_tables_tag50829/',
        'epl': 'https://football24.ua/ru/anglija_tables_tag50820/',
        'll': 'https://football24.ua/ru/ispaniya_tables_tag50823/',
        'l1': 'https://football24.ua/ru/frantsiya_tables_tag50826/',
        'sa': 'https://football24.ua/ru/italiya_tables_tag50822/',
        'upl': 'https://football24.ua/ru/ukrayina_tables_tag50819/',
    }

    url_en = {
        'b': 'https://int.soccerway.com/national/germany/bundesliga/20202021/regular-season/r58871/',
        'epl': 'https://int.soccerway.com/national/england/premier-league/20202021/regular-season/r59136/',
        'll': 'https://int.soccerway.com/national/spain/primera-division/20202021/regular-season/r59097/',
        'l1': 'https://int.soccerway.com/national/france/ligue-1/20202021/regular-season/r58178/',
        'sa': 'https://int.soccerway.com/national/italy/serie-a/20202021/regular-season/r59286/',
        'upl': 'https://int.soccerway.com/national/ukraine/premier-league/20202021/regular-season/r59290/',
    }

    tasks = ((url_uk, 'uk'), (url_ru, 'ru'), (url_en, 'en'))

    try:
        for url, lang in tasks:
            if lang == 'uk':
                parser = parse_uk
            elif lang == 'ru':
                parser = parse_ru
            elif lang == 'en':
                parser = parse_en

            render_b(parser(url['b']), lang)
            render_epl(parser(url['epl']), lang)
            render_ll(parser(url['ll']), lang)
            render_l1(parser(url['l1']), lang)
            render_sa(parser(url['sa']), lang)
            render_upl(parser(url['upl']), lang)
    except AttributeError:
        print('Error in fill_tables')
        fill_tables()
    else:
        print('finished filling tables')


def fill_scorers():
    from utils.render.Bundesliga import render_scorers as render_b
    from utils.render.EPL import render_scorers as render_epl
    from utils.render.La_Liga import render_scorers as render_ll
    from utils.render.Ligue_1 import render_scorers as render_l1
    from utils.render.Serie_A import render_scorers as render_sa
    from utils.render.UPL import render_scorers as render_upl

    from utils.parsing.uk import parse_scorers as parse_uk
    from utils.parsing.uk import parse_scorers_fr as parse_fr_uk
    from utils.parsing.ru import parse_scorers as parse_ru
    from utils.parsing.ru import parse_scorers_fr as parse_fr_ru
    from utils.parsing.en import parse_scorers as parse_en
    from utils.parsing.en import parse_scorers_uk as parse_uk_en

    # global parser
    # global parser_fr
    # global parser_uk

    url_uk = {

        'b': 'https://football24.ua/nimechchina_forwards_tag50829/',
        'epl': 'https://football24.ua/angliya_202021_forwards_tag50820/',
        'll': 'https://football24.ua/ispaniya_202021_forwards_tag50823/',
        'l1': 'https://www.ua-football.com/ua/foreign/france/scorers',
        'sa': 'https://football24.ua/italiya_201920_forwards_tag50822/',
        'upl': 'https://football24.ua/ukrayina_forwards_tag50819/',
    }

    url_ru = {
        'b': 'https://football24.ua/ru/germanija_forwards_tag50829/',
        'epl': 'https://football24.ua/ru/anglija_forwards_tag50820/',
        'll': 'https://football24.ua/ru/ispanija_forwards_tag50823/',
        'l1': 'https://www.ua-football.com/foreign/france/scorers',
        'sa': 'https://football24.ua/ru/italija_forwards_tag50822/',
        'upl': 'https://football24.ua/ru/ukraina_forwards_tag50819/',
    }

    url_en = {
        'b': 'https://www.bbc.com/sport/football/german-bundesliga/top-scorers',
        'epl': 'https://www.bbc.com/sport/football/premier-league/top-scorers',
        'll': 'https://www.bbc.com/sport/football/spanish-la-liga/top-scorers',
        'l1': 'https://www.bbc.com/sport/football/french-ligue-one/top-scorers',
        'sa': 'https://www.bbc.com/sport/football/italian-serie-a/top-scorers',
        'upl': 'https://www.eurosport.com/football/ukrainian-premier-league/2020-2021/standingperson.shtml',
    }

    tasks = ((url_uk, 'uk'), (url_ru, 'ru'), (url_en, 'en'))

    try:
        for url, lang in tasks:
            if lang == 'uk':
                parser_fr = parse_fr_uk
                parser_uk = parse_uk
                parser = parse_uk
            elif lang == 'ru':
                parser_fr = parse_fr_ru
                parser_uk = parse_ru
                parser = parse_ru
            elif lang == 'en':
                parser_fr = parse_en
                parser_uk = parse_uk_en
                parser = parse_en

            render_b(parser(url['b']), lang)
            render_epl(parser(url['epl']), lang)
            render_ll(parser(url['ll']), lang)
            render_l1(parser_fr(url['l1']), lang)
            render_sa(parser(url['sa']), lang)
            render_upl(parser_uk(url['upl']), lang)
    except AttributeError:
        print('Error in fill_scorers')
        fill_scorers()
    else:
        print('finished filling scorers')


def fill_assists():
    from utils.render.Bundesliga import render_assists as render_b
    from utils.render.EPL import render_assists as render_epl
    from utils.render.La_Liga import render_assists as render_ll
    from utils.render.Ligue_1 import render_assists as render_l1
    from utils.render.Serie_A import render_assists as render_sa
    from utils.render.UPL import render_assists as render_upl

    from utils.parsing.uk import parse_assists as parse_uk
    from utils.parsing.uk import parse_assists_fr as parse_fr_uk
    from utils.parsing.ru import parse_assists as parse_ru
    from utils.parsing.ru import parse_assists_fr as parse_fr_ru
    from utils.parsing.en import parse_assists as parse_en

    # global parser
    # global parser_fr

    url_uk = {

        'b': 'https://football24.ua/nimechchina_202021_goalassists_tag50829/',
        'epl': 'https://football24.ua/angliya_202021_goalassists_tag50820/',
        'll': 'https://football24.ua/ispaniya_202021_goalassists_tag50823/',
        'l1': 'https://www.ua-football.com/ua/foreign/france/assistants',
        'sa': 'https://football24.ua/italiya_202021_goalassists_tag50822/',
        'upl': 'https://football24.ua/ukrayina_202021_goalassists_tag50819/',
    }

    url_ru = {
        'b': 'https://football24.ua/ru/germanija_goalassists_tag50829/',
        'epl': 'https://football24.ua/ru/anglija_goalassists_tag50820/',
        'll': 'https://football24.ua/ru/ispanija_goalassists_tag50823/',
        'l1': 'https://www.ua-football.com/foreign/france/assistants',
        'sa': 'https://football24.ua/ru/italija_goalassists_tag50822/',
        'upl': 'https://football24.ua/ru/ukraina_goalassists_tag50819/',
    }

    url_en = {
        'b': 'https://www.bbc.com/sport/football/german-bundesliga/top-scorers/assists',
        'epl': 'https://www.bbc.com/sport/football/premier-league/top-scorers/assists',
        'll': 'https://www.bbc.com/sport/football/spanish-la-liga/top-scorers/assists',
        'l1': 'https://www.bbc.com/sport/football/french-ligue-one/top-scorers/assists',
        'sa': 'https://www.bbc.com/sport/football/italian-serie-a/top-scorers/assists',
        # 'upl': 'https://www.eurosport.com/football/ukrainian-premier-league/2020-2021/standingperson.shtml',
    }

    tasks = ((url_uk, 'uk'), (url_ru, 'ru'), (url_en, 'en'))

    try:
        for url, lang in tasks:
            if lang == 'uk':
                parser_fr = parse_fr_uk
                parser = parse_uk
            elif lang == 'ru':
                parser_fr = parse_fr_ru
                parser = parse_ru
            elif lang == 'en':
                parser_fr = parse_en
                parser = parse_en

            render_b(parser(url['b']), lang)
            render_epl(parser(url['epl']), lang)
            render_ll(parser(url['ll']), lang)
            render_l1(parser_fr(url['l1']), lang)
            render_sa(parser(url['sa']), lang)
            if lang != 'en':
                render_upl(parser(url['upl']), lang)
    except AttributeError:
        print('Error in fill_assists')
        fill_assists()
    else:
        print('finished filling assists')


from utils.db_api import db
from datetime import datetime


def fill_data_matches(match: dict, lang: str, liga: str):
    if match['time'] in ['Скасовано', 'Отменен', 'Canceled']:
        db.insert_matches('matches',
                  {
                      'team_1': match['team 1'],
                      'team_2': match['team 2'],
                      'liga': liga,
                      'lang': lang,
                      'is_canceled': True
                  })

    elif match['time'] != 'FT' and len(match['time']) > 2:
        if match['time'][2] != '-':
            time = match['time'].split(':')
            db.insert_matches('matches',
                      {
                          'time': datetime(int(match['year']), int(match['month']), int(match['day']),
                                           int(time[0]), int(time[1])),
                          'team_1': match['team 1'],
                          'team_2': match['team 2'],
                          'liga': liga,
                          'lang': lang,
                          'is_canceled': False
                      })


def fill_matches():
    from utils.render.Bundesliga import render_matches as render_b
    from utils.render.EPL import render_matches as render_epl
    from utils.render.La_Liga import render_matches as render_ll
    from utils.render.Ligue_1 import render_matches as render_l1
    from utils.render.Serie_A import render_matches as render_sa
    from utils.render.UPL import render_matches as render_upl

    from utils.parsing.uk import parse_matches as parse_uk
    from utils.parsing.ru import parse_matches as parse_ru
    from utils.parsing.en import parse_matches as parse_en

    # global parser

    url_uk = {

        'b': 'https://football24.ua/nimechchina_games_tag50829/',
        'epl': 'https://football24.ua/angliya_games_tag50820/',
        'll': 'https://football24.ua/ispaniya_games_tag50823/',
        'l1': 'https://football24.ua/frantsiya_games_tag50826/',
        'sa': 'https://football24.ua/italiya_games_tag50822/',
        'upl': 'https://football24.ua/ukrayina_games_tag50819/',
    }

    url_ru = {
        'b': 'https://football24.ua/ru/germanija_games_tag50829/',
        'epl': 'https://football24.ua/ru/anglija_games_tag50820/',
        'll': 'https://football24.ua/ru/ispanija_games_tag50823/',
        'l1': 'https://football24.ua/ru/francija_games_tag50826/',
        'sa': 'https://football24.ua/ru/italija_games_tag50822/',
        'upl': 'https://football24.ua/ru/ukraina_games_tag50819/',
    }

    url_en = {
        'b': 'https://int.soccerway.com/national/germany/bundesliga/20202021/regular-season/r58871/',
        'epl': 'https://int.soccerway.com/national/england/premier-league/20202021/regular-season/r59136/',
        'll': 'https://int.soccerway.com/national/spain/primera-division/20202021/regular-season/r59097/',
        'l1': 'https://int.soccerway.com/national/france/ligue-1/20202021/regular-season/r58178/',
        'sa': 'https://int.soccerway.com/national/italy/serie-a/20202021/regular-season/r59286/',
        'upl': 'https://int.soccerway.com/national/ukraine/premier-league/20202021/regular-season/r59290/',
    }

    tasks = ((url_uk, 'uk'), (url_ru, 'ru'), (url_en, 'en'))
    try:

        for url, lang in tasks:
            if lang == 'uk':
                parser = parse_uk
            elif lang == 'ru':
                parser = parse_ru
            elif lang == 'en':
                parser = parse_en

            data_b = parser(url['b'])
            render_b(data_b, lang)
            for match in data_b:
                if isinstance(match, dict):
                    fill_data_matches(match, lang, 'b')

            data_epl = parser(url['epl'])
            render_epl(data_epl, lang)
            for match in data_epl:
                if isinstance(match, dict):
                    fill_data_matches(match, lang, 'epl')

            data_ll = parser(url['ll'])
            render_ll(data_ll, lang)
            for match in data_ll:
                if isinstance(match, dict):
                    fill_data_matches(match, lang, 'll')

            data_l1 = parser(url['l1'])
            render_l1(data_l1, lang)
            for match in data_l1:
                if isinstance(match, dict):
                    fill_data_matches(match, lang, 'l1')

            data_sa = parser(url['sa'])
            render_sa(data_sa, lang)
            for match in data_sa:
                if isinstance(match, dict):
                    fill_data_matches(match, lang, 'sa')

            data_upl = parser(url['upl'])
            render_upl(data_upl, lang)
            for match in data_upl:
                if isinstance(match, dict):
                    fill_data_matches(match, lang, 'upl')
    except AttributeError:
        print('Error in fill_matches')
        fill_matches()
    else:
        print('finished filling matches')


import threading


def fill_all():
    task_tables = threading.Thread(target=fill_tables)
    task_scorers = threading.Thread(target=fill_scorers)
    task_assists = threading.Thread(target=fill_assists)
    # task_matches = threading.Thread(target=fill_matches)
    task_tables.start()
    task_scorers.start()
    task_assists.start()
    fill_matches()

    task_tables.join()
    task_scorers.join()
    task_assists.join()


if __name__ == '__main__':
    beg = time()
    fill_all()
    print(time() - beg)
