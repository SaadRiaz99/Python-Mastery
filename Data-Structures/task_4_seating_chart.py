print("Name: Saad Bin Riaz")
print("ID: BAI-25F-035")

seating_chart = [
    ["Saad", "Ali", "Empty"],
    ["Ayesha", "Empty", "Ahmed"],
    ["Sara", "Bilal", "Empty"]
]

for row in seating_chart:
    for student in row:
        print(student, end="\t")
    print()
