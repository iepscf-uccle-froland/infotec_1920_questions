from turtle import *
from math import pi, sin, cos

ANGLE = pi / 3


def hexagone(point, longueur, col):
    x = point[0]
    y = point[1]

    up()
    goto(x, y)
    down()

    color(col[0])
    begin_fill()
    goto(x + longueur * cos(0 * ANGLE), (y + longueur * sin(0 * ANGLE)))
    goto(x + longueur * cos(1 * ANGLE), (y + longueur * sin(1 * ANGLE)))
    goto(x + longueur * cos(2 * ANGLE), (y + longueur * sin(2 * ANGLE)))
    goto(x + longueur * 0 * cos(0 * ANGLE), (y + longueur * 0 * sin(0)))
    end_fill()

    color(col[1])
    begin_fill()
    goto((x + longueur * cos(0 * ANGLE)), (y + longueur * -sin(0 * ANGLE)))
    goto(x + longueur * cos(1 * ANGLE), (y + longueur * -sin(1 * ANGLE)))
    goto(x + longueur * cos(2 * ANGLE), y + longueur * -sin(2 * ANGLE))
    goto(x + longueur * 0 * cos(0 * ANGLE), (y + longueur * 0 * sin(0)))
    end_fill()

    color(col[2])
    begin_fill()
    goto(x + longueur * cos(2 * ANGLE), (y + longueur * sin(2 * ANGLE)))
    goto(x + longueur * cos(3 * ANGLE), (y + longueur * sin(3 * ANGLE)))
    goto(x + longueur * cos(4 * ANGLE), (y + longueur * sin(4 * ANGLE)))
    goto(x + longueur * 0 * cos(0 * ANGLE), (y + longueur * 0 * sin(0)))
    end_fill()


col = ("green", "yellow", "blue")
inf_gauche = -315
sup_droit = 315
centre = (-50, - 50, -50)
point = -315, -315
longueur = 30
hexagone(point, longueur, col)

done()
