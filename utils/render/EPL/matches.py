from PIL import Image, ImageDraw, ImageFont
from datetime import date

from utils.parsing.en import parse_matches


def _fix_team_name(team_name):
    cur_name = team_name.split()
    if cur_name[0] in ['Шеффілд', 'Шеффилд', 'Sheffield',
                       'Tottenham', 'Wolverhampton', 'Newcastle', 'Leeds', 'Brighton']:
        cur_name = cur_name[0]
        return cur_name
    elif cur_name[0] in ['West'] and cur_name[1] in ['Ham', 'Bromwich']:
        cur_name = ' '.join(cur_name[0:2])
        return cur_name
    return team_name


def render_matches(matches: list, lang: str):
    back_g = Image.open(r'C:/mpr/football-bot/utils/render/EPL/bg/matches/Next matches EPL.jpg')
    draw_text = ImageDraw.Draw(back_g)

    font = ImageFont.truetype(r"C:\mpr\aiogram-bot\utils\render\Roboto-Regular.ttf", size=36)
    title_font = ImageFont.truetype(r"C:\mpr\aiogram-bot\utils\render\Roboto-Regular.ttf", size=26)
    top_font = ImageFont.truetype(r"C:\mpr\aiogram-bot\utils\render\Roboto-Regular.ttf", size=48)

    # print(matches)
    draw_text.text((540, 50), matches[0], anchor='mm', font=top_font, fill='white')

    if lang == 'en':
        canceled_text = 'Canceled'
        weekdays = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday'
        }

        months = {
            '1': 'January',
            '2': 'February',
            '3': 'March',
            '4': 'April',
            '5': 'May',
            '6': 'June',
            '7': 'July',
            '8': 'August',
            '9': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December'
        }

        logos = {
            'Tottenham': r'C:/mpr/football-bot/utils/render/EPL/logo/Tottenham.png',
            'Liverpool': r'C:/mpr/football-bot/utils/render/EPL/logo/Liverpool.png',
            'Chelsea': r'C:/mpr/football-bot/utils/render/EPL/logo/Chelsea.png',
            'Leicester City': r'C:/mpr/football-bot/utils/render/EPL/logo/Leicester.png',
            'Southampton': r'C:/mpr/football-bot/utils/render/EPL/logo/Southampon.png',
            'Manchester United': r'C:/mpr/football-bot/utils/render/EPL/logo/Manchester United.png',
            'Manchester City': r'C:/mpr/football-bot/utils/render/EPL/logo/Manchester City.png',
            'West Ham': r'C:/mpr/football-bot/utils/render/EPL/logo/West Ham.png',
            'Everton': r'C:/mpr/football-bot/utils/render/EPL/logo/Everton.png',
            'Wolverhampton': r'C:/mpr/football-bot/utils/render/EPL/logo/wolverhampton.png',
            'Crystal Palace': r'C:/mpr/football-bot/utils/render/EPL/logo/Crystal Palace.png',
            'Aston Villa': r'C:/mpr/football-bot/utils/render/EPL/logo/Aston Villa.png',
            'Newcastle': r'C:/mpr/football-bot/utils/render/EPL/logo/Newcastle United.png',
            'Leeds': r'C:/mpr/football-bot/utils/render/EPL/logo/Leeds United.png',
            'Arsenal': r'C:/mpr/football-bot/utils/render/EPL/logo/Arsenal.png',
            'Brighton': r'C:/mpr/football-bot/utils/render/EPL/logo/Brighton.png',
            'Fulham': r'C:/mpr/football-bot/utils/render/EPL/logo/Fulham.png',
            'Burnley': r'C:/mpr/football-bot/utils/render/EPL/logo/Burnley.png',
            'West Bromwich': r'C:/mpr/football-bot/utils/render/EPL/logo/West Bromwich.png',
            'Sheffield': r'C:/mpr/football-bot/utils/render/EPL/logo/Sheffield United.png'
        }
    elif lang == 'ru':
        canceled_text = 'Отменен'
        weekdays = {
            0: 'Понедельник',
            1: 'Вторник',
            2: 'Среда',
            3: 'Четверг',
            4: 'Пятница',
            5: 'Суббота',
            6: 'Воскресенье'
        }

        months = {
            '1': 'января',
            '2': 'февраля',
            '3': 'марта',
            '4': 'апреля',
            '5': 'мая',
            '6': 'июня',
            '7': 'июля',
            '8': 'августа',
            '9': 'сентября',
            '10': 'октября',
            '11': 'ноября',
            '12': 'декабря'
        }

        logos = {
            'Тоттенхэм': r'C:/mpr/football-bot/utils/render/EPL/logo/Tottenham.png',
            'Ливерпуль': r'C:/mpr/football-bot/utils/render/EPL/logo/Liverpool.png',
            'Челси': r'C:/mpr/football-bot/utils/render/EPL/logo/Chelsea.png',
            'Лестер Сити': r'C:/mpr/football-bot/utils/render/EPL/logo/Leicester.png',
            'Саутгемптон': r'C:/mpr/football-bot/utils/render/EPL/logo/Southampon.png',
            'Манчестер Юнайтед': r'C:/mpr/football-bot/utils/render/EPL/logo/Manchester United.png',
            'Манчестер Сити': r'C:/mpr/football-bot/utils/render/EPL/logo/Manchester City.png',
            'Вест Хэм': r'C:/mpr/football-bot/utils/render/EPL/logo/West Ham.png',
            'Эвертон': r'C:/mpr/football-bot/utils/render/EPL/logo/Everton.png',
            'Вулверхэмптон': r'C:/mpr/football-bot/utils/render/EPL/logo/wolverhampton.png',
            'Кристал Пэлас': r'C:/mpr/football-bot/utils/render/EPL/logo/Crystal Palace.png',
            'Астон Вилла': r'C:/mpr/football-bot/utils/render/EPL/logo/Aston Villa.png',
            'Ньюкасл': r'C:/mpr/football-bot/utils/render/EPL/logo/Newcastle United.png',
            'Лидс': r'C:/mpr/football-bot/utils/render/EPL/logo/Leeds United.png',
            'Арсенал': r'C:/mpr/football-bot/utils/render/EPL/logo/Arsenal.png',
            'Брайтон': r'C:/mpr/football-bot/utils/render/EPL/logo/Brighton.png',
            'Фулхэм': r'C:/mpr/football-bot/utils/render/EPL/logo/Fulham.png',
            'Бернли': r'C:/mpr/football-bot/utils/render/EPL/logo/Burnley.png',
            'Вест Бромвич': r'C:/mpr/football-bot/utils/render/EPL/logo/West Bromwich.png',
            'Шеффилд': r'C:/mpr/football-bot/utils/render/EPL/logo/Sheffield United.png'
        }
    else:
        canceled_text = 'Скасовано'
        weekdays = {
            0: 'Понеділок',
            1: 'Вівторок',
            2: 'Середа',
            3: 'Четвер',
            4: 'П\'ятниця',
            5: 'Субота',
            6: 'Неділя'
        }

        months = {
            '1': 'січня',
            '2': 'лютого',
            '3': 'березня',
            '4': 'квітня',
            '5': 'травня',
            '6': 'червня',
            '7': 'липня',
            '8': 'серпня',
            '9': 'вересня',
            '10': 'жовтня',
            '11': 'листопада',
            '12': 'грудня'
        }

        logos = {
            'Тоттенхем': r'C:/mpr/football-bot/utils/render/EPL/logo/Tottenham.png',
            'Ліверпуль': r'C:/mpr/football-bot/utils/render/EPL/logo/Liverpool.png',
            'Челсі': r'C:/mpr/football-bot/utils/render/EPL/logo/Chelsea.png',
            'Лестер Сіті': r'C:/mpr/football-bot/utils/render/EPL/logo/Leicester.png',
            'Саутгемптон': r'C:/mpr/football-bot/utils/render/EPL/logo/Southampon.png',
            'Манчестер Юнайтед': r'C:/mpr/football-bot/utils/render/EPL/logo/Manchester United.png',
            'Манчестер Сіті': r'C:/mpr/football-bot/utils/render/EPL/logo/Manchester City.png',
            'Вест Хем': r'C:/mpr/football-bot/utils/render/EPL/logo/West Ham.png',
            'Евертон': r'C:/mpr/football-bot/utils/render/EPL/logo/Everton.png',
            'Вулверхемптон': r'C:/mpr/football-bot/utils/render/EPL/logo/wolverhampton.png',
            'Крістал Пелас': r'C:/mpr/football-bot/utils/render/EPL/logo/Crystal Palace.png',
            'Астон Вілла': r'C:/mpr/football-bot/utils/render/EPL/logo/Aston Villa.png',
            'Ньюкасл': r'C:/mpr/football-bot/utils/render/EPL/logo/Newcastle United.png',
            'Лідс': r'C:/mpr/football-bot/utils/render/EPL/logo/Leeds United.png',
            'Арсенал': r'C:/mpr/football-bot/utils/render/EPL/logo/Arsenal.png',
            'Брайтон': r'C:/mpr/football-bot/utils/render/EPL/logo/Brighton.png',
            'Фулхем': r'C:/mpr/football-bot/utils/render/EPL/logo/Fulham.png',
            'Бернлі': r'C:/mpr/football-bot/utils/render/EPL/logo/Burnley.png',
            'Вест Бромвіч': r'C:/mpr/football-bot/utils/render/EPL/logo/West Bromwich.png',
            'Шеффілд': r'C:/mpr/football-bot/utils/render/EPL/logo/Sheffield United.png'
        }

    cur_weekday = None
    pos_y = 50 + draw_text.textsize(matches[0], font=top_font)[1]
    for match in matches[1:]:
        weekday = weekdays[date(int(match['year']), int(match['month']), int(match['day'])).weekday()]
        if cur_weekday != weekday:
            cur_weekday = weekday
            pos_y += 70
            title = cur_weekday + ', ' + match['day'] + ' ' + months[match['month']] + ' ' + match['year']
            draw_text.text((540, pos_y), title, anchor='mm', font=title_font, fill='white')
            pos_y += draw_text.textsize(title, font=title_font)[1]

        pos_y += 20
        text = match['time'] if match['time'] != 'FT' else match['score']
        draw_text.text((540, pos_y), text, anchor='mm', font=font if text != canceled_text else title_font,
                       fill='white')
        team_1 = _fix_team_name(match['team 1'])
        draw_text.text((380, pos_y), team_1, anchor='rm', font=font, fill='white')
        logo_1 = Image.open(logos[team_1])
        back_g.paste(logo_1, (400, pos_y - 18), logo_1)
        team_2 = _fix_team_name(match['team 2'])
        draw_text.text((700, pos_y), team_2, anchor='lm', font=font, fill='white')
        logo_2 = Image.open(logos[team_2])
        back_g.paste(logo_2, (640, pos_y - 18), logo_2)
        pos_y += draw_text.textsize(text, font=font)[1]

    back_g.save(rf'C:\mpr\football-bot\data\matches\epl_{lang}.jpg')


if __name__ == '__main__':
    render_matches(
        parse_matches('https://int.soccerway.com/national/england/premier-league/20202021/regular-season/r59136/'),
        'en')
