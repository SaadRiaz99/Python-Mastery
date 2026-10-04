print("Saad Bin Riaz")
print("BAI-25F-035")
import string


def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(character.isupper() for character in password):
        score += 1

    if any(character.islower() for character in password):
        score += 1

    if any(character.isdigit() for character in password):
        score += 1

    if any(character in string.punctuation for character in password):
        score += 1

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return score, strength


# Test with predefined passwords
passwords = ["abc", "12345678", "abcdefgh", "Abcdefg1", "Abcdef1!"]
password = input("Enter your password: ")

score, strength = check_password(password)

print(f"Score: {score}/5")
print(f"Strength: {strength}")
for password in passwords:
    score, strength = check_password(password)
    print(f"{password} | Score: {score}/5 | Strength: {strength}")