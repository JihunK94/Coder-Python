# A partir del siguiente código
#
# def login():
#     print(user)
#     print(password)
#     if permisos:
#         print("Sí tiene permisos de administrador")
#     else:
#         print("Acceso denegado")
#
# Crear los parámetros que faltan
# 'permisos' debe ser por defecto False
# invocar la función con argumentos por nombre

def login(user: str, password: str, permisos=False):
    """Función login que sirve para ver si un usuario
    tiene permisos de administrador"""
    print(user)
    print(password)
    if permisos:
        print("Sí tiene permisos de administrador")
    else:
        print("Acceso denegado")


def ingresar_datos_login():
    user = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    permisos = input("Tiene permisos de administrador? s/n: ")
    if permisos.lower().strip() in ("s", "sí", "si"):
        permisos = True
    else:
        permisos = False
    return user, password, permisos


def main():
    user, password, permisos = ingresar_datos_login()
    login(user=user, password=password, permisos=permisos)
    # login(user="Bruno", password="admin123", permisos=True)
    # login(user="Lean", password="user123", permisos=False)
    # login(user="Lean", password="user123")


main()
