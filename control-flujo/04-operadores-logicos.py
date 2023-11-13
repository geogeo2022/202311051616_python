# and or not

gas = True
encendido = True

if gas and encendido:
    print("Puedes Avanzar")

gas = False
encendido = True

if gas and encendido:
    print("Puedes Avanzar")

gas = False
encendido = True

if gas or encendido:
    print("Puedes Avanzar")

gas = False
encendido = False

if gas or encendido:
    print("Puedes Avanzar")

gas = False
encendido = False
edad = 18


if gas and encendido and edad > 17:
    print("Puedes Avanzar")

gas = True
encendido = True
edad = 18


if gas and (encendido or edad > 17):
    print("Puedes Avanzar")


# operadores de cortocircuito

gas = False
encendido = True
edad = 18


if not gas and encendido and edad > 17:
    print("Puedes Avanzar")

# se ejecuta de izquier a derecha
# and que la primera sea false no se ejecuta lo demas
# or que la primera sea true si se ejucuta lo demas
