"""
Ejercicio 6: 
PSEUDOCODIGO
---------------------------
1. INICIO
2. leer palabra_uno
3. leer palabra_dos
4. array_uno <- []
5. array_dos <- []
6. para x en rango de 1 a 4
        letra_uno <- ultima_letra_palabra_uno
        array_uno <- letra_uno
7. para x en rango de 1 a 4
        letra_dos <- ultima_letra_palabra_dos
        arra_uno <- letra_dos
8. si array_uno[0] == array_dos[]
        si array_uno[1] == array[2]
            si array_uno[2] == array[2]
                imprimir 'Riman'
            sino
                imprimir 'Riman poco'
        sino
            imprimir 'No riman'
    sino
        imprimir 'No riman'
8. FIN
-----------------------------
"""
palabra_uno = input("Escribe una palabra: ")
palabra_dos = input("Escribe otra palabra: ")

array_uno = []
array_dos = []

for x in range(1, 4):
	letra_uno = palabra_uno[(len(palabra_uno)-x)]
	array_uno.append(letra_uno)

for x in range(1, 4):
	letra_dos = palabra_dos[(len(palabra_dos)-x)]
	array_dos.append(letra_dos)


if array_uno[0] == array_dos[0]:
	if array_uno[1] == array_dos[1]:
		if array_uno[2] == array_dos[2]:
			print("Riman")
		else:
			print("Riman un poco")
	else:
		print("No riman")
else:
	print("No riman")