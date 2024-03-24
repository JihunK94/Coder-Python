""" I """

bandera = True  # Esto una bandera

while bandera:  # Aquí funciona la bandera
    entrada = input("Escribe salir para salir > ")
    if entrada == 'salir':
        print("ok, salgo")
        bandera = False  # Cambio de bandera


""" II """

while True: 
    entrada = input("Escribe salir para salir > ")
    if entrada == 'salir':
        print("ok, salgo")
        break