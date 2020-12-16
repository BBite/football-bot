from PIL import Image, ImageDraw, ImageFont

from utils.parsing.en import parse_table
from utils.parsing import split_table


def render_table(teams: list, lang: str):
    info_teams = split_table(teams)

    if lang == 'en':
        back_g = Image.open('C:/mpr/football-bot/utils/render/Serie_A/bg/table/SerieA_en.jpg')
        logos = {
            'Milan': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Milan.png',
            'Inter': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Inter.png',
            'Napoli': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Napoli.png',
            'Juventus': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Juventus.png',
            'Sassuolo': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Sassuolo.png',
            'Roma': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Roma.png',
            'Lazio': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Lazio.png',
            'Verona': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Hellas Verona.png',
            'Atalanta': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Atalanta.png',
            'Bologna': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Bologna.png',
            'Cagliari': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Cagliari.png',
            'Sampdoria': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Sampdoria.png',
            'Benevento': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Beneveto.png',
            'Udinese': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Udinese.png',
            'Spezia': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Spezia.png',
            'Parma': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Parma.png',
            'Fiorentina': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Fioerentina.png',
            'Torino': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Torina.png',
            'Genoa': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Genoa.png',
            'Crotone': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Crotone.png'
        }
    elif lang == 'ru':
        back_g = Image.open('C:/mpr/football-bot/utils/render/Serie_A/bg/table/SerieA_ru.jpg')
        logos = {
            'Милан': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Milan.png',
            'Интер': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Inter.png',
            'Наполи': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Napoli.png',
            'Ювентус': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Juventus.png',
            'Сассуоло': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Sassuolo.png',
            'Рома': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Roma.png',
            'Лацио': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Lazio.png',
            'Верона': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Hellas Verona.png',
            'Аталанта': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Atalanta.png',
            'Болонья': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Bologna.png',
            'Кальяри': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Cagliari.png',
            'Сампдория': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Sampdoria.png',
            'Беневенто': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Beneveto.png',
            'Удинезе': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Udinese.png',
            'Специя': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Spezia.png',
            'Парма': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Parma.png',
            'Фиорентина': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Fioerentina.png',
            'Торино': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Torina.png',
            'Дженоа': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Genoa.png',
            'Кротоне': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Crotone.png'
        }
    else:
        back_g = Image.open('C:/mpr/football-bot/utils/render/Serie_A/bg/table/SerieA_ua.jpg')
        logos = {
            'Мілан': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Milan.png',
            'Інтер': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Inter.png',
            'Наполі': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Napoli.png',
            'Ювентус': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Juventus.png',
            'Сассуоло': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Sassuolo.png',
            'Рома': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Roma.png',
            'Лаціо': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Lazio.png',
            'Верона': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Hellas Verona.png',
            'Аталанта': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Atalanta.png',
            'Болонья': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Bologna.png',
            'Кальярі': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Cagliari.png',
            'Сампдорія': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Sampdoria.png',
            'Беневенто': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Beneveto.png',
            'Удінезе': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Udinese.png',
            'Спеція': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Spezia.png',
            'Парма': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Parma.png',
            'Фіорентина': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Fioerentina.png',
            'Торіно': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Torina.png',
            'Дженоа': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Genoa.png',
            'Кротоне': r'C:/mpr/football-bot/utils/render/Serie_A/logo/Crotone.png'
        }

    draw_text = ImageDraw.Draw(back_g)

    for pos, name in enumerate(info_teams[2]):
        cur_name = name.split()
        if cur_name[0] == 'Internazionale':
            info_teams[2][pos] = 'Inter'
        elif len(cur_name) > 1:
            if cur_name[1] in ['Verona']:
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

    back_g.save(rf'C:\mpr\football-bot\data\tables\sa_{lang}.jpg')


if __name__ == '__main__':
    render_table(parse_table('https://int.soccerway.com/national/italy/serie-a/20202021/regular-season/r59286/tables/'),
                 'en')
