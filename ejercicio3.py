"""while True:
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
        print("✨ Fin de la app de división")"""
"""crear una funcion con buenas practicas"""

def ingresar_numeros_para_dividirlos():
    while True:
        try:
            dividendo = float(input("Dividendo: "))
            divisor = float(input("Divisor: "))
            if divisor == 0:
                raise
        except:
            print("Hubo un error. Intenta de vuelta.")
            continue
        else:
            break
    return dividendo, divisor
def dividir(dividendo: float, divisor: float) -> float | bool:
    try:
        division = dividendo / divisor
    except:
        print("No se puede dividir por cero")
        return False
    return division
def mostrar(numero: float) -> None:
    print(f"El resultado de la división es {numero:.5f}")
def main():
    dividendo, divisor = ingresar_numeros_para_dividirlos()
    resultado = dividir(dividendo, divisor)
    if resultado is False:
        pass
    else:
        mostrar(resultado)

main()




