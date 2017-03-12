import matriz

def main():
    
    lista = ['CALCULADORA MATRICES','     MENU\n''1.Determinante', '2.Transpuesta', '3.inversa', '4.Multiplicar por numero la matriz', '5.Matriz elevada a una Potencia', '6.Matriz Simetrica',
             '7.Matriz Identidad', '8.Multiplicacion', '9.Suma', '10.Resta', '11.Salir']

    for i in lista:
        print i
    p = int(input("Selecione La operacion que Desea calcular: "))
    if p == 1:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a=matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.matriz_det(a)

    if p == 2:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.transpuesta()

    if p == 3:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a=matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.matriz_inversa(a)

    if p == 4:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.matriz_numero()
    if p == 5:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.matriz_elevada()

    if p == 6:
         matrizA = matriz.Matriz()
         matrizA.matrizSimet()

    if p == 7:
         matrizA = matriz.Matriz()
         matrizA.matrizidentica()

    if p == 8:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a=matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprime_matrizC()

         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.multmatriz(filasA,columnasB,filasB,columnasA,a,b)

    if p == 9:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a = matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprime_matrizC()

         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.sumamatriz(filasA, columnasB, filasB, columnasA, a, b)

    if p == 10:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a = matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprime_matrizC()

         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.restamatriz(filasA, columnasB, filasB, columnasA, a, b)

    if p == 11:
        print " salir del menu: "

if __name__ == '__main__':
    main()