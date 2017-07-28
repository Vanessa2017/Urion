#!/usr/bin/env python3
# -*- coding: utf-8 -*-
<<<<<<< HEAD
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1478

matrix = tuple(' '.join('{:>3}'.format(abs(i - j) + 1) for j in range(101)) for i in range(101))

while True:
    size = int(input())
    if size == 0:
        break
    width = 4 * size - 1
    for i in range(size):
        print(matrix[i][:width])
    print()
        
=======

from math import ceil
user = -1

while user != 0:

    user = int(input())
    while user < 0 or user > 100:
        user = int(input())

    if user >= 1:
        matrix = [[(0) for row in range(user)] for column in range(user)]
        ceiling = int(ceil(user/2.0))
        for c in range(1, ceiling + 1):
            for i in range(user):
                for j in range(user):
                    matrix[i][j] = abs(i-j) + 1

    for i in matrix:
        for item in i:
            print('  %i' % item,end="")
        print()
    print()
>>>>>>> 6d36efedddaa2f37d711f4fdcb9249389e49552c
