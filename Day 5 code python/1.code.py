from turtle import *
import colorsys

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

hideturtle()
penup()

text = "Aditya"
font_size = 88
goto(0, 0)

h = 0.6  # blue range

while True:
    clear()

    # glow layers
    for i in range(8, 0, -1):
        color(colorsys.hsv_to_rgb(h, 0.6, 0.3))
        goto(0, -i)
        write(text, align="center",
              font=("Arial", font_size, "bold"))

    # main bright text
    goto(0, 0)
    color(colorsys.hsv_to_rgb(h, 1, 1))
    write(text, align="center",
          font=("Arial", font_size, "bold"))

    h += 0.002
    if h > 0.75:
        h = 0.6

    screen.update()