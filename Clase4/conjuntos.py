a = {1, 2, 3, 4}
b = {2, 3, 4, 5}

intersección = a.intersection(b) #valores en común. tambien se puede a & b
print(intersección)

union = a.union(b) #une todo. nuevo conjunto. tambien se puede a l b
print(union)

diferencia_simetrica = a.symmetric_difference(b) #busca la diferencia 
print(diferencia_simetrica)


