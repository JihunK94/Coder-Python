try:     #lugar donde potencialmente puede llegar a tener un error
    x = float(input("Número 1: "))
    y = float(input("Número 2: "))
    division = round(x / y, 2)

except:  #si es error, para que no frene
    print("Algo salió mal...")

else:   #ya se que aca no va ha haber un error (opcional)
    print(division)

print("fin.")