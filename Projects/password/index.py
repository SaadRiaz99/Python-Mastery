print("Saad Bin Riaz")
print("ID: 25F-035")
password = str(input("Enter your password: "))
def encrypt(password:str ) -> str:
    encrypted_password = ""
    for char in password:
        encrypted_password += chr(ord(char) + 3)  
    return encrypted_password

def decrypt(password:str = password) -> str:
    decrypted_password = ""
    for char in password:
        decrypted_password += chr(ord(char) - 3)  
    return decrypted_password

encr = encrypt(password)
dexrp = decrypt(encr)
print(f"Encrypted password: {encr}")
print(f"Decrypted password: {dexrp}")