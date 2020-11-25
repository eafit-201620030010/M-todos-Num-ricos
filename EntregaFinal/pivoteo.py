#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from functions import *

def pivoteoParcial(Ab, k, n):

    mayor = math.fabs(Ab[k][k])
    filaMayor = k

    for i in range(k + 1, n):

        if math.fabs(Ab[i][k]) > mayor:

            mayor = Ab[i][k]
            filaMayor = i

    if mayor == 0:

        print("El sistema no tiene solución única.")

    elif filaMayor != k:

        intercambiarFilas(Ab, k, filaMayor)

    return filaMayor

def pivoteoTotal(Ab, k, n, marcas):
 
    mayor = 0

    filaMayor = k
    columnaMayor = k

    for i in range(k, n):
        for j in range(k, n):

            if math.fabs(Ab[i][j]) > mayor:

                mayor = math.fabs(Ab[i][j])
                filaMayor = i
                columnaMayor = j

    if mayor == 0:

        print("El sistema no tiene solución única.")

    else:

        if filaMayor != k: 

            intercambiarFilas(Ab, k, filaMayor)

        if columnaMayor != k:

            intercambiarColumnas(Ab, k, columnaMayor, marcas)

    return [filaMayor, columnaMayor]
