""" 
✅ A partir de:
try:
    numero = input("Número: ")
    resultado = 6 / int(numero)
    print(resultado)
except ValueError:
    print("No se puede dividir entre un entero y una cadena")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except KeyboardInterrupt:
    print("\nAcabas de salir del programa")
except Exception as mensaje:
    print("Ha ocurrido un error:", type(mensaje)) 
✅ Si el usuario presionar "intro" sin ingresar nada, entonces mostrar el
mismo mensaje que el del except KeyboardInterrupt
"""

try:
    numero = input("Número: ")
    if not numero:     # if numero == "":
        raise KeyboardInterrupt
    resultado = 6 / int(numero)
    print(resultado)
except ValueError:
    print("No se puede dividir entre un entero y una cadena")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except KeyboardInterrupt:
    print("\nAcabas de salir del programa")
except Exception as mensaje:
    print("Ha ocurrido un error:", type(mensaje))