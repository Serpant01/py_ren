
header1 = "Tal".rjust(5)
header2 = "Kvadrat".rjust(10)
header3 = "Kub".rjust(10)

print(header1 + header2 + header3)

for i in range(1, 11):
    tal = str(i).rjust(5)
    kvadrat = str(i**2).rjust(10)
    kub = str(i**3).rjust(10)
    print(tal + kvadrat + kub)
