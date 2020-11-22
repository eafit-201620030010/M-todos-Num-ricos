from py_expression_eval import Parser
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

parser = Parser()

x = Symbol('x')

expresion = "3*(x**2)+5*x"

print(parser.parse(expresion).evaluate({"x": 2})

derivada = parse_expr(expresion).diff(x)

print(parser.parse(str(derivada)).evaluate({"x": 2}))

segundaDerivada = parse_expr(str(derivada)).diff(x)

print segundaDerivada

'''

exprConvertida = parser.parse(exprConvertida)

#exprConvertida.evaluate({})

primeraDerivada = parse_expr
#a = parser.parse("x ^ 2 - 3")
ex = parse_expr("x**2-3+5*x")
parser.parse("x**2-3+5*x")
parser.parse(str(ex.diff(x)))
p = ex.diff(x)
segunda = p.diff(x)
print segunda'''
