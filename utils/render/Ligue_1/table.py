from PIL import Image, ImageDraw, ImageFont

from utils.parsing.en import parse_table
from utils.parsing import split_table


def render_table(teams: list, lang: str):
    info_teams = split_table(teams)
    open(r'C:/mpr/football-bot/utils/render/Ligue_1/logo/Strasbourg Alsace.png')

    if lang == 'en':
        back_g = Image.open('C:/mpr/football-bot/utils/render/Ligue_1/bg/table/Ligue1_en.jpg')
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
        back_g = Image.open('C:/mpr/football-bot/utils/render/Ligue_1/bg/table/Ligue1_ru.jpg')
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
        back_g = Image.open('C:/mpr/football-bot/utils/render/Ligue_1/bg/table/Ligue1_ua.jpg')
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

    for pos, name in enumerate(info_teams[2]):
        cur_name = name.split()
        if cur_name[0] == 'Olympique':
            if cur_name[1] == 'Lyonnais':
                cur_name[1] = 'Lyon'
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

    back_g.save(rf'C:\mpr\football-bot\data\tables\l1_{lang}.jpg')


if __name__ == '__main__':
    render_table(
        parse_table('https://int.soccerway.com/national/france/ligue-1/20202021/regular-season/r58178/tables/'),
        'en')
