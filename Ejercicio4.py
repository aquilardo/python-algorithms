"""
Ejercicio 4: 
PSEUDOCODIGO
---------------------------
1. INICIO
2. mostrar 'Ingrese la lista de numeros separados por un espacio'
3. mylist <- asignar la lista de números en un arreglo
4. para x en mylist
    a <- 0
    b <- entero x
    mientras a < b
        imprimir '*' hasta que se encuentre esapacio
        a <- a+1
    imprimir espacio
5. FIN
-----------------------------
"""
print("Ingrese la lista de numeros separados por un espacio")
mylist = list(map(int,input().split()))
for x in mylist:
    a = 0
    b = int(x)
    while (a<b):
        print("*", end='')
        a = a+1
    print('')