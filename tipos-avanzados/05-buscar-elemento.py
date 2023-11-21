mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]
mascotas2 = ["Pelusa", "Pulga", "Felipe", "Wolfgang", "Chanchito feliz"]
mascotas3 = ["Pelusa", "Wolfgang", "Felipe", "Wolfgang", "Chanchito feliz"]

print(mascotas.index("Pulga"))

if "Wolfgang" in mascotas:
    print(mascotas.index("Wolfgang"))
else:
    print("no existe 1")

if "Wolfgang" in mascotas2:
    print(mascotas2.index("Wolfgang"))
else:
    print("no existe 2")

print(mascotas3.count("Wolfgang"))
if "Wolfgang" in mascotas3:
    print(mascotas3.index("Wolfgang"))
else:
    print("no existe 2")
