#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""No oitavo episodio da segunda temporada do seriado The Big Bang Theory, The Lizard-Spock Expansion, Sheldon e Raj
discutem qual dos dois é o melhor: o filme Saturn 3 ou a série Deep Space 9. A sugestão de Raj para a resolução do
impasse é uma disputa de Pedra-Papel-Tesoura. Contudo, Sheldon argumenta que, se as partes envolvidas se conhecem, entre
75% e 80% das disputas de Pedra-Papel-Tesoura terminam empatadas, e então sugere o Pedra-Papel-Tesoura-Lagarto-Spock."""


def sheldon(wert, M, N):
    matriz = [[1, 3, 0, 3, 0],
              [0, 1, 3, 3, 0],
              [3, 0, 1, 0, 3],
              [0, 0, 3, 1, 3],
              [3, 3, 0, 0, 1]]

    matrix = dict(lagarto=0, papel=1, pedra=2, Spock=3, tesoura=4)

    result = matrix[M],matrix[N]

    if matriz[result[0]][result[1]] == 3:
        print("Caso #%s: Bazinga!" %(count))
    elif matriz[result[0]][result[1]] == 1:
        print("Caso #%s: De novo!" %(count))
    else:
        print("Caso #%s: Raj trapaceou!" %(count))

count = 1

wert = int(input())

while wert >= count:
    lets = input()
    M, N = lets.split()
    sheldon(wert, M, N)
    count += 1
