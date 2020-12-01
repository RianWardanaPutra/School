def encrypt(plain, password):
    plainIntVector = []
    for i in plain:
        plainIntVector.append(ord(i))
    passwordIntVector = []
    for i in password:
        passwordIntVector.append(ord(i))

    plainIndex = 0
    cipherIntVector = []
    while plainIndex < len(plain):
        for i in range(len(password)):
            if plainIndex == len(plain): break
            oneCharCipher = plainIntVector[plainIndex] ^ passwordIntVector[i]
            cipherIntVector.append(oneCharCipher)
            plainIndex += 1
    return cipherIntVector

def decrypt(cipher, password):
    cipherIndex = 0
    plainIntVector = []
    while cipherIndex < len(cipher):
        for i in password:
            if cipherIndex == len(cipher):
                break
            oneCharPlain = cipher[cipherIndex] ^ ord(i)
            plainIntVector.append(oneCharPlain)
            cipherIndex += 1
    plain = [chr(i) for i in plainIntVector]
    plain = ''.join(plain)
    return plain


plain = input("Plain text: ")
password = input("Password: ")

cipher = encrypt(plain, password)
print("Cipher: ", end='')
for i in cipher:
    print(i, end=' ')


print("\nPlaintext: " + decrypt(cipher, password))
