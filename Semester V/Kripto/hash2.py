#!/usr/bin/env python3

# Fungsi untuk penentuan pseudo random value
# fungsi perpangkatan biasa, a pangkat a modulo 41
getA = lambda a: pow(a,a,41)

# fungsi perpangkatan biasa, b pangkat b modulo 47
getB = lambda b: pow(b,b,47)

# fungsi polinomial, x pangkat getA(a) + 7 * getB(b) + 13
# atau sederhananya x ^ a + 7 * b + 13
# dimodulo 256 agar tidak melebihi jumlah ascii
getRandom = lambda x,a,b: (pow(x, getA(a)) + 7*getB(b) + 13)%256

# fungsi hash, dapat memasukkan variabel optional blocksize
def myhash(data, blocksize=16):
    digest = [0]*blocksize

    # inisialisasi variabel awal menggunakan panjang data/plaintext
    # dan isi data/plaintext sehingga didapatkan variabel yang
    # konsisten untuk setiap plaintext yang sama
    a = len(data)+3
    b = sum([ord(i) for i in data])

    # fungsi awal untuk menambahkan karakter random pada data/plaintext
    # apabila panjang data kurang dari panjang blocksize
    while len(data) < blocksize:
        temp = getRandom(13, a, b)
        data += chr(temp)
        a = getRandom(temp, a, b)
        b = getRandom(a, b, temp)

    # inisiasi nilai awal pada block digest.
    # cara kerja program ini untuk membentuk hash digest adalah
    # pertama inisiasi block digest dengan nilai random,
    # dikembangkan dari fungsi awal yang menggunakan 
    # angka 0 sebagai isi block.
    # isi dari tiap iterasi block akan berbeda,
    # karena pengambilan karakter random tiap iterasinya berbeda
    for i in range(blocksize):
        digest[i] = getRandom(ord(data[i]), a, b)
        temp = getRandom(13, a, b)
        a = getRandom(temp, a, b)
        b = getRandom(a, b, temp)

    dataIndex = 0
    end = False
    for i in range(blocksize):
        while dataIndex < len(data) and not end:
            for i in range(blocksize):
                if dataIndex == len(data):
                    dataIndex = 0
                    end = True
                digest[i] = digest[i]^ord(data[dataIndex])
                dataIndex += 1
        return digest

data = input("Data: ")
h = (myhash(data))
for i in range(len(h)):
    print('{:02x}'.format(h[i]),end='')
print()
