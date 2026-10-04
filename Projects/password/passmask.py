print("Saad Bin Riaz")
print("BAI-25F-035")
from getpass import getpass

password = getpass("Enter password: ")

masked_password = "*" * len(password)

print("Masked password:", masked_password)