import subprocess as sp
from PIL import Image, ImageDraw, ImageOps, ImageFilter
import requests
from io import BytesIO
import numpy as np


def get_resolution():
    cmd = ['xrandr']
    cmd2 = ['grep', '*']
    p = sp.Popen(cmd, stdout=sp.PIPE)
    p2 = sp.Popen(cmd2, stdin=p.stdout, stdout=sp.PIPE)
    p.stdout.close()
    resolution_string, junk = p2.communicate()
    resolution = resolution_string.split()[0].decode("utf-8")

    return tuple(map(int, resolution.split('x')))


def get_current_image():
    URL="https://sdo.gsfc.nasa.gov/assets/img/latest/latest_4096_0171.jpg"
    response = requests.get(URL)

    return Image.open(BytesIO(response.content))


def generate_mask(width, height, adjust=430):
    ellipse = ((0+adjust, 0+adjust), (width-adjust, height-adjust))
    mask = Image.new('L', (width, height), 255)
    draw = ImageDraw.Draw(mask)
    draw.ellipse(ellipse, 0)

    return mask

def mask_image(image, mask):
    background = Image.new('RGB', image.size, 0)
    return Image.composite(background, image, mask)


def create_wallpaper(image, width, height, size=1000):
    image = image.resize((size, size))
    x0, x1 = int(width/2-(size/2)), int(width/2+(size/2))
    y0, y1 = int(height/2-(size/2)), int(height/2+(size/2))

    background = Image.new('RGB', (width, height), 0)
    background.paste(image, (x0, y0, x1, y1))

    return background


if __name__ == "__main__":
    sun_image = get_current_image()
    screen_width, screen_height = get_resolution()
    sun_width, sun_height = sun_image.size
    mask = generate_mask(sun_width, sun_height)
    image_masked = mask_image(sun_image, mask)
    wallpaper = create_wallpaper(image_masked, width=screen_width,
                                 height=screen_height)
    wallpaper.save('teste', "PNG")
