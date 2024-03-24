texto = input("Ingresa una oración: ")

lista = texto.split()
print(lista)
palabras_unicas = set(lista)
print(palabras_unicas)

nueva_lista_palabras_unicas = list(palabras_unicas)
print(nueva_lista_palabras_unicas)

nueva_lista_palabras_unicas.sort()
print(nueva_lista_palabras_unicas)

otra_lista = [1, 2, 3, 4]
nueva_lista_palabras_unicas.extend(otra_lista)
print(nueva_lista_palabras_unicas)

nueva_lista_palabras_unicas.insert(0, "hola")
print(nueva_lista_palabras_unicas)

print("******************")
g = nueva_lista_palabras_unicas.copy()
g.append(5000)
print(g)
