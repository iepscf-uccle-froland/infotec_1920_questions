from turtle import *
from math import sin , cos, pi

def hexagone(point, longueur, col, centre, rayon ) :
    color(col[0])
    begin_fill()
    a = pi / 3
    rayon = 50

    goto(point)
    goto(int(rayon * cos(0 * a)), int(rayon * sin(0 * a)))
    goto(int(rayon * cos(1 * a)), int(rayon * sin(1 * a)))
    goto(int(rayon * cos(2 * a)), int(rayon * sin(2 * a)))
    goto(point)
    end_fill()

    begin_fill()
    color(col[1])
    goto(point)
    goto(int(rayon * cos(0 * a)), int(rayon * -sin(0 * a)))
    goto(int(rayon * cos(1 * a)), int(rayon * -sin(1 * a)))
    goto(int(rayon * cos(2 * a)), int(rayon * -sin(2 * a)))
    goto(point)
    end_fill()

    begin_fill()
    color(col[2])
    goto(int(rayon * cos(2 * a)), int(rayon * sin(2 * a)))
    goto(int(rayon * cos(3 * a)), int(rayon * sin(3 * a)))
    goto(int(rayon * cos(4 * a)), int(rayon * sin(4 * a)))
    goto(point)
    end_fill()

    done()


hexagone((0,0), 50, ('blue', 'yellow', 'green'), (0,0,0), 0)

def pavage (inf_gauche, sup_droit, longueur, col, centre, rayon):
    c = 1
    a = pi/3
    sup_d = sup_droit
    es_p = 3 * longueur
    inf_g = inf_gauche
    p_depart = int(inf_gauche - longueur * ( 1 + cos(a)))
    p_final = int (sup_droit + longueur * ( 1 + cos(a)))

    while p_final > p_depart:
        print (p_depart , p_final)
        if c % 2 != 0:
        for i in range (inf_gauche , sup_droit , es_p):
            hexagone((0, 0), 50, ('blue', 'yellow', 'green'), (0, 0, 0), 0)
