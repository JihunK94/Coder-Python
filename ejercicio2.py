"""
A partir del código:
try:
    x = float(input("Número 1: "))
    y = float(input("Número 2: "))
    division = round(x / y, 2)
except:
    print("Algo salió mal...")
else:   # es opcional, se ejecuta cuando no hay errores
    print(division)
finally:  # es opcional, siempre se ejecuta, haya o no errores
    print("Fin.")
Crear un bucle while True, y si algo salió mal, pedir otra vez los números al usuario
"""

while True:
    try:
        x = float(input("Número 1: "))
        y = float(input("Número 2: "))
        division = x / y
    except:
        print("Hubo un error. Intenta de vuelta.")
        continue
    else:   
        print(f"El resultado de la división es: {division:.2f}")
        break
    finally:
        print("✨ Fin de la app de división")

