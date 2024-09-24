import math
def berakna_ar(startvarde, avskrivningstakt, slutvarde):
    ar = math.log(slutvarde / startvarde) / math.log(avskrivningstakt)
    return ar
startvarde = float(input("Ange startvärdet på bilen (kr): "))
avskrivningstakt_procent = float(input("Ange procentuell avskrivningstakt per år (t.ex. 85 för 85%): "))
slutvarde = float(input("Ange slutvärdet på bilen (kr, t.ex. 100000): "))
avskrivningstakt = avskrivningstakt_procent / 100
antal_ar = berakna_ar(startvarde, avskrivningstakt, slutvarde)
print(f"Det tar {antal_ar:.2f} år för bilens värde att minska till {slutvarde} kr.")