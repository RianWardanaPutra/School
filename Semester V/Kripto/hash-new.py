# Import random for the padding if plaintext length is not long enough
import random

def hash_fun(plain, cols=4):
    seed = 0
    for i in plain:
        seed += ord(i)
    random.seed(seed)
    placeholder = [0] * cols
    result = ''
    if len(plain) < cols:
        for i in range(cols - len(plain)):
            if len(plain) >= cols:
                break
            plain += chr(random.randint(0, 26))

    print(plain)
    for i in range(len(plain)):
        modulo = i % cols
        placeholder[modulo] += (ord(plain[i]))
    for i in range(cols):
        placeholder[i] %= cols
        result += (placeholder[i])

    return result

def main():
    plain = input("Masukkan plaintext: ")
    hash_res = hash_fun(plain)
    print(hash_res)

if __name__ == "__main__":
   main()
