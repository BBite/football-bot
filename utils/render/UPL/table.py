from PIL import Image, ImageDraw, ImageFont

from utils.parsing.uk import parse_table
from utils.parsing import split_table


def render_table(teams: list, lang: str):
    info_teams = split_table(teams)

    if lang == 'en':
        back_g = Image.open('C:/mpr/football-bot/utils/render/UPL/bg/table/UPL_en.jpg')
        logos = {
            'Dynamo': r'C:/mpr/football-bot/utils/render/UPL/logo/Dynamo.png',
            'Shakhtar': r'C:/mpr/football-bot/utils/render/UPL/logo/Shakhtar.png',
            'Desna': r'C:/mpr/football-bot/utils/render/UPL/logo/Desna.png',
            'Vorskla': r'C:/mpr/football-bot/utils/render/UPL/logo/Vorskla.png',
            'Zorya': r'C:/mpr/football-bot/utils/render/UPL/logo/Zorya.png',
            'Kolos': r'C:/mpr/football-bot/utils/render/UPL/logo/Kolos.png',
            'Oleksandria': r'C:/mpr/football-bot/utils/render/UPL/logo/Oleksandriya.png',
            'Olimpik': r'C:/mpr/football-bot/utils/render/UPL/logo/Olimpik.png',
            'Mariupol': r'C:/mpr/football-bot/utils/render/UPL/logo/Mariupol.png',
            'Inhulets': r'C:/mpr/football-bot/utils/render/UPL/logo/Ingulets.png',
            'Minaj': r'C:/mpr/football-bot/utils/render/UPL/logo/Minaj.png',
            'Dnipro-1': r'C:/mpr/football-bot/utils/render/UPL/logo/Dniprofake.png',
            'Lviv': r'C:/mpr/football-bot/utils/render/UPL/logo/lviv.png',
            'Rukh': r'C:/mpr/football-bot/utils/render/UPL/logo/Rukh.png'
        }
    elif lang == 'ru':
        back_g = Image.open('C:/mpr/football-bot/utils/render/UPL/bg/table/UPL_ru.jpg')
        logos = {
            'Динамо': r'C:/mpr/football-bot/utils/render/UPL/logo/Dynamo.png',
            'Шахтер': r'C:/mpr/football-bot/utils/render/UPL/logo/Shakhtar.png',
            'Десна': r'C:/mpr/football-bot/utils/render/UPL/logo/Desna.png',
            'Ворскла': r'C:/mpr/football-bot/utils/render/UPL/logo/Vorskla.png',
            'Заря': r'C:/mpr/football-bot/utils/render/UPL/logo/Zorya.png',
            'Колос': r'C:/mpr/football-bot/utils/render/UPL/logo/Kolos.png',
            'Александрия': r'C:/mpr/football-bot/utils/render/UPL/logo/Oleksandriya.png',
            'Олимпик': r'C:/mpr/football-bot/utils/render/UPL/logo/Olimpik.png',
            'Мариуполь': r'C:/mpr/football-bot/utils/render/UPL/logo/Mariupol.png',
            'Ингулец': r'C:/mpr/football-bot/utils/render/UPL/logo/Ingulets.png',
            'Минай': r'C:/mpr/football-bot/utils/render/UPL/logo/Minaj.png',
            'СК Днепр-1': r'C:/mpr/football-bot/utils/render/UPL/logo/Dniprofake.png',
            'Львов': r'C:/mpr/football-bot/utils/render/UPL/logo/lviv.png',
            'Рух': r'C:/mpr/football-bot/utils/render/UPL/logo/Rukh.png'
        }
    else:
        back_g = Image.open('C:/mpr/football-bot/utils/render/UPL/bg/table/UPL_ua.jpg')
        logos = {
            'Динамо': r'C:/mpr/football-bot/utils/render/UPL/logo/Dynamo.png',
            'Шахтар': r'C:/mpr/football-bot/utils/render/UPL/logo/Shakhtar.png',
            'Десна': r'C:/mpr/football-bot/utils/render/UPL/logo/Desna.png',
            'Ворскла': r'C:/mpr/football-bot/utils/render/UPL/logo/Vorskla.png',
            'Зоря': r'C:/mpr/football-bot/utils/render/UPL/logo/Zorya.png',
            'Колос': r'C:/mpr/football-bot/utils/render/UPL/logo/Kolos.png',
            'Олександрія': r'C:/mpr/football-bot/utils/render/UPL/logo/Oleksandriya.png',
            'Олімпік': r'C:/mpr/football-bot/utils/render/UPL/logo/Olimpik.png',
            'Маріуполь': r'C:/mpr/football-bot/utils/render/UPL/logo/Mariupol.png',
            'Інгулець': r'C:/mpr/football-bot/utils/render/UPL/logo/Ingulets.png',
            'Минай': r'C:/mpr/football-bot/utils/render/UPL/logo/Minaj.png',
            'СК Дніпро-1': r'C:/mpr/football-bot/utils/render/UPL/logo/Dniprofake.png',
            'Львів': r'C:/mpr/football-bot/utils/render/UPL/logo/lviv.png',
            'Рух': r'C:/mpr/football-bot/utils/render/UPL/logo/Rukh.png'
        }

    draw_text = ImageDraw.Draw(back_g)

    for pos, name in enumerate(info_teams[2]):
        cur_name = name.split()
        if name == 'Minai':
            info_teams[2][pos] = 'Minaj'
        elif cur_name[0] in ['Динамо', 'Dynamo', 'Shakhtar', 'Kolos', 'Olimpik', 'Rukh']:
            cur_name = cur_name[0]
            info_teams[2][pos] = cur_name
        logo = Image.open(logos[info_teams[2][pos]])
        back_g.paste(logo, (150, 86 + pos * 70), logo)

    font = ImageFont.truetype(r"C:\mpr\aiogram-bot\utils\render\Roboto-Regular.ttf", size=36)

    # pos
    draw_text.multiline_text((100, 85), '\n'.join(info_teams[1]), spacing=36, font=font, fill='black')
    # name
    draw_text.multiline_text((200, 85), '\n'.join(info_teams[2]), spacing=36, font=font, fill='black')
    # played
    draw_text.multiline_text((560, 85), '\n'.join(info_teams[3]), spacing=36, font=font, fill='black')
    # won
    draw_text.multiline_text((620, 85), '\n'.join(info_teams[4]), spacing=36, font=font, fill='black')
    # draw
    draw_text.multiline_text((660, 85), '\n'.join(info_teams[5]), spacing=36, font=font, fill='black')
    # lost
    draw_text.multiline_text((700, 85), '\n'.join(info_teams[6]), spacing=36, font=font, fill='black')
    # goals
    draw_text.multiline_text((770, 85), '\n'.join(info_teams[7]), spacing=36, font=font, fill='black')
    # points
    draw_text.multiline_text((900, 85), '\n'.join(info_teams[8]), spacing=36, font=font, fill='black')

    back_g.save(rf'C:\mpr\football-bot\data\tables\upl_{lang}.jpg')


if __name__ == '__main__':
    render_table(
        parse_table('https://football24.ua/ukraina_tables_tag50819/'), 'uk')
