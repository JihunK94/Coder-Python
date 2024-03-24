""" Ejercicio
Escribe un programa en Python que solicite al usuario dos entradas de tipo entero,
las cuales indican si el usuario aprobó (1) o no aprobó (0) los exámenes A y B respectivamente.
El programa debe convertir estas entradas en valores booleanos y mostrarlas en pantalla.
Además, debes explicar por escrito cómo funciona la función bool() en Python
y por qué se utiliza en este código."""

examen_1 = int(input("Examen A aprobado? (1 es sí, 0 es no)"))
examen_2 = int(input("Examen B aprobado? (1 es sí, 0 es no)"))

examen_1 = bool(examen_1)
examen_2 = bool(examen_2)

print(examen_1)
print(examen_2)
