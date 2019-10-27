from turtle import *
from math import pi, sin, cos, sqrt, acos, asin, atan2

def hexagone(point, longueur, col) :
    x = point[0]
    y = point[1]
    color(col[0])
    a = pi / 3
    r = 50
    begin_fill()
    goto(x+r * cos(0 * a), (y+r * sin(0 * a)))
    goto(x+r * cos(1 * a), (y+r * sin(1 * a)))
    goto(x+r * cos(2 * a), (y+r * sin(2 * a)))
    goto(x+r * 0 * cos(0 * a) , (y+r * 0 * sin(0)))
    end_fill()

    begin_fill()
    color(col[1])
    goto((x+r * cos(0 * a)),(y+r * -sin(0 * a)))
    goto(x+r * cos(1 * a), (y+r * -sin(1 * a)))
    goto(x+r * cos(2 * a), y+r * -sin(2 * a))
    goto(x+r * 0 * cos(0 * a) , (y+r * 0 * sin(0)))
    end_fill()

    begin_fill()
    color(col[2])
    goto(x+r * cos(2 * a), (y+r * sin(2 * a)))
    goto(x+r * cos(3 * a), (y+r * sin(3 * a)))
    goto(x+r * cos(4 * a), (y+r * sin(4 * a)))
    goto(x+r * 0 * cos(0 * a) , (y+r * 0 * sin(0)))
    end_fill()

    done()

color1="green"
color2="yellow"
color3="blue"
col = color1,color2,color3
inf_gauche = -315
sup_droit = 315
centre = (-50, - 50 , -50)
point = -315, -315
longueur = 30
hexagone(point, longueur, col)