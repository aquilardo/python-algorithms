"""
Ejercicio 7: 
PSEUDOCODIGO
---------------------------
1. INICIO
2. mostrar mensaje 'ingrese numero'
3. leer a
4. suma <- 0
5. aux <- 0
6. mientras a>0
        aux <- a mod 10
        suma <- suma + aux
7. si suma mod 2 == 0
        imprimir 'la suma es par'
   sino
        imprimir 'la suma es impar'
8. FIN
-----------------------------
"""
print("ingrese el número")
a = int(input())
suma = 0
aux = 0
while (a > 0):
    aux = a%10
    suma = suma+aux
    a = int(a/10)
if (suma%2==0):
    print("la suma es par")
else:
    print("la suma es impar")
