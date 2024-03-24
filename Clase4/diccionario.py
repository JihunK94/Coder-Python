# *** COPY & CLEAR
diccionario = {"sal": 10.50, "pan": 20.00, "leche": 25.25, "vino": 100.00}

diccionario_copia = diccionario.copy()
diccionario_copia["fideos"] = 200.2

print(diccionario)
print(diccionario_copia)

diccionario_copia.clear()
print(diccionario_copia)

# KEYS Y VALUES
claves = diccionario.keys()
print(claves)
a, b, c, d = diccionario.keys()  # desempacando
print(a, b, c, d)
print(*claves)
print(list(diccionario.keys()))
print(list(diccionario.values())
      # ITEMS
print("*****************")
claves_valores = diccionario.items()
print(claves_valores)
a, b, c, d = diccionario.items()
print(a, b, c, d)
# print(*a, *b, *c, *d)
producto = a[0]
precio = a[1]
print(f"{producto}: ${precio}")

# ✅
print("🔥🔥🔥🔥🔥")
diccionario = {"sal": 10.50, "pan": 20.00, "leche": 25.25, "vino": 100.00}

for clave in diccionario.keys():
    print(clave)

for valor in diccionario.values():
    print(valor)

for clave, valor in diccionario.items():
    print(f"{clave}: ${valor}")

# UPDATE
otro_dict = {"carne": 500, "verdura": 300}
diccionario.update(otro_dict)
print(diccionario)