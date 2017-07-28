#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1827

def PrettyPrint(table, justify = "R", columnWidth = 0):
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

while True:
    ordem = int(input(""))
    if ordem == 0:
        break
    if ordem >= 16:
        ordem = int(input(""))
    else:
        if ordem==1:
            val = 1
            print("%1d\n"%val)
        else:
            matriz = []
            maior = 0
            for i in range(ordem):
                linha = []
                for j in range(ordem):
                    termo = 2**(i+j)
                    if termo>maior:
                        maior = termo
                    linha.append(termo)
                matriz.append(linha)
            # maior = str(maior)
            # tam = len(maior)
            print(PrettyPrint(matriz))