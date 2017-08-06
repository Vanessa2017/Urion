#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A entrada consiste apenas de três inteiros, A, B e C (-100 ≤ A, B, C ≤ 100), os quais representam respectivamente as
temperaturas registradas no 1º, no 2º e no 3º dias."""


wert = input()
A,B,C = wert.split()
a = int(A)
b = int(B)
c = int(C)

if a > b < c:
    '''Se a temperatura desceu do 1º para o 2º dia, mas subiu ou permaneceu constante do 2º para o 3º, as pessoas ficam 
    felizes (primeira figura).'''
    if (a - b) > (b - c):
        '''Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º menos do que subira 
        do 1º para o 2º, as pessoas ficam tristes (terceira figura).'''
        print(":(")
    elif (a - b) == (b - c):
        '''Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º no mínimo o tanto que
         subira do 1º para o 2º, as pessoas ficam felizes (quarta figura)'''
        print(':)')
    else:
        print(":)")
elif a < b >= c:
    '''Se a temperatura subiu do 1º para o 2º dia, mas desceu ou permaneceu constante do 2º para o 3º, as pessoas ficam 
    tristes (segunda figura).'''
    print(':)')
        print(':(')
elif a < b < c:
    if (a - b) > (b - c):
        '''Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º menos do que 
        descera do 1º para o 2º, as pessoas ficam felizes (quinta figura).'''
        print(':)')
    elif (a - b) >= (b - c):
        '''Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º no mínimo o tanto que
        descera do 1º para o 2º, as pessoas ficam tristes (sexta figura).'''
        print(':)')
    else:
        print(':(')

else:
    print(":(")





