from PIL import Image, ImageDraw, ImageFont

from utils.parsing.uk import parse_assists
from utils.parsing import split_assists


def render_assists(assists: list, lang: str):
    info_assists = split_assists(assists)

    if lang == 'en':
        back_g = Image.open('C:/mpr/football_bot/utils/render/La_Liga/bg/assists/LaLiga_en.jpg')
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
        back_g = Image.open('C:/mpr/football_bot/utils/render/La_Liga/bg/assists/LaLiga_ru.jpg')
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
        back_g = Image.open('C:/mpr/football_bot/utils/render/La_Liga/bg/assists/LaLiga_ua.jpg')
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

    for pos, name in enumerate(info_assists[2]):
        cur_name = name.split()
        if cur_name[0] == 'Atlético':
            info_assists[2][pos] = 'Atletico'
        elif cur_name[0] in ['Atletico', 'Athletic', 'Celta']:
            cur_name = cur_name[0]
            info_assists[2][pos] = cur_name
        elif (len(cur_name)) > 1:
            if cur_name[1] in ['Alavés']:
                cur_name = cur_name[1]
                info_assists[2][pos] = cur_name
        logo = Image.open(logos[info_assists[2][pos]])
        back_g.paste(logo, (755, 439 + pos * 62), logo)

    font = ImageFont.truetype(r"C:\mpr\aiogram-bot\utils\render\Roboto-Regular.ttf", size=32)

    # print(draw_text.multiline_textsize('\n'.join(info_scorers[2][:1]), spacing=32, font=font))

    # pos
    draw_text.multiline_text((379, 440), '\n'.join(info_assists[0]), spacing=32, font=font, fill='white')
    # name
    draw_text.multiline_text((428, 440), '\n'.join(info_assists[1]), spacing=32, font=font, fill='white')
    # goals
    draw_text.multiline_text((855, 440), '\n'.join(info_assists[3]), spacing=32, font=font, fill='white')
    # played
    draw_text.multiline_text((965, 440), '\n'.join(info_assists[4]), spacing=32, font=font, fill='white')

    back_g.save(rf'C:\mpr\football_bot\data\assists\ll_{lang}.jpg')


if __name__ == '__main__':
    render_assists(parse_assists('https://football24.ua/ispaniya_202021_goalassists_tag50823/'), 'uk')
