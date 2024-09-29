import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key  : {key}")

# ENCRYPTION

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

# iterate over every letter in plan_text
# Strings are iterable

for letter in plain_text:
    index = chars.index(letter)
    # refer to key
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")



# DE-ENCRYPTION

cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

# iterate over every letter in plan_text
# Strings are iterable

for letter in cipher_text:
    index = key.index(letter)
    # refer to key
    plain_text += chars[index]

print(f"Original message: {cipher_text}")
print(f"Encrypted message: {plain_text}")