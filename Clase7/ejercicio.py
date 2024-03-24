"""
En un bucle while, ingresar números mediante input. 
Cada número ingresado se sumará al anterior.
Si el usuario ingresa 'salir' o 'exit', debe terminar el bucle.
Al terminar se mostrará el resultado final de la suma de números.
"""

suma = 0

while True:
    entrada = input("Ingresar un número ('exit' o 'salir' para salir): ")
    if entrada.lower().strip() in ('exit', 'salir'):
        break
    if entrada.isdigit():
        numero = int(entrada)
        suma += numero
    else:
        print(" 🔴 Debes introducir un número")

print(f"La suma final es {suma}")