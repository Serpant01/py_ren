def main():
    while True:
        print("\nMeny:")
        print("1. Ange en sträng")
        print("2. Avsluta")
        
        val = input("Välj ett alternativ (1 eller 2): ")

        if val == "1":
            user_string = input("Ange en sträng: ")
            reversed_string = user_string[::-1]
            sorted_string = ''.join(sorted(user_string))

            print(f"Baklänges: {reversed_string}")
            print(f"Sorterad: {sorted_string}")

        elif val == "2":
            print("Avslutar programmet. Tack för att du använde det!")
            break

        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main()