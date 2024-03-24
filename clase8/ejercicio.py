# Anotaciones de tipo / Type hints

def saludar_ciudad(nombre: str): 
    print(f"¡BIENVENIDO A {nombre.upper()}!")

entrada = input("Ciudad de origen: ")
saludar_ciudad(entrada)