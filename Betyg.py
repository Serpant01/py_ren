
poäng = int(input("Ange elevens poäng (0-50): "))
if poäng < 0 or poäng > 50:
    print("Ogiltig poäng, var god ange ett tal mellan 0 och 50.")
elif poäng < 25:
    print("Betyg: F")
elif poäng < 30:
    print("Betyg: E")
elif poäng < 35:
    print("Betyg: D")
elif poäng < 40:
    print("Betyg: C")
elif poäng < 45:
    print("Betyg: B")
else:
    print("Betyg: A")
