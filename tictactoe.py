import turtle
import tkinter as tk
from tkinter import simpledialog

t = turtle.Pen()
t.speed(0)
t.up()

def draw_board():
    t.goto(-50, 150)
    t.down()
    t.goto(-50, -150)
    t.up()
    t.goto(50, 150)
    t.down()
    t.goto(50, -150)
    t.up()
    t.goto(-150, 50)
    t.down()
    t.goto(150, 50)
    t.up()
    t.goto(-150, -50)
    t.down()
    t.goto(150, -50)
    t.up()

def check_win(player):
    win_conditions = [
        [q1, q2, q3], [q4, q5, q6], [q7, q8, q9],
        [q1, q4, q7], [q2, q5, q8], [q3, q6, q9],
        [q1, q5, q9], [q3, q5, q7]
    ]
    for condition in win_conditions:
        if all(cell == player for cell in condition):
            return True
    return False

def draw_x(x, y):
    t.goto(x - 40, y + 40)
    t.down()
    t.goto(x + 40, y - 40)
    t.up()
    t.goto(x + 40, y + 40)
    t.down()
    t.goto(x - 40, y - 40)
    t.up()

def draw_o(x, y):
    t.goto(x, y - 40)
    t.down()
    t.circle(40)
    t.up()

q1 = q2 = q3 = q4 = q5 = q6 = q7 = q8 = q9 = ''

draw_board()

def get_input(player):
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askinteger("Ввод", f"Ход {player}: Введите номер клетки (1-9):")

while True:
    XxX = get_input("X")
    if XxX == 1 and q1 == '':
        q1 = 'X'
        draw_x(-100, 100)
    elif XxX == 2 and q2 == '':
        q2 = 'X'
        draw_x(0, 100)
    elif XxX == 3 and q3 == '':
        q3 = 'X'
        draw_x(100, 100)
    elif XxX == 4 and q4 == '':
        q4 = 'X'
        draw_x(-100, 0)
    elif XxX == 5 and q5 == '':
        q5 = 'X'
        draw_x(0, 0)
    elif XxX == 6 and q6 == '':
        q6 = 'X'
        draw_x(100, 0)
    elif XxX == 7 and q7 == '':
        q7 = 'X'
        draw_x(-100, -100)
    elif XxX == 8 and q8 == '':
        q8 = 'X'
        draw_x(0, -100)
    elif XxX == 9 and q9 == '':
        q9 = 'X'
        draw_x(100, -100)
    else:
        continue

    if check_win('X'):
        t.goto(0, -200)
        t.write('X победил!!!', align="center", font=("Arial", 24, "normal"))
        time.sleep(1)
        break

    OoO = get_input("O")
    if OoO == 1 and q1 == '':
        q1 = 'O'
        draw_o(-100, 100)
    elif OoO == 2 and q2 == '':
        q2 = 'O'
        draw_o(0, 100)
    elif OoO == 3 and q3 == '':
        q3 = 'O'
        draw_o(100, 100)
    elif OoO == 4 and q4 == '':
        q4 = 'O'
        draw_o(-100, 0)
    elif OoO == 5 and q5 == '':
        q5 = 'O'
        draw_o(0, 0)
    elif OoO == 6 and q6 == '':
        q6 = 'O'
        draw_o(100, 0)
    elif OoO == 7 and q7 == '':
        q7 = 'O'
        draw_o(-100, -100)
    elif OoO == 8 and q8 == '':
        q8 = 'O'
        draw_o(0, -100)
    elif OoO == 9 and q9 == '':
        q9 = 'O'
        draw_o(100, -100)
    else:
        continue

    if check_win('O'):
        t.goto(0, -200)
        t.write('O победил!!!', align="center", font=("Arial", 24, "normal"))
        time.sleep(1)
        break

turtle.done()
