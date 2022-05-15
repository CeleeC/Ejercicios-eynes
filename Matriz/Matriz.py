import os
os.system("cls")
import numpy as np
from numpy import random as rd

#Se genera una matriz de 5x5 con un rango del 1 al 10
matriz = rd.randint(0,10,(5,5))

#Matriz personalizada para ver si funciona.
#matriz = np.array([[1,2,44,4,5],[2,22,8,9,10],[3,12,13,3,15],[4,17,1,19,20],[5,2,23,24,25]])

print(matriz)

def Buscar_secuencia(matriz):
    secuencia = False
    cont = 0
    fila1 = 0
    columna1 = 0
    fila2 = 0
    columna2 = 0
    for fila in range(0,4):
        if(cont == 4):
            break
        cont = 0
        for columna in range(0,4):
            if((matriz[fila][columna] + 1) == matriz[fila][columna + 1]):
                cont +=1
                if(cont == 1):
                    fila1 = fila
                    columna1 = columna
                if(cont == 4):
                    fila2 = fila
                    columna2 = columna
                    secuencia = True

    if(secuencia != True):
        cont = 0
        fila1 = 0
        columna1 = 0
        fila2 = 0
        columna2 = 0
        fila = 0
        columna = 0
        for columna in range(0,4):
            if(cont == 4):
                break
            cont = 0
            for fila in range(0,4):
                if(matriz[fila][columna] == (matriz[fila+1][columna])-1):
                    cont +=1
                    if(cont == 1):
                        fila1 = fila
                        columna1 = columna
                    if(cont == 4):
                        fila2 = fila
                        columna2 = columna
                        secuencia = True

    print()
    if(secuencia):
        print("En la columna (", fila1,") y en la fila (",columna1, "), empieza la secuencia en el número:", matriz[fila1][columna1])
        print("En la columna (", fila2,") y en la fila (",columna2, "), termina la secuencia en el número:", matriz[fila2][columna2])
    else:
        print("No se encontro ninguna secuencia de cuatro (4) números.")

Buscar_secuencia(matriz)