"""
Tomando la solución del ejercicio pasado, en lugar de devolver None al dividir entre cero,
tienes que capturar una excepción que muestre por pantalla el mensaje:
"No se puede dividir por cero" Además, capturar otros posibles errores.
def dividir(a, b):
    if b == 0:
        return None
    else:
        return a / b
resultado = dividir(10, 0)
print(resultado)
"""

def ingresar_numeros() -> tuple[float, float]:
    while True:
        try:
            numero_1 = float(input("Número 1: "))
            numero_2 = float(input("Número 2: "))
        except ValueError:
            print("Debes ingresar un número, no otros caracteres")
            continue
        except KeyboardInterrupt:
            print("Sales del programa\n")
            exit()
        except Exception as error:
            print(type(error))
        return numero_1, numero_2
def main():
    numero_1, numero_2 = ingresar_numeros()
    division = dividir(numero_1, numero_2)
    if division is False:
        print("No se pudo realizar la división.")
    else:
        print(f"El resultado de la división es {division}")

main()