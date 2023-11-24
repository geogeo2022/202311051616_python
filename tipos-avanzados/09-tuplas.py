# con () no se modifican, tuplas
numeros = (1, 2, 3)
print(numeros)

numeros = (1, 2, 3)+(4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)

menosNumero = numeros[:2]
print(menosNumero)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

# no se pueden modificar las tuplas
# numeros[0] = 55

listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito Feliz"
print(listaNumeros)
