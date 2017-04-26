"""
Ejercicio 9: 
PSEUDOCODIGO
---------------------------
1. INICIO
2. leer numero decimal
3. binario <- ' '
4. mientras decimal div 2 diferente de 0
    binario <- cadena (decimal mod 2) + binario
    decimal <- decimal div 2
5. imprimir cadena(decimal)+binario
6. FIN
-----------------------------
"""

decimal = int(input('Introduce el número a convertir a binario: '))
binario = ''
while decimal // 2 != 0:
    binario = str(decimal % 2) + binario
    decimal = decimal // 2
print(str(decimal)+binario)
