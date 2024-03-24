generación_silenciosa = range(1920, 1941)
baby_boomer = range(1946, 1965)
generacion_x = range(1965, 1980)
generacion_y = range(1980, 2001)
generacion_z = range(2001, 2011)

año_de_nacimiento = int(input("Año de nacimiento: "))

if año_de_nacimiento in generación_silenciosa:
    mensaje = "Generación Silenciosa"
elif año_de_nacimiento in baby_boomer:
    mensaje = "Baby Boomer"
elif año_de_nacimiento in generacion_x:
    mensaje = "Generación X"
elif año_de_nacimiento in generacion_y:
    mensaje = "Generación Y"
elif año_de_nacimiento in generacion_z:
    mensaje = "Generación Z"
else:
    mensaje = "No existe generación asociada"

print(f"El año {año_de_nacimiento} corresponde a la generación '{mensaje}'")


#Para aprobar un crédito, 
 #   - el cliente debe ser mayor de edad. 
  #  - Además, debe tener una antigüedad en el sistema financiero mínima de 3 años, 
   # - y un ingreso mensual mayor a 2500 dólares. 

    #En caso de que no tenga la antigüedad suficiente, 
     #   - su ingreso mensual debe ser como mínimo 4000 dólares. 

#Si no cumple ninguna de las condiciones, no se aprueba el crédito. 
#"""

# Ingreso de datos
edad = int(input("Edad: "))
antigüedad = int(input("Antigüedad en el sistema financiero: "))
ingresos = float(input("Ingresos mensuales: "))

# Condiciones para el crédito
mayor_edad = (edad >= 18)
condición_1 = (mayor_edad and antigüedad >= 3 and ingresos > 2500)
condición_2 = (mayor_edad and antigüedad < 3 and ingresos >= 4000)

# Salida de datos
if condición_1 or condición_2:
    print("Crédito aprobado")
else:
    print("Crédito no aprobado")