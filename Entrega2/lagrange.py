import numpy as np
import tabulate as tb
from tabulate import tabulate
from sympy import *
tb.PRESERVE_WHITESPACE = True

x = symbols('x')
init_printing(use_unicode=False)

def lagrange(puntos):
	print('---puntos---')
	print(puntos)
	print()
	tabla = []

	sum = sympify(0)
	print('---Lk(x) (Opcional)---')
	for k in range(0, len(puntos)):
		numerador = sympify(1)
		denominador = sympify(1)
		for n in range(0, len(puntos)):
			if n != k:
				numerador *= sympify('x - ' + str(puntos[n][0]))
				denominador *= sympify(str(puntos[k][0]) + ' - ' + str(puntos[n][0]))
		lk = numerador / denominador
		print('L' + str(k) + '(x) = ' + str(lk))

		sum += sympify(lk * puntos[k][1])
	print()
	print('---Polinomio expandido---')
	print(pretty(sum))
	print()
	poli = simplify(sum)
	print('---Polinomio simplificado---')
	print(pretty(poli))
	print()


puntos = [[-1,15.5],[0,3],[3,8],[4,1]]

lagrange(puntos)
