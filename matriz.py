#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import random

class Matriz(object):

    def __init__(self, filas=None, columnas=None):
        if filas:
            self.filas=filas
        else:
            self.filas=int(raw_input("ingrese numero de filas: "))
        if columnas:
            self.columnas= columnas
        else:
            self.columnas = int(raw_input("ingrese numero de columnas: "))

    def crearMatrizA(self):
        self.matriz=[]
        for f in range(self.filas):
            self.matriz.append([0]*self.columnas)

    def llenarmatrizA(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = random.randint(1,20)
                #int(raw_input("ingrese %d, %d: " % (f, c)))
        return self.matriz

    def imprime_matriz(self):
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == self.columnas - 1:
                    cadena = cadena + str(self.matriz[i][j]) + "\n"
                else:
                    cadena = cadena + str(self.matriz[i][j]) + "  "

        print "Matriz uno: "+'\n' + cadena

    def imprime_matrizC(self):
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == self.columnas - 1:
                    cadena = cadena + str(self.matriz[i][j]) + "\n"
                else:
                    cadena = cadena + str(self.matriz[i][j]) + "  "

        print "Matriz dos: "+'\n' + cadena

    def imprime_matrizB(self,matrizB):
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == self.columnas - 1:
                    cadena = cadena + str(matrizB[i][j]) + "\n"
                else:
                    cadena = cadena + str(matrizB[i][j]) + "  "
        return cadena

    def matriz_det(self,b):

        if (self.filas != self.columnas):
            print "la matriz no es cuadrada: "
            return True
        elif self.filas==2:
                a=1
                b=1
                for f in range(self.filas):
                    for c in range(self.columnas):
                        if f==c:
                            a*=self.matriz[f][c]
                        else:
                            b*=self.matriz[f][c]
                det=a-b

                print "la determinante es: "+str(det)
                return det
        else:
                m = self.matrizcopy(b)
                n = len(m)
                det = 1
                for i in range(n):
                    j = self.primeroNoNulo(m,i)
                    if j == n:
                        return 0
                    if i != j:
                        det = -1 * det
                        self.intercambiaFilas(m, i, j)
                    det = det * m[i][i]
                    self.multiplicaFila(m, i, 1. / m[i][i])
                    for k in range(i + 1, n):
                        self.combinacion(m, i, k, -m[k][i])

                print "La determinante es: " + str(det)
                return det

    def matrizcopy(self, matriz):
        self.result = []
        for f in matriz:
            self.result.append(f[:])
        return self.result

    def primeroNoNulo(self,m,i):
        result = i
        while result < len(m) and m[result][i] == 0:
            result = result + 1
        return result

    def intercambiaFilas(self, m,i,j):
        m[i], m[j] = m[j], m[i]

    def multiplicaFila(self, m, f, e):

        n = len(m)
        for c in range(n):
            m[f][c] = m[f][c] * e

    def transpuesta(self):

        self.matrizB = []
        for f in range(self.columnas):
            self.matrizB.append([0] * self.filas)

        for i in range(self.filas):
            for j in range(self.columnas):
                self.matrizB[j][i] = self.matriz[i][j]

        a=self.imprime_matrizB(self.matrizB)
        print "Matriz Transpuesta: " + '\n' + a
        return self.matrizB

    def matriz_numero(self):
            self.matrizB = []
            for f in range(self.columnas):
                self.matrizB.append([0] * self.filas)
            a = int(raw_input("ingrese numero: "))
            for i in range(self.filas):
                for j in range(self.columnas):
                    self.matrizB[i][j]= self.matriz[i][j]*a
            b = self.imprime_matrizB(self.matrizB)
            print "el resultado es: " + '\n' + b

    def matriz_elevada(self):

        self.matrizC = []
        for i in range(self.filas):
            self.matrizC.append([0] * self.columnas)
        a = int(raw_input("ingrese la potencia: "))

        if a==2:
            for i in range(self.filas):
                for j in range(self.columnas):
                    for k in range(self.columnas):
                        self.matrizC[i][j] += self.matriz[i][k] * self.matriz[k][j]

            b = self.imprime_matrizB(self.matrizC)
            print "Matriz Elevada Potencia: " + str(a) + '\n' + b

        if a==3:
            self.matrizD = []
            for i in range(self.filas):
                self.matrizD.append([0] * self.columnas)

            for i in range(self.filas):
                for j in range(self.columnas):
                    for k in range(self.columnas):
                        self.matrizC[i][j] += self.matriz[i][k] * self.matriz[k][j]

            for i in range(self.filas):
                for j in range(self.columnas):
                    for k in range(self.columnas):
                        self.matrizD[i][j] += self.matrizC[i][k] * self.matriz[k][j]

            b = self.imprime_matrizB(self.matrizD)
            print "El Resultado es: " + str(a) + '\n' + b

    def matrizSimet(self):

        self.matriz=[]

        for f in range(self.filas):
            auxiliar = []
            for c in range(self.columnas):
                elemento = int(raw_input("ingrese %d, %d: " % (f, c)))

                auxiliar.append(elemento)
            self.matriz.append(auxiliar)

        a =self.imprime_matrizB(self.matriz)
        print "Matriz Original: "+ '\n' + a

        matriz_T= self.transpuesta()

        if matriz_T == self.matriz:
            print "es una matriz simetrica:"
        else:
            print "no es una matriz simetrica:"


    def matrizidentica(self):

        self.matriz = []

        for f in range(self.filas):
            auxiliar = []
            for c in range(self.columnas):
                elemento = int(raw_input("ingrese %d, %d: " % (f, c)))

                auxiliar.append(elemento)
            self.matriz.append(auxiliar)

        a = self.imprime_matrizB(self.matriz)
        print "Matriz Original: " + '\n' + a

        if (self.filas != self.columnas):
            print "no se puede hallar la matriz identica:"

        else:

            self.matrizI=[]
            for i in range(self.filas):
                self.matrizI.append([0] * self.columnas)

            for f in range(self.filas):
               for c in range(self.columnas):
                    if f == c:
                        self.matrizI[f][c]=1
                    else:
                        self.matrizI[f][c]= 0

            b = self.imprime_matrizB(self.matrizI)
            print "la matriz Matriz Identica: " + '\n' + b

    def multmatriz(self, filasA, columnasB, filasB,columnasA,matrizA,matrizB):

        if (filasB != columnasA):
            print "no se puede realizar la operacion"
        else:
            self.matrizC = []
            for i in range(filasA):
                self.matrizC.append([0] * columnasB)

            for i in range(filasA):
                for j in range(columnasB):
                    for k in range(filasB):
                        self.matrizC[i][j] += matrizA[i][k] * matrizB[k][j]

            b = self.imprime_matrizB(self.matrizC)
            print "la Matriz Resultado: " + '\n' + b

    def sumamatriz(self, filasA, columnasB, filasB,columnasA,matrizA,matrizB):

        if (filasA == filasB and columnasA == columnasB):

            self.matrizC = []
            for i in range(filasA):
                self.matrizC.append([0] * columnasB)

            for i in range(filasA):
                for j in range(columnasA):
                        self.matrizC[i][j] = matrizA[i][j] + matrizB[i][j]

            b = self.imprime_matrizB(self.matrizC)
            print "la Matriz Resultado: " + '\n' + b

        else:
            print "no se puede realizar la operacion:"

    def restamatriz(self, filasA, columnasB, filasB,columnasA,matrizA,matrizB):

        if (filasA == filasB and columnasA == columnasB):

            self.matrizC = []
            for i in range(filasA):
                self.matrizC.append([0] * columnasB)

            for i in range(filasA):
                for j in range(columnasA):
                        self.matrizC[i][j] = matrizA[i][j] - matrizB[i][j]

            b = self.imprime_matrizB(self.matrizC)
            print "la Matriz Resultado: " + '\n' + b

        else:
            print "no se puede realizar la operacion:"

    def getFilas(self):
        return self.filas

    def getColumnas(self):
        return self.columnas
