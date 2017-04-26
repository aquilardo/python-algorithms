"""
Ejercicio 5: 
PSEUDOCODIGO
---------------------------
1. INICIO
2. mostrar 'Ingrese el numero'
3. a <- leer numero
4. i <- 1
5. mientras i<=a
    si a mod i == 0
        imprimir (i + '-')
    i = i + 1
6. FIN
-----------------------------
"""

print("Ingrese el numero")
a = int(input())
i = 1
while (i<=a):
    if (a%i == 0):
        print(i, end='-'),
    i = i + 1