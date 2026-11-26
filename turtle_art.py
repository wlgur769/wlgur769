import turtle

# 설정
ARM = 260        # 가지 길이
DEPTH = 3        # 세밀함 (클수록 오래 걸림)

screen = turtle.Screen()
screen.setup(820, 820)
screen.bgcolor("#0b1730")
screen.title("Snowflake")
screen.delay(0)

t = turtle.Turtle()
t.shape("turtle")
t.color("white")
t.speed(0)       # 1~10: 느림~빠름, 0: 가장 빠름
t.penup()

COLORS = ["#ffffff", "#cdeeff", "#94d3ff", "#62b5ee"]

def branch(length, depth):
    # 가지 하나 + 좌우 곁가지 (재귀)
    t.pencolor(COLORS[DEPTH - depth])
    t.width(depth + 1)
    if depth == 0:
        t.forward(length)
        t.backward(length)
        return

    n = 5 if depth == DEPTH else 3          # 곁가지 개수
    seg = length / (n + 1)
    for i in range(1, n + 1):
        t.forward(seg)
        side = length * 0.42 * (1 - i / (n + 1))   # 끝으로 갈수록 짧게
        t.left(60)
        branch(side, depth - 1)
        t.right(120)
        branch(side, depth - 1)
        t.left(60)
        t.pencolor(COLORS[DEPTH - depth])
        t.width(depth + 1)
    t.forward(seg)
    if depth == DEPTH:
        t.dot(8, "#ffffff")                  # 끝 장식
    t.backward(length)

def hexagon(size, color, w):
    # 중심 기준 육각형
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.forward(size)
    t.setheading(120)
    t.pendown()
    t.pencolor(color)
    t.width(w)
    for _ in range(6):
        t.forward(size)
        t.left(60)
    t.penup()

# 1. 중심 육각판
for s, c in [(60, "#5aaee8"), (45, "#a9ddff"), (30, "#ffffff")]:
    hexagon(s, c, 2)

# 2. 큰 가지 6개
for k in range(6):
    t.goto(0, 0)
    t.setheading(90 + k * 60)
    t.pendown()
    branch(ARM, DEPTH)
    t.penup()

# 3. 가지 사이 작은 가지 6개
for k in range(6):
    t.goto(0, 0)
    t.setheading(120 + k * 60)
    t.pendown()
    branch(ARM * 0.35, DEPTH - 1)
    t.penup()

t.goto(0, 0)
t.hideturtle()
turtle.done()