from PIL import Image, ImageDraw, ImageFont
from datetime import date

from utils.parsing.uk import parse_matches


def _fix_team_name(team_name):
    cur_name = team_name.split()
    if cur_name[0] in ['Atletico', 'Athletic', 'Celta']:
        cur_name = cur_name[0]
        return cur_name
    if (len(cur_name)) > 1:
        if cur_name[1] in ['Alavés']:
            cur_name = cur_name[1]
            return cur_name
    return team_name


def render_matches(matches: list, lang: str):
    back_g = Image.open(r'C:/mpr/football_bot/utils/render/La_Liga/bg/matches/Next matches LaLiga.jpg')
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
            'Atletico': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Athletico Madrid.png',
            'Real Sociedad': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Real Sociedad.png',
            'Villarreal': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Villarreal.png',
            'Real Madrid': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Real Madrid.png',
            'Cádiz': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Cadiz.png',
            'Sevilla': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Sevilla.png',
            'Granada': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Granada.png',
            'Real Betis': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Real Betis.png',
            'Barcelona': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Barcelona.png',
            'Elche': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Elche.png',
            'Eibar': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Eibar.png',
            'Alavés': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Alaves.png',
            'Valencia': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Valencia.png',
            'Athletic': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Athletic.png',
            'Getafe': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Getafe.png',
            'Celta': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Celta.png',
            'Levante': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Levante.png',
            'Osasuna': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Osasuna.png',
            'Real Valladolid': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Real Valladolid.png',
            'Huesca': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Huesca.png'
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
            'Атлетико': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Athletico Madrid.png',
            'Реал Сосьедад': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Real Sociedad.png',
            'Вильярреал': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Villarreal.png',
            'Реал Мадрид': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Real Madrid.png',
            'Кадис': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Cadiz.png',
            'Севилья': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Sevilla.png',
            'Гранада': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Granada.png',
            'Бетис': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Real Betis.png',
            'Барселона': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Barcelona.png',
            'Эльче': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Elche.png',
            'Эйбар': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Eibar.png',
            'Алавес': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Alaves.png',
            'Валенсия': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Valencia.png',
            'Атлетик': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Athletic.png',
            'Хетафе': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Getafe.png',
            'Сельта': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Celta.png',
            'Леванте': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Levante.png',
            'Осасуна': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Osasuna.png',
            'Вальядолид': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Real Valladolid.png',
            'Уэска': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Huesca.png'
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
            'Атлетіко': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Athletico Madrid.png',
            'Реал Сосьєдад': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Real Sociedad.png',
            'Вільяреал': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Villarreal.png',
            'Реал Мадрид': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Real Madrid.png',
            'Кадіс': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Cadiz.png',
            'Севілья': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Sevilla.png',
            'Гранада': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Granada.png',
            'Бетіс': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Real Betis.png',
            'Барселона': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Barcelona.png',
            'Ельче': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Elche.png',
            'Ейбар': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Eibar.png',
            'Алавес': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Alaves.png',
            'Валенсія': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Valencia.png',
            'Атлетік': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Athletic.png',
            'Хетафе': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Getafe.png',
            'Сельта': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Celta.png',
            'Леванте': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Levante.png',
            'Осасуна': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Osasuna.png',
            'Вальядолід': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Real Valladolid.png',
            'Уеска': r'C:/mpr/football_bot/utils/render/La_Liga/logo/Huesca.png'
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

    back_g.save(rf'C:\mpr\football_bot\data\matches\ll_{lang}.jpg')


if __name__ == '__main__':
    render_matches(
        parse_matches('https://football24.ua/ispaniya_games_tag50823/'),
        'uk')
