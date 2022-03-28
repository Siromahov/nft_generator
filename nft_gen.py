from PIL import Image
import numpy as np
import os
from random import seed
from random import randint

dirname = os.path.dirname(__file__)

dimensions = 480, 480

for x in range(0, 5000):
    seed(x)

    hd = (randint(0, 256), randint(0, 256), randint(0, 256))
    c = randint(0, 500)
    seed(c)

    th = (randint(0, 256), randint(0, 256), randint(0, 256))
    d = randint(0, 1000)
    seed(d)

    ew = (240, 248, 255)
    ey = (0, 0, 0)
    e = randint(0, 1000)
    hg = (252, 116, 106)
    seed(e)

    f = randint(0, 1000)
    if f > 500:
        bk = (152, 152, 152)
    elif 500 >= f > 47:
        bk = (204, 172, 0)
    elif 47 >= f > 7:
        bk = (204, 0, 0)
    else:
        bk = (0, 0, 0)

    # background color
    bg = (randint(0, 256), randint(0, 256), randint(0, 256))
    # hat light
    hl = (randint(0, 256), randint(0, 256), randint(0, 256))
    # 2nd_hat_colour
    h2 = (randint(0, 256), randint(0, 256), randint(0, 256))
    # outline color
    ol = (0, 0, 0)
    # bandana
    bn = (randint(0, 256), randint(0, 256), randint(0, 256))
    bl = (179, 92, 16)
    sm = (179, 179, 179)
    # hoodie
    ho = (randint(0, 256), randint(0, 256), randint(0, 256))
    # beard
    f = randint(0, 1000)
    if f > 500:
        # if random number is 501-1000 >> grey beak
        br = (139, 69, 19)
    elif 500 >= f > 47:
        # 48-500 >> gold beak
        br = (204, 172, 0)
    elif 47 >= f > 7:
        # 8 >> 47 >> red beak
        br = (152, 152, 152)
    else:
        # random number is 7 or less >> black beak
        br = (0, 0, 0)

    # man with cap and beard
    basic_man = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, ol, h2, h2, h2, h2, h2, h2, h2, h2, h2, h2, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ew, ew, hd, ew, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ey, ew, hd, ey, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, hd, hd, hd, hd, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, ol, ol, ol, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # man with cap and beard with different eyes
    basic_man2 = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, br, br, hd, br, br, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ey, ew, hd, ey, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, hd, hd, hd, hd, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, ol, ol, ol, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # man with bandana and glasses
    man_with_glasses = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bn, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bn, bn, bn, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bn, bn, bn, bn, bn, bn, bn, bn, bn, bn, bn, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bn, bn, bn, bn, bn, bn, bn, bn, bn, bn, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, ol, hd, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # man with bandana and normal eyes
    man_with_bandana = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bn, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bn, bn, bn, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bn, bn, bn, bn, bn, bn, bn, bn, bn, bn, bn, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bn, bn, bn, bn, bn, bn, bn, bn, bn, bn, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ew, ew, hd, ew, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ey, ew, hd, ey, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # man with bandana and different eyes
    man_with_bandana2 = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bn, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bn, bn, bn, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bn, bn, bn, bn, bn, bn, bn, bn, bn, bn, bn, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bn, bn, bn, bn, bn, bn, bn, bn, bn, bn, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, br, br, hd, br, br, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ey, ew, hd, ey, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # man just with glasses
    bald_man_with_glasses = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, ol, hd, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # man with glasses and cap
    bald_man_with_glasses2 = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, ol, h2, h2, h2, h2, h2, h2, h2, h2, h2, h2, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, ol, hd, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # man with glasses and beard and cap
    bald_man_with_glasses3 = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, ol, h2, h2, h2, h2, h2, h2, h2, h2, h2, h2, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, ol, hd, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, hd, hd, hd, hd, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, ol, ol, ol, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # bald man with glasses and beard
    man_with_glasses_and_beard = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, ol, hd, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, hd, hd, hd, hd, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, ol, ol, ol, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    man_with_hair = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, ol, hd, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, hd, hd, hd, hd, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, ol, ol, ol, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # man with hair and eyes
    man_with_hair2 = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ew, ew, hd, ew, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ey, ew, hd, ey, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, hd, hd, hd, hd, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, ol, ol, ol, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # man with different eyes
    man_with_hair3 = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, br, br, hd, br, br, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ey, ew, hd, ey, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, hd, hd, hd, hd, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, ol, ol, ol, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # man with normal eyes and no beard
    man_with_hair4 = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ew, ew, hd, ew, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ey, ew, hd, ey, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # man with different eyesand no beard
    man_with_hair5 = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, br, br, hd, br, br, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ey, ew, hd, ey, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # high man with cap and beard
    high_man1 = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, ol, h2, h2, h2, h2, h2, h2, h2, h2, h2, h2, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hg, hg, hd, hg, hg, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ey, hg, hd, ey, hg, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, sm, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, sm, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, hd, hd, hd, hd, br, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, br, br, br, ol, bg, sm, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, ol, ol, ol, bl, bl, bl, bl, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, br, br, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, br, br, br, br, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # high man with cap
    high_man2 = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hl, hl, hl, hl, hl, hl, hl, hl, hl, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, ol, h2, h2, h2, h2, h2, h2, h2, h2, h2, h2, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hg, hg, hd, hg, hg, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ey, hg, hd, ey, hg, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, sm, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, sm, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, sm, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, ol, ol, bl, bl, bl, bl, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]
    # just high man
    high_man3 = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hg, hg, hd, hg, hg, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ey, hg, hd, ey, hg, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, sm, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, hd, hd, ol, bg, bg, sm, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, sm, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ol, ol, ol, bl, bl, bl, bl, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    seed(f)
    d = randint(0, 1000)
    if 100 > d:
        pixels = basic_man
        p = "basic"
    elif 200 > d:
        pixels = basic_man2
        p = "basic"
    elif 300 > d:
        pixels = man_with_glasses
        p = "basic"
    elif 350 >= d:
        pixels = bald_man_with_glasses
        p = "basic"
    elif 400 >= d:
        pixels = bald_man_with_glasses2
        p = "basic"
    elif 500 >= d:
        pixels = bald_man_with_glasses3
        p = "basic"
    elif 550 >= d:
        pixels = man_with_glasses_and_beard
        p = "basic"
    elif 600 >= d:
        pixels = man_with_hair
        p = "basic"
    elif 650 >= d:
        pixels = man_with_hair2
        p = "basic"
    elif 700 >= d:
        pixels = man_with_hair3
        p = "basic"
    elif 750 >= d:
        pixels = high_man1
        p = "basic"
    elif 800 >= d:
        pixels = high_man2
        p = "basic"
    elif 850 >= d:
        pixels = high_man3
        p = "basic"
    elif 900 >= d:
        pixels = man_with_bandana
        p = "basic"
    elif 950 >= d:
        pixels = man_with_bandana2
        p = "basic"
    elif 999 >= d:
        pixels = man_with_bandana2
        p = "basic"

    array = np.array(pixels, dtype=np.uint8)

    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = dirname + '/nft_man_images/' + (str(x)) + '.png'
    new_image.save(imgname)
