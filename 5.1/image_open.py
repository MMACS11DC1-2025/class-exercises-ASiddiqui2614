from PIL import Image

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

def is_green(r, g, b):
    if 0 < r <= 25 and 230 < g <= 255 and 0 < b <= 25:
        return True
    else:
        return False
def color(r, g, b):
    if r == 255 and 0 == g and 0 == b:
        return "red"
    if r == 0 and 255 == g and 0 == b:
        return "green"
    if r == 0 and 0 == g and 255 == b:
        return "blue"
    if r == 255 and 255 == g and 255 == b:
        return "white"
    if r == 0 and 0 == g and 0 == b:
        return "black"
    if r == 255 and 255 == g and 0 == b:
        return "yellow"
    if r == 255 and 0 == g and 255 == b:
        return "magenta"