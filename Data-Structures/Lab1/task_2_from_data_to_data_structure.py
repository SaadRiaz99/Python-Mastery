print("Name: Saad Bin Riaz")
print("ID: BAI-25F-035")
print("Task 2 - From Data to a Data Structure")
print("Sample daily-life data:")

daily_life_data = {
    "Name": "Saad Bin Riaz",
    "Phone battery percentage": 75,
    "Study hours": 1.5,
    "Wi-Fi connected": True,
    "Daily steps": 4500
}

for item, value in daily_life_data.items():
    print(f"{item}: {value}")

print("I chose a dictionary because it groups different types of data using clear names for each value.")
