print("Name: Saad Bin Riaz")
print("ID: BAI-25F-035")

subjects = ["Data Structures", "Programming Fundamentals", "Discrete Mathematics", "Linear Algebra", "English"]

subject_name = input("Enter a subject name: ").strip()
found = False

for index in range(len(subjects)):
    if subjects[index].lower() == subject_name.lower():
        print(f"{subjects[index]} exists at index {index}.")
        found = True
        break

if not found:
    print("Subject not found.")
