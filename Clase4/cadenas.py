cadena = " esta es una prueba con Pithon  🔥🔥   "
print(cadena)

print("upper:", cadena.upper())
print("lower:", cadena.lower())
print("title:", cadena.title())

cadena = cadena.strip()
print(cadena)
print("capitalize:", cadena.capitalize())
cadena = cadena.capitalize()
print(cadena)
print("replace:", cadena.replace("pithon", "Python"))
print("find:", cadena.find("a"))
print("find:", cadena.find("A"))
print("isdigit:", "1234".isdigit())
print("isdigit:", "a1234".isdigit())
print("count", cadena.count("🔥"))
print("count", cadena.count("E") + cadena.count("e"))

print("  Esta es una Prueba".strip().upper().replace("E", "3"))
x = 232345.34
print(x.is_integer()) #pregunta si es entero (int)

cadena = " esta es una prueba con Pithon  🔥🔥   "
lista = cadena.split() #si no se indica nada, separa por espacios. se indica escribiendo algo en la () crea una lista
print(lista)

lista_de_frutas = ["limón", "palta", "sandia"]
cadena_de_frutas = " ". join(lista_de_frutas) #entre las "" se pone como se divide ej:, espacio - etc
#iterar significa ir caminando sobre una colección de datos. lleva una lista a una cadena

