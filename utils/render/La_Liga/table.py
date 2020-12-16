from PIL import Image, ImageDraw, ImageFont

from utils.parsing.uk import parse_table
from utils.parsing import split_table


def render_table(teams: list, lang: str):
    info_teams = split_table(teams)

    if lang == 'en':
        back_g = Image.open('C:/mpr/football_bot/utils/render/La_Liga/bg/table/LaLiga_en.jpg')
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
        back_g = Image.open('C:/mpr/football_bot/utils/render/La_Liga/bg/table/LaLiga_ru.jpg')
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
        back_g = Image.open('C:/mpr/football_bot/utils/render/La_Liga/bg/table/LaLiga_ua.jpg')
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

    draw_text = ImageDraw.Draw(back_g)

    for pos, name in enumerate(info_teams[2]):
        cur_name = name.split()
        if cur_name[0] in ['Atletico', 'Athletic', 'Celta']:
            cur_name = cur_name[0]
            info_teams[2][pos] = cur_name
        if (len(cur_name)) > 1:
            if cur_name[1] in ['Alavés']:
                cur_name = cur_name[1]
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

    back_g.save(rf'C:\mpr\football_bot\data\tables\ll_{lang}.jpg')


if __name__ == '__main__':
    render_table(
        parse_table('https://football24.ua/ispaniya_tables_tag50823/'), 'uk')
