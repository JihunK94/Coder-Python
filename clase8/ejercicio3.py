"""Crear 2 funciones:
 sumar(), que va a sumar 2 números y devuelve un entero.
y la otra función ingresar_numeros(), que solicita 2 números y devuelve ambos"""

def sumar(numero_1: int, numero_2: int) -> int:
    suma = numero_1 + numero_2
    return suma


def ingresar_numeros() -> tuple[int, int]:
    numero_1 = int(input("Ingrese el número 1: "))
    numero_2 = int(input("Ingrese el número 2: "))
    return numero_1, numero_2


def mostrar_resultado(suma: int) -> None:
    print(f"El resultado de la suma es {suma}")


def main():
    numero_1, numero_2 = ingresar_numeros()
    suma = sumar(numero_1, numero_2)
    mostrar_resultado(suma)
    

main()




