from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_line(x0, y0, x1, y1, step=2, frame_delay=0.01):
    dx = x1 - x0
    dy = y1 - y0
    dist = math.hypot(dx, dy)
    if dist == 0:
        # 바로 그립니다
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(int(x1), int(y1))
        delay(frame_delay)
        return
    steps = max(1, int(dist / step))
    for i in range(steps):
        t = (i + 1) / steps
        xi = x0 + dx * t
        yi = y0 + dy * t
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(int(xi), int(yi))
        delay(frame_delay)
    # 정확한 종료점 보정
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(int(x1), int(y1))
    delay(frame_delay)

def move_rectangle():
    # 경로: (400,90) -> (784,90) -> (784,560) -> (16,560) -> (16,90) -> (400,90)
    pts = [
        (400, 90),
        (784, 90),
        (784, 560),
        (16, 560),
        (16, 90),
        (400, 90),
    ]
    for a, b in zip(pts, pts[1:]):
        move_line(a[0], a[1], b[0], b[1])

def move_circle():
    cx, cy, r = 405, 325, 235
    for angle in range(360, 0, -5):
        clear_canvas_now()
        grass.draw_now(400, 30)
        rad = math.radians(angle)
        x = int(cx + r * math.cos(rad))
        y = int(cy + r * math.sin(rad))
        character.draw_now(x, y)
        delay(0.01)
    # (원운동 후 원래 위치로 복귀하는 처리를 원치 않으면 제거 가능)
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400, 90)
    delay(0.01)

def move_triangle():
    # 경로: (400,90) -> (784,90) -> (400,560) -> (16,90) -> (400,90)
    pts = [
        (400, 90),
        (784, 90),
        (400, 560),
        (16, 90),
        (400, 90),
    ]
    for a, b in zip(pts, pts[1:]):
        move_line(a[0], a[1], b[0], b[1])

while True:
    move_rectangle()
    move_circle()
    move_triangle()
