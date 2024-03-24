print("PASS")
x = 0
while x < 5:
    x += 1
    if x == 3:
        pass
    print(x)

print("CONTINUE")
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)

print("BREAK")
x = 0
while x < 5:
    x += 1
    if x == 3:
        break
    print(x)