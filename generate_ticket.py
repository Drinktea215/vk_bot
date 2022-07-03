from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont

TEMPLATE_PATH = "files/ticket.png"
FONT_PATH = "files/Roboto-Regular.ttf"
FONT_SIZE = 20
AVATAR_SIZE = 90


def generate_ticket(city_out, city_in, city_transfer, departure_time, name, email):
    base = Image.open(TEMPLATE_PATH).convert("RGBA")
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    draw = ImageDraw.Draw(base)
    draw.text((220, 94), name, font=font, fill=(0, 0, 0, 255))
    draw.text((220, 125), city_out, font=font, fill=(0, 0, 0, 255))
    draw.text((220, 156), city_in, font=font, fill=(0, 0, 0, 255))
    draw.text((220, 187), city_transfer, font=font, fill=(0, 0, 0, 255))
    draw.text((220, 218), departure_time, font=font, fill=(0, 0, 0, 255))
    draw.text((220, 249), 'Не "Sukhoi Superjet 100"', font=font, fill=(0, 0, 0, 255))

    response = requests.get(url=f'https://api.adorable.io/avatars/{AVATAR_SIZE}/{email}')
    avatar_file_like = BytesIO(response.content)
    avatar = Image.open(avatar_file_like)
    base.paste(avatar, (30, 94))
    temp_file = BytesIO()
    base.save(temp_file, 'png')
    temp_file.seek(0)
    return temp_file
