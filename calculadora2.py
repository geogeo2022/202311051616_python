import sys

print("Bienvenidos a la calculadora 2.0")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi, div")

bandera = True

valor = 0

n1 = input("Ingresa numero 1: ")

print(n1)

if n1.lower() == "salir":
    sys.exit()


while True:
    while True:
        n2 = input("Ingresa la operacion(suma, resta, multi, div)(salir): ")
        if n2.lower() == "suma" or n2.lower() == "resta" or n2.lower() == "multi" or n2.lower() == "div" or n2.lower() == "salir":
            break

    if n2.lower() == "salir":
        break
        #sys.exit()

    n3 = input("Ingresa numero 2: ")

    if n3.lower() == "salir":
        break
        #sys.exit()

    if n2.lower() == "suma":
        if bandera:
            resul = int(n1)+int(n3)
            bandera = False
        else:
            resul = resul + int(n3)
        print("La suma es", resul)

    elif n2.lower() == "resta":
        if bandera:
            resul = int(n1)-int(n3)
            bandera = False
        else:
            resul = resul - int(n3)
        print("La resta es", resul)

    elif n2.lower() == "multi":
        if bandera:
            resul = int(n1)*int(n3)
            bandera = False
        else:
            resul = resul * int(n3)
        print("La multiplicacion es", resul)
    else:
        if bandera:
            resul = int(n1)/int(n3)
            bandera = False
        else:
            resul = resul / int(n3)
        print("La division es", resul)

