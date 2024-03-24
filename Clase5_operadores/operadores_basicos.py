# Operadores relaciones

print(12 == 12)
print(12 != 12)
print(12 > 2)
print(12 < 2)
print(12 >= 12)
print(12 <= 1)

# Ejercicio
expresiones = [
    False == True,
    10 >= 2 * 4,
    33 / 3 == 11,
    True > False,
    True * 5 == 2.5 * 2,
]

expresiones_1 = False == True
expresiones_2 = 10 >= 2 * 4
expresiones_3 = 33 / 3 == 11
expresiones_4 = True > False
expresiones_5 = True * 5 == 2.5 * 2

tupla_de_expresiones = (expresiones_1, expresiones_2,
                        expresiones_3, expresiones_4, expresiones_5)
print(tupla_de_expresiones)

# Ejercicio

expresiones = [
    not False,
    not 3 == 5,
    33/3 == 11 and 5 > 2,
    True or False,
    True*5 == 2.5*2 or 123 >= 23,
    12 > 7 and True < False
]

dict = {'exp1': expresiones[0], 'exp2': expresiones[1], 'exp3': expresiones[2],
        'exp4': expresiones[3], 'exp5': expresiones[4], 'exp6': expresiones[5]}
print(dict)
