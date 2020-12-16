from PIL import Image, ImageDraw, ImageFont
from datetime import date

from utils.parsing.en import parse_matches


def _fix_team_name(team_name):
    cur_name = team_name.split()
    if cur_name == ['Minai']:
        return 'Minaj'
    if cur_name[0] in ['Динамо', 'Dynamo', 'Shakhtar', 'Kolos', 'Olimpik', 'Rukh']:
        return cur_name[0]
    return team_name


def render_matches(matches: list, lang: str):
    back_g = Image.open(r'C:/mpr/football_bot/utils/render/UPL/bg/matches/Next matches UPL.jpg')
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
            'Dynamo': r'C:/mpr/football_bot/utils/render/UPL/logo/Dynamo.png',
            'Shakhtar': r'C:/mpr/football_bot/utils/render/UPL/logo/Shakhtar.png',
            'Desna': r'C:/mpr/football_bot/utils/render/UPL/logo/Desna.png',
            'Vorskla': r'C:/mpr/football_bot/utils/render/UPL/logo/Vorskla.png',
            'Zorya': r'C:/mpr/football_bot/utils/render/UPL/logo/Zorya.png',
            'Kolos': r'C:/mpr/football_bot/utils/render/UPL/logo/Kolos.png',
            'Oleksandria': r'C:/mpr/football_bot/utils/render/UPL/logo/Oleksandriya.png',
            'Olimpik': r'C:/mpr/football_bot/utils/render/UPL/logo/Olimpik.png',
            'Mariupol': r'C:/mpr/football_bot/utils/render/UPL/logo/Mariupol.png',
            'Inhulets': r'C:/mpr/football_bot/utils/render/UPL/logo/Ingulets.png',
            'Minaj': r'C:/mpr/football_bot/utils/render/UPL/logo/Minaj.png',
            'Dnipro-1': r'C:/mpr/football_bot/utils/render/UPL/logo/Dniprofake.png',
            'Lviv': r'C:/mpr/football_bot/utils/render/UPL/logo/lviv.png',
            'Rukh': r'C:/mpr/football_bot/utils/render/UPL/logo/Rukh.png'
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
            'Динамо': r'C:/mpr/football_bot/utils/render/UPL/logo/Dynamo.png',
            'Шахтер': r'C:/mpr/football_bot/utils/render/UPL/logo/Shakhtar.png',
            'Десна': r'C:/mpr/football_bot/utils/render/UPL/logo/Desna.png',
            'Ворскла': r'C:/mpr/football_bot/utils/render/UPL/logo/Vorskla.png',
            'Заря': r'C:/mpr/football_bot/utils/render/UPL/logo/Zorya.png',
            'Колос': r'C:/mpr/football_bot/utils/render/UPL/logo/Kolos.png',
            'Александрия': r'C:/mpr/football_bot/utils/render/UPL/logo/Oleksandriya.png',
            'Олимпик': r'C:/mpr/football_bot/utils/render/UPL/logo/Olimpik.png',
            'Мариуполь': r'C:/mpr/football_bot/utils/render/UPL/logo/Mariupol.png',
            'Ингулец': r'C:/mpr/football_bot/utils/render/UPL/logo/Ingulets.png',
            'Минай': r'C:/mpr/football_bot/utils/render/UPL/logo/Minaj.png',
            'СК Днепр-1': r'C:/mpr/football_bot/utils/render/UPL/logo/Dniprofake.png',
            'Львов': r'C:/mpr/football_bot/utils/render/UPL/logo/lviv.png',
            'Рух': r'C:/mpr/football_bot/utils/render/UPL/logo/Rukh.png'
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
            'Динамо': r'C:/mpr/football_bot/utils/render/UPL/logo/Dynamo.png',
            'Шахтар': r'C:/mpr/football_bot/utils/render/UPL/logo/Shakhtar.png',
            'Десна': r'C:/mpr/football_bot/utils/render/UPL/logo/Desna.png',
            'Ворскла': r'C:/mpr/football_bot/utils/render/UPL/logo/Vorskla.png',
            'Зоря': r'C:/mpr/football_bot/utils/render/UPL/logo/Zorya.png',
            'Колос': r'C:/mpr/football_bot/utils/render/UPL/logo/Kolos.png',
            'Олександрія': r'C:/mpr/football_bot/utils/render/UPL/logo/Oleksandriya.png',
            'Олімпік': r'C:/mpr/football_bot/utils/render/UPL/logo/Olimpik.png',
            'Маріуполь': r'C:/mpr/football_bot/utils/render/UPL/logo/Mariupol.png',
            'Інгулець': r'C:/mpr/football_bot/utils/render/UPL/logo/Ingulets.png',
            'Минай': r'C:/mpr/football_bot/utils/render/UPL/logo/Minaj.png',
            'СК Дніпро-1': r'C:/mpr/football_bot/utils/render/UPL/logo/Dniprofake.png',
            'Львів': r'C:/mpr/football_bot/utils/render/UPL/logo/lviv.png',
            'Рух': r'C:/mpr/football_bot/utils/render/UPL/logo/Rukh.png'
        }

    cur_weekday = None
    pos_y = 50 + draw_text.textsize(matches[0], font=top_font)[1] - 70
    for match in matches[1:]:
        weekday = weekdays[date(int(match['year']), int(match['month']), int(match['day'])).weekday()]
        if cur_weekday != weekday:
            cur_weekday = weekday
            pos_y += 150
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

    back_g.save(rf'C:\mpr\football_bot\data\matches\upl_{lang}.jpg')


if __name__ == '__main__':
    render_matches(parse_matches(
        'https://int.soccerway.com/national/ukraine/premier-league/20202021/regular-season/r59290/'), 'en')
