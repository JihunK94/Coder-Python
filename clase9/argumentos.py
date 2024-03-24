def division(numero1, numero2):
    """Argumentos por posicion"""
    return numero1 / numero2
resultado = division(8, 2)
print(resultado)

def division2(numero1, numero2):
    """Argumentos por nombre"""
    return numero1 / numero2
resultado = division2(numero2=2, numero1=8)
print(resultado)