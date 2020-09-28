def encrypt(plain, column):
    cipher = ''
    numLines = len(plain) // column
    if(numLines * column) < len(plain):
        numLines += 1
    block = [[" " for i in range(column)] for j in range(numLines)]

    i = 0
    j = 0

    for k in plain:
        block[i][j] = k
        j = (j+1) % column
        if j == 0:
            i += 1

    for j in range(column):
        for i in range(numLines):
            cipher += block[i][j]

    return cipher

def decrypt(cipher, column):
    plain = ''
    numLines = len(cipher) // column
    if(numLines * column) < len(cipher):
        numLines += 1
    block = [[" " for i in range(numLines)] for j in range(column)]

    i = 0
    j = 0

    for k in cipher:
        block[j][i] = k
        i = (i+1) % numLines
        if i == 0:
            j += 1

    for i in range(numLines):
        for j in range(column):
            plain += block[j][i]

    return plain

plain = input("Enter text: ")
column = int(input("Column: "))

print(decrypt(plain, column))
