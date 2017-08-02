#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Para aquecer você para esta competição, vamos pedir que você desenvolva um programa que calcule o quociente e o resto
da divisão de dois números inteiros, pode ser? Lembre que o quociente e o resto da divisão de um inteiro a por um
inteiro não-nulo b são respectivamente os únicos inteiros q e r tais que 0 ≤ r < |b| e:"""

def euclides(a,b):
    if (a < 0) and (b < 0):
        abteilung = divmod(abs(a), b)
        return abs(abteilung[0]), abs(abteilung[1])

    elif (a < 0):
        abteilung = divmod(abs(a), -(b))
        return abteilung[0], abs(abteilung[1])

    elif (b < 0):
        abteilung = divmod(-(a), b)
        return abteilung[0] * (-1), abs(abteilung[1])

    else:
        abteilung = divmod(a, b)
        return abteilung[0], abs(abteilung[1])

wert = input()
A,B = wert.split()
a = int(A)
b = int(B)
matrix = (euclides(a, b))
print("%d %d" %(matrix[0],matrix[1]))







