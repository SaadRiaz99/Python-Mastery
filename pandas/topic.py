import pandas as pd


import pandas as pd

data = {
    "Student_ID": list(range(101, 131)),
    "Name": [
        "Ali", "Sara", "Hamza", "Ayesha", "Zain",
        "Fatima", "Ahmed", "Hina", "Bilal", "Maryam",
        "Usman", "Iqra", "Saad", "Sana", "Hassan",
        "Noor", "Talha", "Zoya", "Danish", "Maham",
        "Umar", "Alina", "Fahad", "Hira", "Huzaifa",
        "Laiba", "Asad", "Areeba", "Salman", "Eman"
    ],
    "Class": [
        9, 10, 9, 10, 8, 8, 9, 10, 8, 9,
        10, 8, 9, 10, 8, 9, 10, 8, 9, 10,
        8, 9, 10, 8, 9, 10, 8, 9, 10, 8
    ],
    "Marks": [
        75, 92, 58, 88, 45, 95, 67, 81, 39, 90,
        72, 64, 85, 77, 52, 98, 61, 83, 48, 91,
        70, 86, 55, 79, 93, 66, 42, 89, 74, 60
    ],
    "City": [
        "Karachi", "Lahore", "Karachi", "Islamabad", "Multan",
        "Lahore", "Karachi", "Islamabad", "Multan", "Karachi",
        "Lahore", "Multan", "Karachi", "Islamabad", "Lahore",
        "Karachi", "Multan", "Islamabad", "Lahore", "Karachi",
        "Multan", "Islamabad", "Karachi", "Lahore", "Multan",
        "Islamabad", "Karachi", "Lahore", "Multan", "Islamabad"
    ],
    "Attendance": [
        90, 98, 72, 95, 65, 99, 85, 92, 58, 96,
        88, 80, 94, 87, 70, 100, 76, 91, 62, 97,
        84, 93, 68, 89, 98, 82, 60, 95, 86, 78
    ],
    "Monthly_Fee": [
        3500, 4000, 3500, 4000, 3000, 3000, 3500, 4000, 3000, 3500,
        4000, 3000, 3500, 4000, 3000, 3500, 4000, 3000, 3500, 4000,
        3000, 3500, 4000, 3000, 3500, 4000, 3000, 3500, 4000, 3000
    ],
    "Fee_Status": [
        "Paid", "Paid", "Pending", "Paid", "Pending",
        "Paid", "Paid", "Pending", "Pending", "Paid",
        "Paid", "Pending", "Paid", "Paid", "Pending",
        "Paid", "Pending", "Paid", "Pending", "Paid",
        "Paid", "Paid", "Pending", "Paid", "Paid",
        "Pending", "Pending", "Paid", "Paid", "Pending"
    ]
}

df = pd.DataFrame(data)

print(df.to_string(index=False))
print("\nRows and columns:", df.shape)
sv = pd.DataFrame(data)
print(sv)

#see column
# 
se = sv.columns
clm = sv.shape
print(f"The Shape is {se}") 
print(f"The Column is {clm}") 