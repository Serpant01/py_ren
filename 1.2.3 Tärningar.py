import random

antal_tarningar = int(input("Hur många tärningar vill du kasta? "))
resultat = []
total_summa = 0
for i in range(antal_tarningar):
    kast = random.randint(1, 6)  
    resultat.append(kast) 
    total_summa += kast 
medelvarde = total_summa / antal_tarningar if antal_tarningar > 0 else 0
print("Resultaten av tärningskasten: ", resultat)
print("Total summa: ", total_summa)
print("Medelvärde: ", medelvarde)
