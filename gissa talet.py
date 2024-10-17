import random
hemligt_tal = random.randint(1, 100)
max_gissningar = 7
gissningar = 0
print("Jag har valt ett tal mellan 1 och 100. Du har 7 försök att gissa rätt.")
while gissningar < max_gissningar:
    gissning = int(input("Gissa talet: "))
    gissningar += 1

    if gissning < hemligt_tal:
        print("För lågt.")
    elif gissning > hemligt_tal:
        print("För högt.")
    else:
        print("Bra jobbat! Du gissade rätt!")
        break
if gissning != hemligt_tal:
    print(f"Tyvärr, du har gissat fel 7 gånger. Det rätta talet var {hemligt_tal}.")
    