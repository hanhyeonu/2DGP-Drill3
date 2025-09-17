from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 90
r = 235
cx, cy = 405, 325
d = 5

def move_rectangle():
    global x, y
    while True:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        if y == 90 and x < 784:
            x = x + 2
        elif x >= 784 and y < 560:
            y = y + 2
        elif y >= 560 and x > 16:
            x = x - 2
        elif x <= 16 and y > 90:
            y = y - 2

        delay(0.01)

        if x == 400 and y == 90:
            break


def move_circle():
    global x, y
    angle = 360
    while angle > 0:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        radian = math.radians(angle)
        x = int(cx + r * math.cos(radian))
        y = int(cy + r * math.sin(radian))
        angle = angle - d

        delay(0.01)

    x, y = 400, 90


while True:
    move_rectangle()
    move_circle()
