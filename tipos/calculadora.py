n1 = input("Ingresa primer numero: ")
n2 = input("Ingresa segundo numero: ")

n1 = int(n1)
n2 = int(n2)

# print(n1, n2)
# print(n1 + n2)

suma = n1+n2
resta = n1-n2
multi = n1*n2
div = n1/n2

mensaje = f"""
Para los Numeros {n1} y {n2},
La suma es: {suma}
La resta es: {resta}
La multiplicacion es: {multi}
La Division es: {div}
"""
print(mensaje)
