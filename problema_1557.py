#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1575

l=[]
def preenche(n):
    for i in range(n):
        l.append([])
        for j in range(n):
            if (i==0) and (j==0):
                l[i].append(1)
            elif (i>0) and (j==0):
                l[i].append((l[i-1][j])*2)
            else:
                l[i].append((l[i][j-1])*2)

# Pretty Print table in tabular format
def PrettyPrint(table, justify = "R", columnWidth = 0):
    # Not enforced but
    # if provided columnWidth must be greater than max column width in table!
    if columnWidth == 0:
        # find max column width
        for row in table:
            for col in row:
                width = len(str(col))
                if width > columnWidth:
                    columnWidth = width

    outputStr = ""
    for row in table:
        rowList = []
        for col in row:
            if justify == "R": # justify right
                rowList.append(str(col).rjust(columnWidth))
            elif justify == "L": # justify left
                rowList.append(str(col).ljust(columnWidth))
            elif justify == "C": # justify center
                rowList.append(str(col).center(columnWidth))
        outputStr += ' '.join(rowList) + "\n"
    return outputStr

n=int(input())
while True:
    if n == 0:
        break
    elif n <= 15:
        preenche(n)
        print(PrettyPrint(l,"R"))
        l=[]
        n=int(input())
    else:
        n = int(input())