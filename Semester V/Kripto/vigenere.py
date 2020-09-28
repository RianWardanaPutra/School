import string

letters = string.ascii_lowercase + ' '
invLetters = {}
numLetters = len(letters)

for i in range(numLetters):
    invLetters[letters[i]] = i

def encrypt(plain, password):
    global letters, invLetters, numLetters
    cipher = ''
    passwordIndex = 0
    for i in plain:
        shift = invLetters[password[passwordIndex]]
        index = (invLetters[i] + shift) % numLetters
        cipher += letters[index]
        passwordIndex = (passwordIndex + 1) % len(password)
    return cipher

def decrypt(cipher, password):
    global letters, invLetters, numLetters
    plain = ''
    passwordIndex = 0
    for i in cipher:
        shift = invLetters[password[passwordIndex]]
        index = (invLetters[i] - shift) % numLetters
        plain += letters[index]
        passwordIndex = (passwordIndex + 1) % len(password)
    return plain

plain = input("Plain text: ")
password = input("Input password: ")

print(encrypt(plain, password))
print('decrypt:', decrypt(encrypt(plain, password), password))
