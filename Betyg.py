
poang = int(input("Ange elevens poäng (0-50): "))
if poang < 0 or poang > 50:
    print("Ogiltig poäng, var god ange ett tal mellan 0 och 50.")
elif poang < 25:
    print("Betyg: F")
elif poang < 30:
    print("Betyg: E")
elif poang < 35:
    print("Betyg: D")
elif poang < 40:
    print("Betyg: C")
elif poang < 45:
    print("Betyg: B")
else:
    print("Betyg: A")
