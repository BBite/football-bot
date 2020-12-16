from PIL import Image, ImageDraw, ImageFont

from utils.parsing.en import parse_scorers
from utils.parsing import split_scorers


def render_scorers(scorers: list, lang: str):
    info_scorers = split_scorers(scorers)

    if lang == 'en':
        goal_pos = 864
        back_g = Image.open(r'C:/mpr/football-bot/utils/render/Bundesliga/bg/scorers/Bundesliga_en.jpg')
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
        goal_pos = 871
        back_g = Image.open('C:/mpr/football-bot/utils/render/Bundesliga/bg/scorers/Bundesliga_ru.jpg')
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
        goal_pos = 873
        back_g = Image.open('C:/mpr/football-bot/utils/render/Bundesliga/bg/scorers/Bundesliga_ua.jpg')
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

    for pos, name in enumerate(info_scorers[2]):
        cur_name = name.split()
        if len(cur_name) > 1:
            if cur_name[1] == 'FC':
                cur_name = ' '.join(cur_name[2:])
                info_scorers[2][pos] = cur_name
            elif cur_name[1] in ['Wolfsburg', 'Stuttgart', 'Hoffenheim', ]:
                cur_name = cur_name[1]
                info_scorers[2][pos] = cur_name
            elif cur_name[0] in ['Bayer']:
                cur_name = cur_name[0] + ' ' + cur_name[2]
                info_scorers[2][pos] = cur_name
            elif cur_name[0] in ['Айнтрахт', 'Eintracht']:
                cur_name = cur_name[0]
                info_scorers[2][pos] = cur_name
            elif cur_name[0] in ['Борусія', 'Боруссия', 'Borussia']:
                cur_name[1] = cur_name[1][0]
                cur_name = ' '.join(cur_name)
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
    draw_text.multiline_text((965, 440), '\n'.join(info_scorers[4]), spacing=32, font=font, fill='white')

    back_g.save(rf'C:\mpr\football-bot\data\scorers\b_{lang}.jpg')


if __name__ == '__main__':
    render_scorers(parse_scorers('https://www.bbc.com/sport/football/german-bundesliga/top-scorers'), 'en')
