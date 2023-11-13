# for numero in range(5):
#     print(numero)
#     print(numero, numero * 'hola mundo ')


buscar = 10

for numero in range(5):
    print(numero)
    if buscar == numero:
        print("encontrado ", buscar)
        break
else:
    print("no encontre el numero :(")


for char in "Ultimate Python":
    print(char)
