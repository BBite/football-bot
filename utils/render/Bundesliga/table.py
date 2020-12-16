from PIL import Image, ImageDraw, ImageFont

from utils.parsing.uk import parse_table
from utils.parsing import split_table


def render_table(teams: list, lang: str):
    info_teams = split_table(teams)

    if lang == 'en':
        back_g = Image.open('C:/mpr/football-bot/utils/render/Bundesliga/bg/table/Bundesliga_en.jpg')
        logos = {
            'Bayern Munich': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Bayern Munchen.png',
            'Bayer Leverkusen': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Bayer Leverkusen.png',
            'RB Leipzig': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/RB Leipzig.png',
            'Borussia D': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Borussia Dortmund.png',
            'Wolfsburg': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Wolfsburg.png',
            'Union Berlin': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Union Berlin.png',
            'Borussia M': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Borussia Monchengladbach.png',
            'Stuttgart': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Stuttgart.png',
            'Eintracht': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Eintracht.png',
            'Hoffenheim': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Hoffenheim.png',
            'Augsburg': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Augsburg.png',
            'Hertha BSC': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Herta BSC.png',
            'Werder Bremen': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Werder Bremen.png',
            'Freiburg': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Freiburg.png',
            'Köln': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Koln.png',
            'Arminia Bielefeld': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Arminia.png',
            'Mainz 05': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Mainz 05.png',
            'Schalke 04': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Schalke 04.png'
        }
    elif lang == 'ru':
        back_g = Image.open('C:/mpr/football-bot/utils/render/Bundesliga/bg/table/Bundesliga_ru.jpg')
        logos = {
            'Бавария': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Bayern Munchen.png',
            'Байер': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Bayer Leverkusen.png',
            'РБ Лейпциг': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/RB Leipzig.png',
            'Боруссия Д': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Borussia Dortmund.png',
            'Вольфсбург': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Wolfsburg.png',
            'Унион Берлин': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Union Berlin.png',
            'Боруссия М': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Borussia Monchengladbach.png',
            'Штутгарт': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Stuttgart.png',
            'Айнтрахт': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Eintracht.png',
            'Хоффенхайм': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Hoffenheim.png',
            'Аугсбург': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Augsburg.png',
            'Герта': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Herta BSC.png',
            'Вердер': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Werder Bremen.png',
            'Фрайбург': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Freiburg.png',
            'Кельн': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Koln.png',
            'Арминия': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Arminia.png',
            'Майнц': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Mainz 05.png',
            'Шальке': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Schalke 04.png'
        }
    else:
        back_g = Image.open(r'C:/mpr/football-bot/utils/render/Bundesliga/bg/table/Bundesliga_ua.jpg')
        logos = {
            'Баварія': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Bayern Munchen.png',
            'Байєр': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Bayer Leverkusen.png',
            'РБ Лейпциг': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/RB Leipzig.png',
            'Борусія Д': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Borussia Dortmund.png',
            'Вольфсбург': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Wolfsburg.png',
            'Уніон Берлін': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Union Berlin.png',
            'Борусія М': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Borussia Monchengladbach.png',
            'Штутгарт': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Stuttgart.png',
            'Айнтрахт': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Eintracht.png',
            'Хоффенхайм': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Hoffenheim.png',
            'Аугсбург': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Augsburg.png',
            'Герта': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Herta BSC.png',
            'Вердер': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Werder Bremen.png',
            'Фрайбург': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Freiburg.png',
            'Кельн': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Koln.png',
            'Армінія': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Arminia.png',
            'Майнц': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Mainz 05.png',
            'Шальке': r'C:/mpr/football-bot/utils/render/Bundesliga/logo/Schalke 04.png'
        }

    draw_text = ImageDraw.Draw(back_g)

    for pos, name in enumerate(info_teams[2]):
        cur_name = name.split()
        if cur_name[0] in ['Айнтрахт', 'Eintracht']:
            cur_name = cur_name[0]
            info_teams[2][pos] = cur_name
        elif cur_name[0] in ['Борусія', 'Боруссия', 'Borussia']:
            cur_name[1] = cur_name[1][0]
            cur_name = ' '.join(cur_name)
            info_teams[2][pos] = cur_name
        logo = Image.open(logos[info_teams[2][pos]])
        back_g.paste(logo, (150, 80 + pos * 54), logo)

    font = ImageFont.truetype(r"C:\mpr\aiogram-bot\utils\render\Roboto-Regular.ttf", size=36)

    # pos
    draw_text.multiline_text((100, 76), '\n'.join(info_teams[1]), spacing=20, font=font, fill='black')
    # name
    draw_text.multiline_text((200, 76), '\n'.join(info_teams[2]), spacing=20, font=font, fill='black')
    # played
    draw_text.multiline_text((560, 76), '\n'.join(info_teams[3]), spacing=20, font=font, fill='black')
    # won
    draw_text.multiline_text((620, 76), '\n'.join(info_teams[4]), spacing=20, font=font, fill='black')
    # draw
    draw_text.multiline_text((660, 76), '\n'.join(info_teams[5]), spacing=20, font=font, fill='black')
    # lost
    draw_text.multiline_text((700, 76), '\n'.join(info_teams[6]), spacing=20, font=font, fill='black')
    # goals
    draw_text.multiline_text((770, 76), '\n'.join(info_teams[7]), spacing=20, font=font, fill='black')
    # points
    draw_text.multiline_text((900, 76), '\n'.join(info_teams[8]), spacing=20, font=font, fill='black')

    back_g.save(rf'C:\mpr\football-bot\data\tables\b_{lang}.jpg')


if __name__ == '__main__':
    render_table(
        parse_table('https://football24.ua/nimechchina_tables_tag50829/'), 'uk')
