from PIL import Image, ImageDraw, ImageFont

from utils.parsing.uk import parse_table
from utils.parsing import split_table


def render_table(teams: list, lang: str):
    info_teams = split_table(teams)

    if lang == 'en':
        back_g = Image.open('C:/mpr/football_bot/utils/render/EPL/bg/table/EPL_en.jpg')
        logos = {
            'Tottenham': r'C:/mpr/football_bot/utils/render/EPL/logo/Tottenham.png',
            'Liverpool': r'C:/mpr/football_bot/utils/render/EPL/logo/Liverpool.png',
            'Chelsea': r'C:/mpr/football_bot/utils/render/EPL/logo/Chelsea.png',
            'Leicester City': r'C:/mpr/football_bot/utils/render/EPL/logo/Leicester.png',
            'Southampton': r'C:/mpr/football_bot/utils/render/EPL/logo/Southampon.png',
            'Manchester United': r'C:/mpr/football_bot/utils/render/EPL/logo/Manchester United.png',
            'Manchester City': r'C:/mpr/football_bot/utils/render/EPL/logo/Manchester City.png',
            'West Ham': r'C:/mpr/football_bot/utils/render/EPL/logo/West Ham.png',
            'Everton': r'C:/mpr/football_bot/utils/render/EPL/logo/Everton.png',
            'Wolverhampton': r'C:/mpr/football_bot/utils/render/EPL/logo/wolverhampton.png',
            'Crystal Palace': r'C:/mpr/football_bot/utils/render/EPL/logo/Crystal Palace.png',
            'Aston Villa': r'C:/mpr/football_bot/utils/render/EPL/logo/Aston Villa.png',
            'Newcastle': r'C:/mpr/football_bot/utils/render/EPL/logo/Newcastle United.png',
            'Leeds': r'C:/mpr/football_bot/utils/render/EPL/logo/Leeds United.png',
            'Arsenal': r'C:/mpr/football_bot/utils/render/EPL/logo/Arsenal.png',
            'Brighton': r'C:/mpr/football_bot/utils/render/EPL/logo/Brighton.png',
            'Fulham': r'C:/mpr/football_bot/utils/render/EPL/logo/Fulham.png',
            'Burnley': r'C:/mpr/football_bot/utils/render/EPL/logo/Burnley.png',
            'West Bromwich': r'C:/mpr/football_bot/utils/render/EPL/logo/West Bromwich.png',
            'Sheffield': r'C:/mpr/football_bot/utils/render/EPL/logo/Sheffield United.png'
        }
    elif lang == 'ru':
        back_g = Image.open('C:/mpr/football_bot/utils/render/EPL/bg/table/EPL_ru.jpg')
        logos = {
            'Тоттенхэм': r'C:/mpr/football_bot/utils/render/EPL/logo/Tottenham.png',
            'Ливерпуль': r'C:/mpr/football_bot/utils/render/EPL/logo/Liverpool.png',
            'Челси': r'C:/mpr/football_bot/utils/render/EPL/logo/Chelsea.png',
            'Лестер Сити': r'C:/mpr/football_bot/utils/render/EPL/logo/Leicester.png',
            'Саутгемптон': r'C:/mpr/football_bot/utils/render/EPL/logo/Southampon.png',
            'Манчестер Юнайтед': r'C:/mpr/football_bot/utils/render/EPL/logo/Manchester United.png',
            'Манчестер Сити': r'C:/mpr/football_bot/utils/render/EPL/logo/Manchester City.png',
            'Вест Хэм': r'C:/mpr/football_bot/utils/render/EPL/logo/West Ham.png',
            'Эвертон': r'C:/mpr/football_bot/utils/render/EPL/logo/Everton.png',
            'Вулверхэмптон': r'C:/mpr/football_bot/utils/render/EPL/logo/wolverhampton.png',
            'Кристал Пэлас': r'C:/mpr/football_bot/utils/render/EPL/logo/Crystal Palace.png',
            'Астон Вилла': r'C:/mpr/football_bot/utils/render/EPL/logo/Aston Villa.png',
            'Ньюкасл': r'C:/mpr/football_bot/utils/render/EPL/logo/Newcastle United.png',
            'Лидс': r'C:/mpr/football_bot/utils/render/EPL/logo/Leeds United.png',
            'Арсенал': r'C:/mpr/football_bot/utils/render/EPL/logo/Arsenal.png',
            'Брайтон': r'C:/mpr/football_bot/utils/render/EPL/logo/Brighton.png',
            'Фулхэм': r'C:/mpr/football_bot/utils/render/EPL/logo/Fulham.png',
            'Бернли': r'C:/mpr/football_bot/utils/render/EPL/logo/Burnley.png',
            'Вест Бромвич': r'C:/mpr/football_bot/utils/render/EPL/logo/West Bromwich.png',
            'Шеффилд': r'C:/mpr/football_bot/utils/render/EPL/logo/Sheffield United.png'
        }
    else:
        back_g = Image.open('C:/mpr/football_bot/utils/render/EPL/bg/table/EPL_ua.jpg')
        logos = {
            'Тоттенхем': r'C:/mpr/football_bot/utils/render/EPL/logo/Tottenham.png',
            'Ліверпуль': r'C:/mpr/football_bot/utils/render/EPL/logo/Liverpool.png',
            'Челсі': r'C:/mpr/football_bot/utils/render/EPL/logo/Chelsea.png',
            'Лестер Сіті': r'C:/mpr/football_bot/utils/render/EPL/logo/Leicester.png',
            'Саутгемптон': r'C:/mpr/football_bot/utils/render/EPL/logo/Southampon.png',
            'Манчестер Юнайтед': r'C:/mpr/football_bot/utils/render/EPL/logo/Manchester United.png',
            'Манчестер Сіті': r'C:/mpr/football_bot/utils/render/EPL/logo/Manchester City.png',
            'Вест Хем': r'C:/mpr/football_bot/utils/render/EPL/logo/West Ham.png',
            'Евертон': r'C:/mpr/football_bot/utils/render/EPL/logo/Everton.png',
            'Вулверхемптон': r'C:/mpr/football_bot/utils/render/EPL/logo/wolverhampton.png',
            'Крістал Пелас': r'C:/mpr/football_bot/utils/render/EPL/logo/Crystal Palace.png',
            'Астон Вілла': r'C:/mpr/football_bot/utils/render/EPL/logo/Aston Villa.png',
            'Ньюкасл': r'C:/mpr/football_bot/utils/render/EPL/logo/Newcastle United.png',
            'Лідс': r'C:/mpr/football_bot/utils/render/EPL/logo/Leeds United.png',
            'Арсенал': r'C:/mpr/football_bot/utils/render/EPL/logo/Arsenal.png',
            'Брайтон': r'C:/mpr/football_bot/utils/render/EPL/logo/Brighton.png',
            'Фулхем': r'C:/mpr/football_bot/utils/render/EPL/logo/Fulham.png',
            'Бернлі': r'C:/mpr/football_bot/utils/render/EPL/logo/Burnley.png',
            'Вест Бромвіч': r'C:/mpr/football_bot/utils/render/EPL/logo/West Bromwich.png',
            'Шеффілд': r'C:/mpr/football_bot/utils/render/EPL/logo/Sheffield United.png'
        }

    draw_text = ImageDraw.Draw(back_g)

    for pos, name in enumerate(info_teams[2]):
        cur_name = name.split()
        if cur_name[0] in ['Шеффілд', 'Шеффилд', 'Sheffield',
                           'Tottenham', 'Wolverhampton', 'Newcastle', 'Leeds', 'Brighton']:
            cur_name = cur_name[0]
            info_teams[2][pos] = cur_name
        elif cur_name[0] in ['West'] and cur_name[1] in ['Ham', 'Bromwich']:
            cur_name = ' '.join(cur_name[0:2])
            info_teams[2][pos] = cur_name
        logo = Image.open(logos[info_teams[2][pos]])
        back_g.paste(logo, (150, 75 + pos * 49), logo)

    font = ImageFont.truetype(r"C:\mpr\aiogram-bot\utils\render\Roboto-Regular.ttf", size=36)

    # pos
    draw_text.multiline_text((100, 71), '\n'.join(info_teams[1]), spacing=15, font=font, fill='black')
    # name
    draw_text.multiline_text((200, 71), '\n'.join(info_teams[2]), spacing=15, font=font, fill='black')
    # played
    draw_text.multiline_text((560, 71), '\n'.join(info_teams[3]), spacing=15, font=font, fill='black')
    # won
    draw_text.multiline_text((620, 71), '\n'.join(info_teams[4]), spacing=15, font=font, fill='black')
    # draw
    draw_text.multiline_text((660, 71), '\n'.join(info_teams[5]), spacing=15, font=font, fill='black')
    # lost
    draw_text.multiline_text((700, 71), '\n'.join(info_teams[6]), spacing=15, font=font, fill='black')
    # goals
    draw_text.multiline_text((770, 71), '\n'.join(info_teams[7]), spacing=15, font=font, fill='black')
    # points
    draw_text.multiline_text((900, 71), '\n'.join(info_teams[8]), spacing=15, font=font, fill='black')

    back_g.save(rf'C:\mpr\football_bot\data\tables\epl_{lang}.jpg')


if __name__ == '__main__':
    render_table(
        parse_table('https://football24.ua/angliya_tables_tag50820/'), 'uk')
