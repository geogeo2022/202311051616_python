numeros = [2, 4, 1, 45, 75, 22]
numeros2 = [2, 4, 1, 45, 75, 22]
print(numeros)

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

numeros3 = sorted(numeros2)
print(numeros3)

numeros3 = sorted(numeros2, reverse=True)
print(numeros3)

usuarios = [
    [4, "Chanchito"],
    [1, "Felipe"],
    [5, "Pulga"]
]

print(usuarios)

usuarios.sort()
print(usuarios)

usuarios2 = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

print(usuarios2)

usuarios2.sort()
print(usuarios2)


usuarios3 = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

print(usuarios3)

# feo


# def ordena(elemento):
#     return elemento[1]


# usuarios3.sort(key=ordena)
# print(usuarios3)

# usuarios3.sort(key=ordena, reverse=True)
# print(usuarios3)

# def ordena(elemento):
# return elemento[1]

usuarios3.sort(key=lambda el: el[1], reverse=True)
print(usuarios3)
