mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]
print(mascotas)

for mascota in mascotas:
    print(mascota)


for mascota in enumerate(mascotas):
    print(mascota)
    print(mascota[0])
    print(mascota[1])

for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
