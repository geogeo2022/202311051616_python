lista1 = [1, 2, 3, 4]
print(1, 2, 3, 4)
print(lista1)
print(*lista1)

lista3 = (1, 2, 3, 4)
print(1, 2, 3, 4)
print(*lista3)

lista2 = [5, 6]

combinada = [*lista1, *lista2]
print(combinada)

combinada = ["Hola", *lista1, "mundo", *lista2, "Chanchito"]
print(combinada)

punto10 = {"x": 19, "y": "Hola"}
punto11 = {"y": 15}

nuevoPunto = {**punto10, "lala": "hola mundo", **punto11, "z": "mundo"}

print(nuevoPunto)
