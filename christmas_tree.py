import turtle as t
from time import sleep
import pygame

from path import get_resource_path
from tree_part import draw_tree_part as dtp
from draw_snowflake import sideflake

pygame.mixer.init()
sound = pygame.mixer.Sound(get_resource_path('music/merry_christmas.mp3'))
sound.play(-1)

screen = t.Screen()
screen.setup(800, 650)
screen.colormode(255)

circle = t.Turtle('circle')
circle.color('red')
circle.speed(5)
circle.up()

square = t.Turtle('square')
square.color('green')
square.speed(5)
square.up()

circle.goto(0, 300)
circle.stamp()

body_part = 3
for i in range(body_part): # i 画的场次-1
    xsquare = 0
    ysquare = 270 - i * 120
    dtp(square, circle, xsquare, ysquare, i+1)

square.goto(0, 270 - body_part * 120)
square.color((255, 153, 18))
for i in range(6):
    sleep(0.45)
    square.goto(0, 270 - body_part * 120 - i * 30)
    square.stamp()

text = t.Turtle()
text.hideturtle()
text.penup()
text.goto(60, -200)
text.color('red')
wish = '圣诞快乐~~'

for i in wish:
    text.write(i, font=("youyuan", 30, "normal"))
    text.fd(60)
    sleep(0.2)

snow = t.Turtle()
snow.up()
snow.hideturtle()
snow.goto(-350, 200)
snow.color((0, 255, 255))
snow.down()
snow.speed('fastest')
for i in range(3):
    sideflake(snow, 80, 4)
    snow.right(120)

snow.up()
snow.goto(270, 200)
snow.down()
for i in range(3):
    sideflake(snow, 80, 4)
    snow.right(120)

text.color((138, 43, 226))
text.goto(-350, -280)
text.write('created by 尧')

t.done()

