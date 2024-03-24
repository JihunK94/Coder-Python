def ingresar_numeros():
    lista_de_precios = []
    while True:
        entrada = input("Ingrese un número o 'salir' para salir: ")
        if entrada == 'salir':
            break
        elif entrada.isdigit():
            numero = int(entrada)
            lista_de_precios += [numero]
            # lista_de_precios.append(numero)
        else:
            continue
    return lista_de_precios

def total_compra(*args):
    resultado = sum(args)
    return resultado

def main():
    compra_anterios = [1, 10, 100, 1000]
    lista_de_precios = ingresar_numeros()
    resultado = total_compra(*lista_de_precios, *compra_anterios) #acá es asterisco está para desempacar los valores y que no queden dos listas
    print(f"El total de tu compra fue ${resultado}")
main()
