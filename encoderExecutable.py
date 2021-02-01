import math

def VigenereEncoder(plaintext, key):
    Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphaPlain = ""
    numericKey = [Alphabet.index(i.lower()) for i in key]
    for char in plaintext:
        if(char.isalpha()):
            alphaPlain += char
    ciphertext = ""
    for j in range(0, len(alphaPlain)):
        ciphertext += Alphabet[(Alphabet.index(alphaPlain[j].lower()) + numericKey[j%len(numericKey)])%26]
    return ciphertext

def getKeyWord():
    key = input("Please enter the key word: ")
    keyWordOk = True
    for k in key:
        if(k.isalpha()):
            continue
        else:
            print("The keyword must be made of only english alphabetic characters.")
            return getKeyWord()
    return key

if __name__ == '__main__':
    plaintext = input("Please enter the text you want encoded (note that only the alphabetic characters will be encoded): ")
    keyword = getKeyWord()
    ciphertext = VigenereEncoder(plaintext, keyword)
    print(ciphertext)
    input("End.")
