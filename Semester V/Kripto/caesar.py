import string

letters = string.ascii_lowercase + ' '

inverseLetters = {}
numLetters = len(letters)

for i in range(numLetters):
    inverseLetters[letters[i]] = i

def encrypt(plain, shift):
    global letters, inverseLetters, numLetters
    cipher = ''
    for i in plain:
        index = (inverseLetters[i] - shift) % numLetters
        cipher += letters[index]
    return cipher

def decrypt(cipher, shift):
    global letters, inverseLetters, numLetters
    plain = ''
    for i in cipher:
        index = (inverseLetters[i] - shift) % numLetters
        plain += letters[index]
    return plain

cipher = input("Enter cipher text: ")
shift = int(input("Shift: "))

cipher = encrypt(cipher, shift)
print("Cipher:", cipher)
