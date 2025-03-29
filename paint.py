import turtle
import tkinter as tk
from tkinter import colorchooser

# Настройка экрана
screen = turtle.Screen()
screen.title("Python Turtle Paint")
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Создаем черепашку для рисования
pen = turtle.Turtle()
pen.shape("circle")
pen.shapesize(0.5)
pen.speed(0)
pen.width(3)
pen.penup()  # Поднимаем перо вначале

# Создаем черепашку для отображения текущего цвета
color_indicator = turtle.Turtle()
color_indicator.shape("square")
color_indicator.shapesize(2)
color_indicator.penup()
color_indicator.goto(-350, 250)

# Переменные
current_color = "black"
current_width = 3
is_drawing = False
eraser_mode = False
update_lock = False  # Блокировка для предотвращения рекурсии

# Функции
def start_drawing(x, y):
    global is_drawing
    is_drawing = True
    pen.pendown()
    pen.goto(x, y)

def stop_drawing(x, y):
    global is_drawing
    is_drawing = False
    pen.penup()

def draw(x, y):
    global update_lock
    if is_drawing and not update_lock:
        try:
            update_lock = True
            if eraser_mode:
                original_color = pen.color()[0]
                pen.color("white")
                pen.goto(x, y)
                pen.color(original_color)
            else:
                pen.goto(x, y)
        finally:
            update_lock = False

def change_color():
    global current_color, eraser_mode
    eraser_mode = False
    # Используем tkinter для выбора цвета
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    color = colorchooser.askcolor(title="Выберите цвет")
    if color[1]:
        current_color = color[1]
        pen.color(current_color)
        color_indicator.color(current_color)

def eraser():
    global eraser_mode
    eraser_mode = True

def increase_width():
    global current_width, update_lock
    if not update_lock:
        try:
            update_lock = True
            current_width += 1
            pen.width(current_width)
        finally:
            update_lock = False

def decrease_width():
    global current_width, update_lock
    if not update_lock and current_width > 1:
        try:
            update_lock = True
            current_width -= 1
            pen.width(current_width)
        finally:
            update_lock = False

def clear_screen():
    pen.clear()

def save_drawing():
    # Получаем холст turtle
    canvas = screen.getcanvas()
    # Сохраняем рисунок как PostScript файл
    canvas.postscript(file="drawing.eps", colormode='color')
    print("Рисунок сохранен как drawing.eps")

# Настройка событий
screen.listen()
screen.onscreenclick(start_drawing, 1)  # Левая кнопка мыши
screen.onscreenclick(stop_drawing, 3)   # Правая кнопка мыши
pen.ondrag(draw)  # Используем ondrag для плавного рисования

# Настройка горячих клавиш
screen.onkey(change_color, "c")
screen.onkey(eraser, "e")
screen.onkey(increase_width, "+")
screen.onkey(decrease_width, "-")
screen.onkey(clear_screen, "space")
screen.onkey(save_drawing, "s")

# Инструкция
instructions = turtle.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.goto(-350, -280)
instructions.write(
    "Инструкция:\n"
    "ЛКМ - рисовать\n"
    "ПКМ - остановить рисование\n"
    "C - выбрать цвет\n"
    "E - ластик\n"
    "+/- - изменить размер кисти\n"
    "Пробел - очистить экран\n"
    "S - сохранить рисунок",
    font=("Arial", 10, "normal")
)

# Инициализация
pen.color(current_color)
color_indicator.color(current_color)

# Главный цикл
turtle.done()
