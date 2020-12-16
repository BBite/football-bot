from PIL import Image, ImageDraw, ImageFont

from utils.parsing.ru import parse_scorers
from utils.parsing import split_scorers


def render_scorers(scorers: list, lang: str):
    info_scorers = split_scorers(scorers)

    if lang == 'en':
        goal_pos = 864
        back_g = Image.open('C:/mpr/football-bot/utils/render/Serie_A/bg/scorers/Serie A_en.jpg')
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
        goal_pos = 871
        back_g = Image.open('C:/mpr/football-bot/utils/render/Serie_A/bg/scorers/Serie A_ru.jpg')
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
        goal_pos = 873
        back_g = Image.open('C:/mpr/football-bot/utils/render/Serie_A/bg/scorers/Serie A_ua.jpg')
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

    for pos, name in enumerate(info_scorers[2]):
        cur_name = name.split()
        if cur_name[0] == 'Inter':
            cur_name = cur_name[0]
            info_scorers[2][pos] = cur_name
        elif len(cur_name) > 1:
            if cur_name[1] in ['Verona', 'Milan']:
                cur_name = cur_name[1]
                info_scorers[2][pos] = cur_name
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
    draw_text.multiline_text((967, 440), '\n'.join(info_scorers[4]), spacing=32, font=font, fill='white')

    back_g.save(rf'C:\mpr\football-bot\data\scorers\sa_{lang}.jpg')


if __name__ == '__main__':
    render_scorers(parse_scorers('https://football24.ua/ru/italiya_202021_forwards_tag50822/'), 'ru')
