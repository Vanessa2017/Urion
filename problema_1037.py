#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Você deve fazer um programa que leia um valor qualquer e apresente
uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50],
(50,75], (75,100]) este valor se encontra. Obviamente se o valor não 
estiver em nenhum destes intervalos, deverá ser impressa a mensagem 
“Fora de intervalo”.'''

import os
os.system('clear')

valores = float(input())

if valores < 0:
	print("Fora de intervalo")
elif valores <= 25.00:
	print("Intervalo [0,25]")
elif valores <= 50.00:
	print("Intervalo (25,50]")
elif valores <= 75.00:
	print("Intervalo (50,75]")
elif valores <= 100.00:
	print("Intervalo (75,100]")
else:
	print("Fora de intervalo")

	
