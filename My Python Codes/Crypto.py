alphabet= "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext):
    ciphertext= ""
    for i in range(0, len(plaintext)):
        for j in range(0, len(alphabet)):
            if plaintext[i]==alphabet[j]:
                ciphertext+=alphabet[(j+3)%26]
    print("Encrypted Message:", ciphertext)