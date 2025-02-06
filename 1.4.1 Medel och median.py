import statistics

def main():
    numbers = []
    
    for i in range(5):
        while True:
            try:
                num = float(input(f"Mata in tal {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Ogiltig inmatning, försök igen med ett nummer.")
    
    mean_value = sum(numbers) / len(numbers)
    median_value = statistics.median(numbers)
    
    print(f"Medelvärde: {mean_value}")
    print(f"Median: {median_value}")

if __name__ == "__main__":
    main()