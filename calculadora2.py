print("Bienvenidos a la calculadora 2.0")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi, div")

bandera = True

valor = 0

n1 = input("Ingresa numero 1: ")

while True:
    while True:
        n2 = input("Ingresa la operacion(suma, resta, multi, div)(salir): ")
        if n2.lower() == "suma" or "resta" or "multi" or "div" or "salir":
            break

    if n2.lower() == "salir":
        break
    n3 = input("Ingresa numero 2: ")

    if n3.lower() == "salir":
        break

    if n2.lower() == "suma":
        if bandera:
            resul = int(n1)+int(n3)
            bandera = False
        elif bandera:
            resul = resul + int(n3)
        print("La suma es", resul)

    elif n2.lower() == "resta":
        resul = int(n1)-int(n3)
        print("La resta es", resul)
