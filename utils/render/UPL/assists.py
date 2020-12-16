from PIL import Image, ImageDraw, ImageFont

from utils.parsing.uk import parse_assists
from utils.parsing import split_assists


def render_assists(assists: list, lang: str):
    info_assists = split_assists(assists)

    if lang == 'en':
        goal_pos = 864
        back_g = Image.open('C:/mpr/football_bot/utils/render/UPL/bg/assists/UPL_en.jpg')
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
        goal_pos = 871
        back_g = Image.open('C:/mpr/football_bot/utils/render/UPL/bg/assists/UPL_ru.jpg')
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
        goal_pos = 873
        back_g = Image.open('C:/mpr/football_bot/utils/render/UPL/bg/assists/UPL_ua.jpg')
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

    draw_text = ImageDraw.Draw(back_g)

    for pos, name in enumerate(info_assists[2]):
        cur_name = name.split()
        if cur_name[0] in ['FC']:
            cur_name = cur_name[1]
            info_assists[2][pos] = cur_name
        elif cur_name[0] in ['Динамо', 'Dynamo', 'Shakhtar', 'Kolos', 'Olimpik', 'Rukh', 'Vorskla', 'Zorya',
                             'Inhulets']:
            cur_name = cur_name[0]
            info_assists[2][pos] = cur_name
        if info_assists[2][pos] == 'Mynai':
            info_assists[2][pos] = 'Minaj'
        logo = Image.open(logos[info_assists[2][pos]])
        back_g.paste(logo, (772, 439 + pos * 62), logo)

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

    back_g.save(rf'C:\mpr\football_bot\data\assists\upl_{lang}.jpg')


if __name__ == '__main__':
    render_assists(parse_assists('https://football24.ua/ru/ukrayina_202021_goalassists_tag50819/'), 'ru')
