#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Neste programa seu trabalho é ler um valor inteiro que será o tamanho da
matriz quadrada (largura e altura) que será preenchida da seguinte forma: a
parte externa é preenchida com 0, a parte interna é preenchida com 1, a diagonal
principal é preenchida com 2, a diagonal secundária é preenchida com 3 e o ponto
central contém o valor 4, conforme os exemplos abaixo."""

while True:
    try:
        l=[]
        n=int(input())
        for i in range(n):
            l.append([0]*n)
        ini, fim=int(n/3), (n-(int(n/3)))

        if (5<=n<=101) and (n%2!=0):
            for i in range(n):
                for j in range(n):
                    if ((i<ini) or (i>=fim)):
                        if i==j:
                            l[i][j]=2
                        elif (j==(n-1-i)):
                            l[i][n-1-i]=3
                    elif (i>=ini) or (i<fim):
                        if (ini<=j<fim):
                            l[i][j]=1
                        if i==int(n/2) and j==int(n/2):
                            l[int(n/2)][int(n/2)]=4
                    print (l[i][j], end = "")
                    if j==(len(l)-1):
                        print()
        print()
    except:
        break