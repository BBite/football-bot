from PIL import Image, ImageDraw, ImageFont
from datetime import date

from utils.parsing.uk import parse_matches


def _fix_team_name(team_name):
    cur_name = team_name.split()
    if (len(cur_name)) > 1:
        if cur_name[1] in ['Verona']:
            cur_name = cur_name[1]
            return cur_name
    return team_name


def render_matches(matches: list, lang: str):
    back_g = Image.open(r'C:/mpr/football_bot/utils/render/Serie_A/bg/matches/Next matches SerieA.jpg')
    draw_text = ImageDraw.Draw(back_g)

    font = ImageFont.truetype(r"C:\mpr\aiogram-bot\utils\render\Roboto-Regular.ttf", size=36)
    title_font = ImageFont.truetype(r"C:\mpr\aiogram-bot\utils\render\Roboto-Regular.ttf", size=26)
    top_font = ImageFont.truetype(r"C:\mpr\aiogram-bot\utils\render\Roboto-Regular.ttf", size=48)

    # print(matches)
    draw_text.text((540, 50), matches[0], anchor='mm', font=top_font, fill=(255, 255, 255))

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
            'Milan': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Milan.png',
            'Internazionale': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Inter.png',
            'Napoli': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Napoli.png',
            'Juventus': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Juventus.png',
            'Sassuolo': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Sassuolo.png',
            'Roma': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Roma.png',
            'Lazio': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Lazio.png',
            'Verona': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Hellas Verona.png',
            'Atalanta': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Atalanta.png',
            'Bologna': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Bologna.png',
            'Cagliari': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Cagliari.png',
            'Sampdoria': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Sampdoria.png',
            'Benevento': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Beneveto.png',
            'Udinese': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Udinese.png',
            'Spezia': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Spezia.png',
            'Parma': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Parma.png',
            'Fiorentina': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Fioerentina.png',
            'Torino': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Torina.png',
            'Genoa': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Genoa.png',
            'Crotone': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Crotone.png'
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
            'Милан': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Milan.png',
            'Интер': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Inter.png',
            'Наполи': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Napoli.png',
            'Ювентус': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Juventus.png',
            'Сассуоло': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Sassuolo.png',
            'Рома': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Roma.png',
            'Лацио': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Lazio.png',
            'Верона': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Hellas Verona.png',
            'Аталанта': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Atalanta.png',
            'Болонья': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Bologna.png',
            'Кальяри': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Cagliari.png',
            'Сампдория': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Sampdoria.png',
            'Беневенто': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Beneveto.png',
            'Удинезе': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Udinese.png',
            'Специя': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Spezia.png',
            'Парма': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Parma.png',
            'Фиорентина': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Fioerentina.png',
            'Торино': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Torina.png',
            'Дженоа': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Genoa.png',
            'Кротоне': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Crotone.png'
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
            'Мілан': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Milan.png',
            'Інтер': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Inter.png',
            'Наполі': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Napoli.png',
            'Ювентус': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Juventus.png',
            'Сассуоло': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Sassuolo.png',
            'Рома': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Roma.png',
            'Лаціо': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Lazio.png',
            'Верона': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Hellas Verona.png',
            'Аталанта': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Atalanta.png',
            'Болонья': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Bologna.png',
            'Кальярі': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Cagliari.png',
            'Сампдорія': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Sampdoria.png',
            'Беневенто': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Beneveto.png',
            'Удінезе': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Udinese.png',
            'Спеція': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Spezia.png',
            'Парма': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Parma.png',
            'Фіорентина': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Fioerentina.png',
            'Торіно': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Torina.png',
            'Дженоа': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Genoa.png',
            'Кротоне': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Crotone.png'
        }

    cur_weekday = None
    pos_y = 50 + draw_text.textsize(matches[0], font=top_font)[1]
    for match in matches[1:]:
        weekday = weekdays[date(int(match['year']), int(match['month']), int(match['day'])).weekday()]
        if cur_weekday != weekday:
            cur_weekday = weekday
            pos_y += 70
            title = cur_weekday + ', ' + match['day'] + ' ' + months[match['month']] + ' ' + match['year']
            draw_text.text((540, pos_y), title, anchor='mm', font=title_font, fill=(255, 255, 255))
            pos_y += draw_text.textsize(title, font=title_font)[1]

        pos_y += 20
        text = match['time'] if match['time'] != 'FT' else match['score']
        draw_text.text((540, pos_y), text, anchor='mm', font=font if text != canceled_text else title_font,
                       fill='white')
        team_1 = _fix_team_name(match['team 1'])
        draw_text.text((380, pos_y), team_1, anchor='rm', font=font, fill=(255, 255, 255))
        logo_1 = Image.open(logos[team_1])
        back_g.paste(logo_1, (400, pos_y - 18), logo_1)
        team_2 = _fix_team_name(match['team 2'])
        draw_text.text((700, pos_y), team_2, anchor='lm', font=font, fill=(255, 255, 255))
        logo_2 = Image.open(logos[team_2])
        back_g.paste(logo_2, (640, pos_y - 18), logo_2)
        pos_y += draw_text.textsize(text, font=font)[1]

    back_g.save(rf'C:\mpr\football_bot\data\matches\sa_{lang}.jpg')


if __name__ == '__main__':
    render_matches(parse_matches('https://football24.ua/italiya_games_tag50822/'),
                   'uk')
