from PIL import Image, ImageDraw, ImageFont

from utils.parsing.uk import parse_assists
from utils.parsing import split_assists


def render_assists(assists: list, lang: str):
    info_assists = split_assists(assists)

    if lang == 'en':
        back_g = Image.open('C:/mpr/football_bot/utils/render/Serie_A/bg/assists/Serie A_en.jpg')
        logos = {
            'Milan': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Milan.png',
            'Inter': r'C:/mpr/football_bot/utils/render/Serie_A/logo/Inter.png',
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
        back_g = Image.open('C:/mpr/football_bot/utils/render/Serie_A/bg/assists/Serie A_ru.jpg')
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
        back_g = Image.open('C:/mpr/football_bot/utils/render/Serie_A/bg/assists/Serie A_ua.jpg')
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

    draw_text = ImageDraw.Draw(back_g)

    for pos, name in enumerate(info_assists[2]):
        cur_name = name.split()
        two_teams = name.split(',')
        if len(two_teams) > 1:
            info_assists[2][pos] = cur_name
            info_assists[2][pos] = two_teams[0]
        if cur_name[0] == 'Inter':
            cur_name = cur_name[0]
            info_assists[2][pos] = cur_name
        elif len(cur_name) > 1:
            if cur_name[1] in ['Verona', 'Milan']:
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

    back_g.save(rf'C:\mpr\football_bot\data\assists\sa_{lang}.jpg')


if __name__ == '__main__':
    render_assists(parse_assists('https://football24.ua/italiya_goalassists_tag50822/'), 'uk')
