from turtle import *
from math import sin, cos, pi

ANGLE = pi / 3


def hexagone(point, longueur, col, centre, rayon):
    x, y = point

    up()
    goto(x, y)
    down()

    color(col[0])
    begin_fill()
    goto(x + int(longueur * cos(0 * ANGLE)), y + int(longueur * sin(0 * ANGLE)))
    goto(x + int(longueur * cos(1 * ANGLE)), y + int(longueur * sin(1 * ANGLE)))
    goto(x + int(longueur * cos(2 * ANGLE)), y + int(longueur * sin(2 * ANGLE)))
    goto(x, y)
    end_fill()

    color(col[1])
    begin_fill()
    goto(x, y)
    goto(x + int(longueur * cos(0 * ANGLE)), y + int(longueur * -sin(0 * ANGLE)))
    goto(x + int(longueur * cos(1 * ANGLE)), y + int(longueur * -sin(1 * ANGLE)))
    goto(x + int(longueur * cos(2 * ANGLE)), y + int(longueur * -sin(2 * ANGLE)))
    goto(x, y)
    end_fill()

    color(col[2])
    begin_fill()
    goto(x + int(longueur * cos(2 * ANGLE)), y + int(longueur * sin(2 * ANGLE)))
    goto(x + int(longueur * cos(3 * ANGLE)), y + int(longueur * sin(3 * ANGLE)))
    goto(x + int(longueur * cos(4 * ANGLE)), y + int(longueur * sin(4 * ANGLE)))
    goto(point)
    end_fill()


def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    deplacement_horizontal = 3 * longueur
    deplacement_vertical = int(longueur * sin(ANGLE))
    ligne = 1

    for y in range(inf_gauche, sup_droit, deplacement_vertical):
        if ligne % 2 == 0:
            decalage_ligne = int(1.5 * longueur)
        else:
            decalage_ligne = 0
        for x in range(inf_gauche + decalage_ligne, sup_droit, deplacement_horizontal):
            hexagone((x, y), longueur, col, centre, rayon)
        ligne = ligne + 1
    done()


pavage(-150, 150, 30, ('blue', 'yellow', 'green'), (0, 0, 0), 0)
