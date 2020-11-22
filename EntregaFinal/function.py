import math

def f(x): return math.pow(x, 2) + 1

def fd(x): return 2 * x

def fdd(x): return 2

def g(x): return (x * math.exp(x) - math.pow(x, 2) - 3) / 5
