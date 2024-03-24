try:
    numero = int(input("Número: "))
    6 / numero
except Exception as mensaje:
    print("Ha ocurrido un error:", type(mensaje))