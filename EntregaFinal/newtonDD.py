import numpy as np
import tabulate as tb
from tabulate import tabulate
from sympy import *
tb.PRESERVE_WHITESPACE = True

x = symbols('x')
init_printing(use_unicode=False)

def newtonDD(puntos):
	print('---puntos---')
	print(puntos)
	print()
	grado = len(puntos) - 1
	tabla = []
	for i in range(0,len(puntos)):
		tabla.append([i,puntos[i][0],puntos[i][1]])
		for j in range(0,i):
			rowAnt = i - j - 1
			col = j + 2		
			value = ((tabla[i][col] - tabla[i-1][col])/(tabla[i][1] - tabla[rowAnt][1]))
			tabla[i].append(value)

	print('---Tabla de diferencias---')
	print(tabulate(tabla, floatfmt = '.6f', 
		headers=['n','xi','1ra','2da','3ra','4ta','5ta','6ta','7ma','8va','9na','10ma']))
	print()
	expr = sympify('0')

	for i in range(0,len(tabla)):
		c = tabla[i][-1]
		factor = sympify('1')
		for j in range(0,i):
			factor *= sympify('x - ' + str(tabla[j][1]))
		expr += c * factor
	print('---Polinomio expandido---')
	print(pretty(expr))
	print()
	print('---Polinomio simplificado---')
	expr = simplify(expr)
	print(pretty(expr))
	print()	

#puntos = [[1,0.6747],[1.2,0.8491],[1.4,1.1214],
#[1.6,1.4921],[1.8,1.9607],[2,2.5258]]
puntos = [[-1,15.5],[0.0,3.0],[3.0,8.0],[4,1.0]]


newtonDD(puntos)