magicNumber = 26

for n in range(101):
    if n is magicNumber:
        print(n, " is the magic number!")
        break
    else:
        print(n)

for x in range(100):
    if x%4 is 0:
        print(x)