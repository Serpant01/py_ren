
text = "  hej och välkommen till Python-programmering!  "
#1
centered = text.center(50)
print(f".center():\n'{centered}'\n")
#2
count_e = text.count('e')
print(f".count('e'):\nAntal 'e': {count_e}\n")
#3
right_justified = text.rjust(60)
print(f".rjust():\n'{right_justified}'\n")
#4
left_justified = text.ljust(60)
print(f".ljust():\n'{left_justified}'\n")
#5
upper_case = text.upper()
print(f".upper():\n'{upper_case}'\n")
#6
lower_case = text.lower()
print(f".lower():\n'{lower_case}'\n")
#7
capitalized = text.capitalize()
print(f".capitalize():\n'{capitalized}'\n")
#8
titled = text.title()
print(f".title():\n'{titled}'\n")
#9
stripped = text.strip()
print(f".strip():\n'{stripped}'\n")
#10
replaced = text.replace("Python", "JavaScript")
print(f".replace():\n'{replaced}'\n")
