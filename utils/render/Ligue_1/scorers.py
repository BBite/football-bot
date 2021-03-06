from PIL import Image, ImageDraw, ImageFont

from utils.parsing.ru import parse_scorers_fr
from utils.parsing import split_scorers


def render_scorers(scorers: list, lang: str):
    info_scorers = split_scorers(scorers)

    if lang == 'en':
        goal_pos = 864
        back_g = Image.open('C:/mpr/football-bot/utils/render/Ligue_1/bg/scorers/Ligue 1_en.jpg')
        logos = {
            'PSG': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/PSG.png',
            'Lille': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Lille OSC.png',
            'Lyon': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Olympique Lyon.png',
            'Marseille': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Olympique Marseille.png',
            'Monaco': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Monaco.png',
            'Montpellier': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Montpellier.png',
            'Angers SCO': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Angers SCO.png',
            'Lens': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Lens.png',
            'Rennes': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Rennais.png',
            'Bordeaux': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Girondins Bordeaux.png',
            'Nice': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/OGC Nice.png',
            'Brest': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Stade Brestois.png',
            'Metz': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Metz.png',
            'Nantes': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Nantes.png',
            'Saint-Etienne': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Saint Etienne.png',
            'Nîmes': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Nimes Olympique.png',
            'Reims': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Reims.png',
            'Strasbourg': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Strasbourg Alsace.png',
            'Lorient': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Lorient.png',
            'Dijon': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Dijon FCO.png'
        }
    elif lang == 'ru':
        goal_pos = 871
        back_g = Image.open('C:/mpr/football-bot/utils/render/Ligue_1/bg/scorers/Ligue 1_ru.jpg')
        logos = {
            'ПСЖ': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/PSG.png',
            'Лилль': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Lille OSC.png',
            'Лион': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Olympique Lyon.png',
            'Марсель': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Olympique Marseille.png',
            'Монако': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Monaco.png',
            'Монпелье': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Montpellier.png',
            'Анже': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Angers SCO.png',
            'Ланс': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Lens.png',
            'Ренн': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Rennais.png',
            'Бордо': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Girondins Bordeaux.png',
            'Ницца': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/OGC Nice.png',
            'Брест': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Stade Brestois.png',
            'Метц': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Metz.png',
            'Нант': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Nantes.png',
            'Сент-Этьен': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Saint Etienne.png',
            'Ним': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Nimes Olympique.png',
            'Реймс': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Reims.png',
            'Страсбур': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Strasbourg Alsace.png',
            'Лорьян': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Lorient.png',
            'Дижон': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Dijon FCO.png'
        }
    else:
        goal_pos = 873
        back_g = Image.open('C:/mpr/football-bot/utils/render/Ligue_1/bg/scorers/Ligue 1_ua.jpg')
        logos = {
            'ПСЖ': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/PSG.png',
            'Лілль': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Lille OSC.png',
            'Ліон': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Olympique Lyon.png',
            'Марсель': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Olympique Marseille.png',
            'Монако': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Monaco.png',
            'Монпельє': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Montpellier.png',
            'Анже': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Angers SCO.png',
            'Ланс': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Lens.png',
            'Ренн': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Rennais.png',
            'Бордо': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Girondins Bordeaux.png',
            'Ніцца': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/OGC Nice.png',
            'Брест': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Stade Brestois.png',
            'Метц': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Metz.png',
            'Нант': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Nantes.png',
            'Сент-Етьєн': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Saint Etienne.png',
            'Нім': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Nimes Olympique.png',
            'Реймс': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Reims.png',
            'Страсбур': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Strasbourg Alsace.png',
            'Лор\'ян': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Lorient.png',
            'Діжон': r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Dijon FCO.png'
        }

    draw_text = ImageDraw.Draw(back_g)

    for pos, name in enumerate(info_scorers[2]):
        if name == 'Paris Saint Germain':
            info_scorers[2][pos] = 'PSG'
        elif name in ['Парі Сен-Жермен', 'Пари Сен-Жермен']:
            info_scorers[2][pos] = 'ПСЖ'
        logo = Image.open(logos[info_scorers[2][pos]])
        back_g.paste(logo, (772, 439 + pos * 62), logo)

    font = ImageFont.truetype(r"C:\mpr\aiogram-bot\utils\render\Roboto-Regular.ttf", size=32)

    # pos
    draw_text.multiline_text((400, 440), '\n'.join(info_scorers[0]), spacing=32, font=font, fill='white')
    # name
    draw_text.multiline_text((448, 440), '\n'.join(info_scorers[1]), spacing=32, font=font, fill='white')
    # goals
    draw_text.multiline_text((goal_pos, 440), '\n'.join(info_scorers[3]), spacing=32, font=font, fill='white')
    # played
    draw_text.multiline_text((965, 440), '\n'.join(info_scorers[4]), spacing=32, font=font, fill='white')

    back_g.save(rf'C:\mpr\football-bot\data\scorers\l1_{lang}.jpg')


if __name__ == '__main__':
    render_scorers(parse_scorers_fr('https://www.ua-football.com/foreign/france/scorers'), 'ru')
