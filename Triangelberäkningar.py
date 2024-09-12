import math

def calculate_hypotenuse(a, b):
    """Beräknar hypotenusan för en rätvinklig triangel."""
    return math.sqrt(a**2 + b**2)

def main():
    a, b = 3, 4
    hypotenuse = calculate_hypotenuse(a, b)
    print(f"För kateterna {a} cm och {b} cm är hypotenusans längd {hypotenuse:.2f} cm")
    a, b = 2, 5
    hypotenuse = calculate_hypotenuse(a, b)
    print(f"För kateterna {a} cm och {b} cm är hypotenusans längd {hypotenuse:.2f} cm")

    a, b = 14, 11
    hypotenuse = calculate_hypotenuse(a, b)
    print(f"För kateterna {a} cm och {b} cm är hypotenusans längd {hypotenuse:.2f} cm")

    try:
        a = float(input("Ange längden på den första kateten (i cm): "))
        b = float(input("Ange längden på den andra kateten (i cm): "))

        if a <= 0 or b <= 0:
            print("Kateterna måste vara positiva tal.")
        else:
            hypotenuse = calculate_hypotenuse(a, b)
            print(f"Hypotenusans längd är {hypotenuse:.2f} cm")
    except ValueError:
        print("Vänligen ange ett giltigt nummer.")

if __name__ == "__main__":
    main()
