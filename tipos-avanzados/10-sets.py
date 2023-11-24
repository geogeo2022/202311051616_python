# set = grupo o conjunto
primer = {1, 1, 2, 2, 3, 4, 5}
print(primer)

# primer.add(5)
# print(primer)

# primer.remove(1)
# print(primer)

segundo = [3, 4, 5]
print(segundo)
segundo = set(segundo)
print(segundo)

print(primer | segundo)

print(primer)
print(segundo)

print(primer & segundo, "diferencia")

print(primer - segundo)

# diferencia simetrica
print(primer ^ segundo)

if 5 in segundo:
    print("hola mundo")
