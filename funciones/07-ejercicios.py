def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char+texto_al_reves
    return texto_al_reves


def es_palindromo2(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()

#################################################


def largo(texto2):
    resultado = 0
    for _ in texto2:
        resultado += 1
    return resultado


def borrar_espacios(texto_espacio):
    texto_limpio = ""
    for numero in range(0, largo(texto_espacio)):
        if texto_espacio[numero] != " ":
            texto_limpio = texto_limpio+texto_espacio[numero]
    return texto_limpio


def es_palindromo(texto):
    # texto = texto.replace(" ", "")
    texto = borrar_espacios(texto)
    texto3 = ""

    for numero in range(largo(texto), 0, -1):
        texto3 = texto3+texto[numero-1]
        # print(numero)

    if texto.lower() == texto3.lower():
        return "es palindromo"
    else:
        return "no es palindromo"


print("hola")

print("abba", es_palindromo("abba"))
print("reconocer", es_palindromo("reconocer"))
print("amor", es_palindromo("amor"))
print("amo la paloma", es_palindromo("amo la paloma"))
print("Hola Mundo", es_palindromo("Hola Mundo"))


print("hola2")

print("abba", es_palindromo2("abba"))
print("reconocer", es_palindromo2("reconocer"))
print("amor", es_palindromo2("amor"))
print("amo la paloma", es_palindromo2("amo la paloma"))
print("Hola Mundo", es_palindromo2("Hola Mundo"))
