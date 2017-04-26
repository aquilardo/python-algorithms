"""
Ejercicio 10: 
PSEUDOCODIGO
---------------------------
1. INICIO
2. leer num1
3. leer num2
4. a <- num1
5. b <- num2
6. resto <- 0
7. mientras b > 0
    resto <- b
    b <- a mod b
    a <- resto
8. imprimir 'El maximo comun divisor de num1 y num2 es a'
9. FIN
-----------------------------
"""

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
a = num1
b = num2
resto = 0
while (b > 0):
    resto = b
    b = a % b
    a = resto

print("El máximo común divisor de ", num1, " y ", num2, " es ", a)