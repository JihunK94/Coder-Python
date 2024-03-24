def mi_decorador(funcion):
    def envoltorio():
        print("********* Antes de ejecutar la función")
        funcion()
        print("********* Después de ejecutar la función")
    return envoltorio
@mi_decorador
def bienvenida():
    print("hola")
@mi_decorador
def adios():
    print("adios")

bienvenida()
adios()