def saludar_ciudad(nombre: str) -> str: 
    mensaje = f"¡BIENVENIDO A {nombre.upper()}!"
    return mensaje


entrada = input("Ciudad de origen: ")
saludo = saludar_ciudad(entrada)
print(saludo)