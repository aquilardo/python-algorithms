"""
Ejercicio 8: 
PSEUDOCODIGO
---------------------------
1. INICIO
2. mostrar mensaje 'Ingrese la base'
3. leer a
4. mostrar mensaje 'Ingrese la potencia'
5. leer b
6. aux <- 1
7. resultado <- 1
8. mientras aux <= b
    resultado <- a*resultado
    aux <- aux + 1
9. imprimir resultado
10. FIN
-----------------------------
"""
print("Ingrese la base")
a = int(input())
print("Ingrese la potencia")
b = int(input())
aux = 1
resultado = 1
while (aux <= b):
    resultado = a*resultado
    aux = aux + 1
print(resultado)
