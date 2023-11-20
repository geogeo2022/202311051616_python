#no usar variables globales
saludo="Hola Global"

def saludar():
    #print(saludo)
    global saludo
    print(saludo)
    saludo="Hola Mundo"
    print(saludo)

def saludaChanchito():
    saludo = "Saludo Chanchito"
    print(saludo)

#print(saludo)
saludar()
saludaChanchito()
saludar()

print(saludo)
