
#*************

# A partir de dos variables llamadas nombre y edad debes crear una
# variable que almacene si se cumplen todas las siguientes condiciones,
# y mostrar al usuario True o False:
# nombre sea diferente de cuatro asteriscos ****
# edad sea mayor que 5 y a su vez menor que 20
# Que la longitud de nombre sea mayor o igual a 4  pero a la vez menor que 8
# edad multiplicada por 3 sea mayor que 35
# 🆗 Debes ingresar los datos con input():
# 🚫 No debes usar funciones, condicionales, bucles o cualquier
# otra instrucción que no hayamos visto

#Datos
nombre = input("Ingrese su nombre: ")
edad = int(input("ingrese su edad: "))

#Variables
requisito1 = nombre != "****"
requisito2 = edad > 5 and edad < 20
requisito3 = (len(nombre)) >= 4 and (len(nombre)) <= 8
requisito4 = edad * 3 > 35

#Salida
cumple = va1 and va2 and va3 and va4 
print(cumple)

