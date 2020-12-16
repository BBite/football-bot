from PIL import Image, ImageDraw, ImageFont
from datetime import date

from utils.parsing.ru import parse_matches


def _fix_team_name(team_name):
    cur_name = team_name.split()
    if cur_name[0] in ['Айнтрахт', 'Eintracht']:
        cur_name = cur_name[0]
        return cur_name
    elif cur_name[0] in ['Борусія', 'Боруссия', 'Borussia']:
        cur_name[1] = cur_name[1][0]
        cur_name = ' '.join(cur_name)
        return cur_name
    return team_name


def render_matches(matches: list, lang: str):
    back_g = Image.open(r'C:/mpr/football-bot/utils/render/Bundesliga/bg/matches/Next matches Bundesliga.jpg')
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
            'Bayern Munich': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Bayern Munchen.png',
            'Bayer Leverkusen': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Bayer Leverkusen.png',
            'RB Leipzig': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/RB Leipzig.png',
            'Borussia D': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Borussia Dortmund.png',
            'Wolfsburg': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Wolfsburg.png',
            'Union Berlin': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Union Berlin.png',
            'Borussia M': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Borussia Monchengladbach.png',
            'Stuttgart': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Stuttgart.png',
            'Eintracht': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Eintracht.png',
            'Hoffenheim': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Hoffenheim.png',
            'Augsburg': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Augsburg.png',
            'Hertha BSC': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Herta BSC.png',
            'Werder Bremen': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Werder Bremen.png',
            'Freiburg': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Freiburg.png',
            'Köln': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Koln.png',
            'Arminia Bielefeld': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Arminia.png',
            'Mainz 05': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Mainz 05.png',
            'Schalke 04': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Schalke 04.png'
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
            'Бавария': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Bayern Munchen.png',
            'Байер': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Bayer Leverkusen.png',
            'РБ Лейпциг': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/RB Leipzig.png',
            'Боруссия Д': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Borussia Dortmund.png',
            'Вольфсбург': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Wolfsburg.png',
            'Унион Берлин': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Union Berlin.png',
            'Боруссия М': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Borussia Monchengladbach.png',
            'Штутгарт': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Stuttgart.png',
            'Айнтрахт': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Eintracht.png',
            'Хоффенхайм': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Hoffenheim.png',
            'Аугсбург': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Augsburg.png',
            'Герта': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Herta BSC.png',
            'Вердер': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Werder Bremen.png',
            'Фрайбург': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Freiburg.png',
            'Кельн': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Koln.png',
            'Арминия': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Arminia.png',
            'Майнц': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Mainz 05.png',
            'Шальке': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Schalke 04.png'
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
            'Баварія': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Bayern Munchen.png',
            'Байєр': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Bayer Leverkusen.png',
            'РБ Лейпциг': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/RB Leipzig.png',
            'Борусія Д': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Borussia Dortmund.png',
            'Вольфсбург': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Wolfsburg.png',
            'Уніон Берлін': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Union Berlin.png',
            'Борусія М': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Borussia Monchengladbach.png',
            'Штутгарт': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Stuttgart.png',
            'Айнтрахт': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Eintracht.png',
            'Хоффенхайм': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Hoffenheim.png',
            'Аугсбург': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Augsburg.png',
            'Герта': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Herta BSC.png',
            'Вердер': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Werder Bremen.png',
            'Фрайбург': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Freiburg.png',
            'Кельн': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Koln.png',
            'Армінія': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Arminia.png',
            'Майнц': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Mainz 05.png',
            'Шальке': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Schalke 04.png'
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

    back_g.save(rf'C:\mpr\football-bot\data\matches\b_{lang}.jpg')


if __name__ == '__main__':
    render_matches(
        parse_matches('https://football24.ua/nimechchina_games_tag50829/'),
        'uk')
