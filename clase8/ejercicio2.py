"""A partir del siguiente código, crear una función ingresar_ciudad() donde se use input()
Luego imprimir el mensaje en el ámbito global
def saludar_ciudad(nombre):
    print(f"¡BIENVENIDO A {nombre.upper()}!")

entrada = input("Ciudad de origen: ")
saludar_ciudad(entrada)
"""

def saludar_ciudad(nombre):
    saludo = f"¡BIENVENIDO A {nombre.upper()}!"
    return saludo

def ingresar_ciudad():
    ciudad = input("Ingrese su ciudad: ")
    return ciudad

ciudad_ingresada = ingresar_ciudad()
saludo_especifico = saludar_ciudad(ciudad_ingresada)
print(saludo_especifico)
