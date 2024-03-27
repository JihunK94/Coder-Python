#Ingreso de datos

def logon():

  email = input("Ingrese un email:")
  for formulario in usuarios_lista:
     if email in formulario["email"]:
        print("El email ingresado ya corresponde a un usuario. Ingrese otro email")
        return
     else: 
        print("El email se ha registrado correctamente⭐")

  while True: 
    password = input("Ingrese una contraseña:")
    verificar_password = input("Verifique su contraseña:")
    if password == verificar_password:
       print("Contraseña creada con éxito✅")
       break
    else:
       print("❌Error, la contraseña debe ser la misma❌")
  formulario ={"email": email, "password": password}
  usuarios_lista.append(formulario)

def login():
    ingresar_email = input("Email:")
    hay_email_password = False
    intento = 5
    while intento >0 and not hay_email_password:
       intento -= 1
       password = input("Contraseña:")
       for formulario in usuarios_lista:
          if ingresar_email in formulario["email"] and password in formulario["password"]:
             hay_email_password = True
             print("Email y contreseña correcta. Iniciando sesión✅")
          else:
             print("El email o la contraseña es inválida. Intente nuevamente")
      

usuarios_lista :list[dict] = []

print("Bienvenido! inicie sesión para poder disfrutar de nuestro contenido")

while True:
  print()
  print("1. Crear usuario y contraseña")
  print("2. Loggin")
  print("3. Salir del programa")
  opción = input("Seleccione alguna de las tres opciones")

  if opción == "1":
    logon()
  elif opción == "2":
    login()
  elif opción == "3":
    print("Adiós, nos vemos pronto😉")
    break
  else:
    print()
    print("Opción invalida, vuelva a intentar😕")



     
