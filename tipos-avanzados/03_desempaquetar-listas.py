numeros = [1, 2, 3]

# feo
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

print(numeros)
# print(primero, segundo, tercero)

# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

# primero, *otros = numeros
# print(primero, otros)

numeros2 = list(range(1, 10))
print(numeros2)

# primero, segundo, *otros = numeros2
# print(primero, segundo, otros)

# primero, *otros, ultimo = numeros2
# print(primero, otros, ultimo)

primero, segundo, *otros, penu, ultimo = numeros2
print(primero, segundo, otros, penu, ultimo)
