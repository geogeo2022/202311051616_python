usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

print(usuarios)

nombres = []

for usuario in usuarios:
    nombres.append(usuario[0])
    print(usuario[0])

print(nombres)

# map
nombres2 = [usuario[0] for usuario in usuarios]
print(nombres2)

nombres3 = [usuario[1] for usuario in usuarios]
print(nombres3)

# filter
nombres4 = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres4)

# map - filter
nombres5 = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres5)

# list map
nombres6 = list(map(lambda usuario: usuario[0], usuarios))
print(nombres6)

# list map - filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
