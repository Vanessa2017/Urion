#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1575

def imprime_matriz(matriz,T):
    ordem = len(matriz)
    string =" "
    if ordem!=2:
        for i in range(ordem):
            for j in range(ordem):
                tam_e = len(str(matriz[i][j]))
                menos = tam_e-1
                if j == 0:
                    if tam_e < T:
                        print("%s%d"%(string*(T-menos-1),matriz[i][j]),end="")
                    else:
                        print("%s%d"%(string*(T-2-(tam_e-2)),matriz[i][j]),end="")
                elif j == ordem-1:
                    if tam_e < T:
                        print(" %s%d"%(string*(T-menos-1),matriz[i][j]))
                    else:
                        print(" %s%d"%(string*(T-2-(tam_e-2)),matriz[i][j]))
                else:
                    if tam_e < T:
                        print(" %s%d"%(string*(T-menos-1),matriz[i][j]),end ="")
                    else:
                        print(" %s%d"%(string*(T-2-(tam_e-2)),matriz[i][j]),end ="")
    else:
        print("1 2\n2 4")
    print("")
while True:
    ordem = int(input(""))
    if ordem == 0:
        break
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
            maior = str(maior)
            tam = len(maior)
            imprime_matriz(matriz,tam)