#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import ceil
user = -1

while user != 0:

    user = int(input())
    while user < 0 or user > 100:
        user = int(input())

    if user >= 1:
        matrix = [[(0) for row in range(user)] for column in range(user)]
        ceiling = (user+1)//2
        for c in range(1, ceiling + 1):
            for i in range(user):
                for j in range(user):
                    matrix[i][j] = abs(i-j) + 1

    for i in matrix:
        for item in i:
            print('  %i' % item,end="")
        print()
    print()

    