import os
import base64

title = """
   ___         ___                    _             
  / _ \_   _  / __\   _ ___  ___ __ _| |_ ___  _ __ 
 / /_)/ | | |/ _\| | | / __|/ __/ _` | __/ _ \| '__|
/ ___/| |_| / /  | |_| \__ \ (_| (_| | || (_) | |   
\/     \__, \/    \__,_|___/\___\__,_|\__\___/|_|   
       |___/                                        
"""

print(title)

def caesar_cipher(s, shift):
    result = ""
    for char in s:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            result += char
    return result

def obfuscate_string(method):
    c = input("Enter the string you want to obfuscate: ")
    obfuscated_string = ""

    if method == "Base64 Encoding":
        obfuscated_string = base64.b64encode(c.encode()).decode()
    
    elif method == "Hex Encoding":
        hex_encoded = "".join("{:02x}".format(ord(char)) for char in c)
        obfuscated_string = hex_encoded

    elif method == "Formatting as \\x Notation":
        sc = "".join("\\x{:02x}".format(ord(char)) for char in c)
        obfuscated_string = sc
    
    elif method == "Caesar Cipher":
        shift = int(input("Enter the shift value: "))
        caesar_encoded = caesar_cipher(c, shift)
        obfuscated_string = caesar_encoded
    
    elif method == "Reversed Caesar Cipher":
        shift = int(input("Enter the shift value: "))
        caesar_encoded = caesar_cipher(c, shift)
        reversed_encoded = caesar_encoded[::-1]
        obfuscated_string = reversed_encoded
    
    else:
        print("Invalid choice!")
    
    return obfuscated_string

## obfuscation method selection menu
print("\nSelect an obfuscation method:")
print("1. Base64 Encoding")
print("2. Hex Encoding")
print("3. Formatting as \\x Notation")
print("4. Caesar Cipher")
print("5. Reversed Caesar Cipher")
print()

choice = None
while choice not in ["1", "2", "3", "4", "5"]:
    choice = input("Enter your choice: ")
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice! Please enter a number between 1 and 5.")

## map user's choice to obfuscation method 
obfuscation_methods = {
    "1": "Base64 Encoding",
    "2": "Hex Encoding",
    "3": "Formatting as \\x Notation",
    "4": "Caesar Cipher",
    "5": "Reversed Caesar Cipher"
}

selected_method = obfuscation_methods.get(choice)

if selected_method:
    x = obfuscate_string(selected_method)
    print("\nObfuscated String:")
    print(x)
else:
    print("Invalid choice!")

input("\nPress Enter to exit...")
