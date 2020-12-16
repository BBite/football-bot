from PIL import Image, ImageDraw, ImageFont
from datetime import date

from utils.parsing.uk import parse_matches


def _fix_team_name(team_name):
    cur_name = team_name.split()
    if cur_name[0] in 'Olympique':
        cur_name = cur_name[1]
        if cur_name == 'Lyonnais':
            cur_name = 'Lyon'
        return cur_name
    return team_name


def render_matches(matches: list, lang: str):
    back_g = Image.open(r'C:/mpr/football_bot/utils/render/Ligue_1/bg/matches/Next matches Ligue1.jpg')
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
            'PSG': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/PSG.png',
            'Lille': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Lille OSC.png',
            'Lyon': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Olympique Lyon.png',
            'Marseille': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Olympique Marseille.png',
            'Monaco': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Monaco.png',
            'Montpellier': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Montpellier.png',
            'Angers SCO': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Angers SCO.png',
            'Lens': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Lens.png',
            'Rennes': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Rennais.png',
            'Bordeaux': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Girondins Bordeaux.png',
            'Nice': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/OGC Nice.png',
            'Brest': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Stade Brestois.png',
            'Metz': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Metz.png',
            'Nantes': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Nantes.png',
            'Saint-Etienne': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Saint Etienne.png',
            'Nîmes': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Nimes Olympique.png',
            'Reims': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Reims.png',
            'Strasbourg': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Strasbourg Alsace.png',
            'Lorient': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Lorient.png',
            'Dijon': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Dijon FCO.png'
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
            'ПСЖ': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/PSG.png',
            'Лилль': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Lille OSC.png',
            'Лион': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Olympique Lyon.png',
            'Марсель': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Olympique Marseille.png',
            'Монако': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Monaco.png',
            'Монпелье': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Montpellier.png',
            'Анже': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Angers SCO.png',
            'Ланс': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Lens.png',
            'Ренн': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Rennais.png',
            'Бордо': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Girondins Bordeaux.png',
            'Ницца': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/OGC Nice.png',
            'Брест': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Stade Brestois.png',
            'Метц': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Metz.png',
            'Нант': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Nantes.png',
            'Сент-Этьен': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Saint Etienne.png',
            'Ним': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Nimes Olympique.png',
            'Реймс': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Reims.png',
            'Страсбур': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Strasbourg Alsace.png',
            'Лорьян': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Lorient.png',
            'Дижон': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Dijon FCO.png'
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
            'ПСЖ': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/PSG.png',
            'Лілль': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Lille OSC.png',
            'Ліон': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Olympique Lyon.png',
            'Марсель': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Olympique Marseille.png',
            'Монако': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Monaco.png',
            'Монпельє': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Montpellier.png',
            'Анже': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Angers SCO.png',
            'Ланс': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Lens.png',
            'Ренн': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Rennais.png',
            'Бордо': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Girondins Bordeaux.png',
            'Ніцца': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/OGC Nice.png',
            'Брест': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Stade Brestois.png',
            'Метц': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Metz.png',
            'Нант': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Nantes.png',
            'Сент-Етьєн': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Saint Etienne.png',
            'Нім': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Nimes Olympique.png',
            'Реймс': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Reims.png',
            'Страсбур': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Strasbourg Alsace.png',
            'Лор\'ян': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Lorient.png',
            'Діжон': r'C:/mpr/football_bot/utils/render/Ligue_1/logo/Dijon FCO.png'
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

    back_g.save(rf'C:\mpr\football_bot\data\matches\l1_{lang}.jpg')


if __name__ == '__main__':
    render_matches(parse_matches('https://football24.ua/frantsiya_games_tag50826/'),
                   'uk')
