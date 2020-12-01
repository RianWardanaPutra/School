'''
Simple hashing function
Made by: Fransiskus Rian Wardana Putra
this simple hash function returns string
by creating tables and summing char value
into that specific tables by index.
ex:
plaintext: brown fox jumps
table column: 4

 0 1 2 3|
 b r o w|
 n f o x|
 j u m p|
 s      |
 -------- +
[a b c d]: a contains int value of (b+n+j+s) and so on

after that, calculate [a b c d] mod column
that [a b c d] is the result
'''

# Import random for the padding if plaintext length is not long enough
import random

def hash_fun(plain, cols=4):
    seed = 0
    for i in plain:
        seed += ord(i)
    random.seed(seed)
    placeholder = [0] * cols
    result = ''
    start_char = 97 # 'a'
    if len(plain) < cols:
        for i in range(cols - len(plain)):
            if len(plain) >= cols:
                break
            plain += chr(start_char + random.randint(0, 26))

    print(plain)
    for i in range(len(plain)):
        modulo = i % cols
        placeholder[modulo] += (ord(plain[i]))
    for i in range(cols):
        placeholder[i] %= cols
        result += chr(placeholder[i] + start_char)

    return result

def main():
    plain = input("Masukkan plaintext: ")
    hash_res = hash_fun(plain)
    print(hash_res)

if __name__ == "__main__":
   main()
