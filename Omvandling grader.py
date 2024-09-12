import math

def grader_till_radianer(grader):
    return grader * (math.pi / 180)

grader_a = 160
radianer_a = grader_till_radianer(grader_a)
print(f"{grader_a}° är {radianer_a:.4f} radianer")

grader_b = 360
radianer_b = grader_till_radianer(grader_b)
print(f"{grader_b}° är {radianer_b:.4f} radianer")

grader_c = 90
radianer_c = grader_till_radianer(grader_c)
print(f"{grader_c}° är {radianer_c:.4f} radianer")

grader = float(input("Ange gradantalet: "))
radianer = grader_till_radianer(grader)
print(f"{grader}° är {radianer:.4f} radianer")

antal_decimaler = int(input("Hur många decimaler vill du avrunda till? "))
radianer_formaterad = f"{radianer:.{antal_decimaler}f}"
print(f"{grader}° är {radianer_formaterad} radianer.")