import math

def radianer_till_grader(radianer):
    grader = radianer * (180 / math.pi)
    return grader
def main():
    radianer_exempel = [math.pi, 2 * math.pi, math.pi / 2]
    for rad in radianer_exempel:
        grader = radianer_till_grader(rad)
        print(f"{rad} radianer är {grader} grader")

    radianer_input = float(input("Ange antalet radianer: "))
    decimaler = int(input("Ange antal decimaler att avrunda till: "))

    grader_input = radianer_till_grader(radianer_input)
    grader_avrundade = round(grader_input, decimaler)
    print(f"{radianer_input} radianer är {grader_avrundade} grader (avrundat till {decimaler} decimaler)")

if __name__ == "__main__":main()  