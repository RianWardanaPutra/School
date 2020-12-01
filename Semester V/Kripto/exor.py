# Fungsi enkripsi
def encrypt(plain,password):
    plainIntVector = []
    for i in range(len(plain)):
        plainIntVector.append(ord(plain[i]))
    passwordIntVector = []

    # inisiasi variabel baru untuk membuat setiap perubahan yang terjadi pada
    # password akan menyebabkan avalanche effect
    # variabel ini berisi jumlahan dari nilai ascii password dipangkatkan 
    # panjang password mod 256, agar tidak melebihi jumlah ascii
    added_value = pow(sum([ord(i) for i in password]), len(password), 256)
    for i in range(len(password)):
        passwordIntVector.append((ord(password[i]) + added_value) % 256)

    # fungsi lainnya tidak berubah
    plainIndex = 0
    cipherIntVector = []
    while plainIndex < len(plain):
        for i in range(len(password)):
            if plainIndex == len(plain):
                break
            oneCharCipher = plainIntVector[plainIndex]^passwordIntVector[i]
            cipherIntVector.append(oneCharCipher)
            plainIndex += 1
    return cipherIntVector

def decrypt(cipherIntVector,password):
    passwordIntVector = []

    # fungsi yang sama seperti fungsi cipher juga dimasukkan di sini
    # agar decipher menghasilkan karakter yang sama
    added_value = pow(sum([ord(i) for i in password]), len(password), 256)
    for i in range(len(password)):
        passwordIntVector.append((ord(password[i]) + added_value) % 256)

    cipherIndex = 0
    plainIntVector = []
    while cipherIndex < len(cipherIntVector):
        for i in range (len(password)):
            if cipherIndex == len(cipherIntVector):
                break
            oneCharPlain = cipherIntVector[cipherIndex]^passwordIntVector[i]
            plainIntVector.append(oneCharPlain)
            cipherIndex += 1
    plain = ''
    for i in range(len(plainIntVector)):
        plain = plain + chr(plainIntVector[i])
    return plain

plain = input("Plain text: ")
password = input("Password: ")

cipher = encrypt(plain, password)
print ("Cipher: ", end='')
print(cipher)
print("Cipher in hex:", end=" ")
for i in cipher:
    print(f"{i:02X}", end=" ")
print()
print("Plain: " + decrypt(cipher,password))
