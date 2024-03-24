lista = [1, 2, 3, 4, 5, 6]

for elemento in lista:
    if elemento == 3:
        continue
    if elemento == 5:
        break
    print(elemento)