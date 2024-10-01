
årskort_pris = float(input("Ange priset för ett årskort: "))
biljett_pris = float(input("Ange priset för en biljett: "))
antal_besok = int(input("Ange antalet besök du planerar att göra under året: "))
total_biljettkostnad = biljett_pris * antal_besok
if årskort_pris < total_biljettkostnad:
    print("Det lönar sig att köpa årskort.")
else:
    print("Det lönar sig inte att köpa årskort.")