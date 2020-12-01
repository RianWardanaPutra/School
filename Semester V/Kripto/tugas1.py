import string

letters = string.ascii_letters + ' '

def vigenere(plain, key):
    cipher = ''
    for i in range(len(plain)):
        shift = letters.index(key[i % len(key)])
        new_letter = letters[(letters.index(plain[i]) + shift) % len(letters)]
        cipher += new_letter
    return cipher


def transposition(plain, columns):
    cipher = ''
    rows = len(plain) // columns
    if rows * columns < len(plain):
        rows += 1

    block = [[' ' for i in range(columns)] for j in range(rows)]
    i=0; j=0

    for char in plain:
        block[i][j] = char
        j = (j+1) % columns
        if j == 0:
            i += 1

    for col in range(columns):
        for row in range(rows):
            cipher += block[row][col]

    return cipher

def decrypt_transpose(cipher, columns):
    plain = ''
    rows = len(cipher) // columns
    if columns*rows < len(cipher):
        rows += 1

    block = [[' ' for i in range(rows)] for j in range(columns)]
    i = 0; j = 0

    for char in cipher:
        block[j][i] = char
        i = (i+1) % rows
        if i == 0:
            j += 1

    for i in range(rows):
        for j in range(columns):
            plain += block[j][i]

    return plain

def decrypt_vigenere(cipher, key):
    cipher = cipher.rstrip()
    plain = ''
    for i in range(len(cipher)):
        shift = letters.index(key[i % len(key)])
        new_letter = letters[(letters.index(cipher[i]) - shift) % len(letters)]
        plain += new_letter
    return plain

print("""
      Welcome, this double secure encryption system
      Double encryption method, double security.
""")

plain = input("Enter plain text: ")
key = input("Enter key string: ")
column = int(input("Enter number of columns: "))

# result = transposition(vigenere(plain, key), column)
first = vigenere(plain, key)
second = transposition(first, column)
third = decrypt_transpose(second, column)
last = decrypt_vigenere(third, key)
print(f"1. Vigenere ciphered: {first}")
print(f"2. Transpose ciphered: {second}")
print(f"3. Transpose reversed: {third}")
print(f"4. Vigenere reversed: {last}")
# print(f"Here is your encrypted message: {result}")


