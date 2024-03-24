def dividir(numero1, numero2=2):
    return numero1 / numero2

print(dividir(300, 3))
print(dividir(300))
print(dividir(300, 3))
print(dividir(50))


def dar_energia(x=True, y=True):
    return x and y
print()
print(dar_energia())
print(dar_energia(x=True, y=True))
print(dar_energia(x=True, y=False))
print(dar_energia(y=False))