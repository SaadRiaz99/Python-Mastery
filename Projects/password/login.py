import string

print("Saad Bin Riaz")
print("BAI-25F-035")
username = "admin"
password = "admin123"
input_username = str(input("Enter your username: "))
passwi : str = str(input("Enter your password:"))

if input_username == username and passwi == password:
    print("Login Successful")
else:
    print("Access Denied")

score = 0

if passwi.capitalize() == passwi:
    score += 1
if passwi.islower() == passwi:
    score += 1
if any(character.isdigit() for character in passwi):
    score += 1
if any(character in string.punctuation for character in passwi):
    score += 1
else:
    score = 0

if score == 4:
    strength = "Strong"
elif score >= 2:
    strength = "Medium"
else:
    strength = "Weak"

