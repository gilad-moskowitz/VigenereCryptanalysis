import math

def gcd_list(integers):
    listToUse = [i for i in integers]
    if (len(listToUse) == 0):
        return 0
    if (len(listToUse) == 1):
        return listToUse[0]
    while (len(listToUse) > 2):
        listToUse.append(math.gcd(listToUse[0], listToUse[1]))
        listToUse.pop(0)
        listToUse.pop(0)
    return math.gcd(listToUse[0], listToUse[1])
    
def frequencyOfLetters(string):
    Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return [string.lower().count(Alphabet[i]) for i in range(0, 26)]
    
def KasiskiTest(ciphertext, substringlen = 3, start = 0, stop = False):
    a = 0
    test = ciphertext[start:(start + substringlen)]
    duplicateIndices = []
    while(a < len(ciphertext) - substringlen):
        duplicate = True
        for i in range(0, substringlen):
            if(ciphertext[a + i].lower() != test[i].lower()):
                duplicate = False
                break
        if(duplicate):
            duplicateIndices.append(a)
            a += 2
        a += 1
    distances = [i - duplicateIndices[0] for i in duplicateIndices]
    if((len(distances) >= 3) or (stop)):
        return gcd_list(distances)
    elif(start < len(ciphertext) - substringlen):
        newStart = start + 1
        return KasiskiTest(ciphertext, substringlen, newStart)
    else:
        return -1
        
def indexOfCoincidence(ciphertext, mValue = 1):
    maxLen = int(len(ciphertext)/mValue)
    totalIOC = []
    for i in range(0, mValue):
        substring_list = [ciphertext[i + j*mValue] for j in range(0, maxLen)]
        substring = ""
        for x in substring_list:
            substring += x
        freq = frequencyOfLetters(substring)
        IOC = 0
        for q in range(0, 26):
            IOC += (freq[q]*(freq[q] - 1))/(len(substring)*(len(substring) - 1))
        totalIOC.append(IOC)
    return (sum(totalIOC)/len(totalIOC))
    
def findingTheKey(ciphertext, guessedM):
    probabilities = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
    maxLen = int(len(ciphertext)/guessedM)
    key = []
    for i in range(0, guessedM):
        #print(i)
        substring_list = [ciphertext[i + j*guessedM] for j in range(0, maxLen)]
        if((i + guessedM*maxLen) < len(ciphertext)):
            substring_list.append(ciphertext[i + guessedM*maxLen])
        substring = ""
        for x in substring_list:
            substring += x
        freq = frequencyOfLetters(substring)
        allM = []
        #print(substring)
        for g in range(0, 26):
            M_g = 0
            for t in range(0, 26):
                M_g += (probabilities[t]*freq[(t + g)%26])/len(substring)
            allM.append(abs(M_g - 0.065))
            #print(M_g)
        key.append(allM.index(min(allM)))
    return key
    
def CryptoAnalysisVigenere(ciphertext):
    Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    allPossiblePlainTexts = {}
    for i in range(3, int(len(ciphertext)**(1/2))):
        guessedM = KasiskiTest(ciphertext, i, 0)
        if(guessedM != -1):
            break
    testingIOC = []
    if(guessedM == -1):
        for length in range(1, int(len(ciphertext)/2)):
            testingIOC.append(indexOfCoincidence(ciphertext, length))
        for test in testingIOC:
            if((0.05 < test) and (0.08 > test)):
                current_m = testingIOC.index(test) + 1
                key = findingTheKey(ciphertext, current_m)
                plaintext = ""
                for j in range(0, len(ciphertext)):
                    plaintext += Alphabet[(Alphabet.index(ciphertext[j].lower()) - key[j%current_m])%26]
                allPossiblePlainTexts[testingIOC.index(test) + 1] = [key, plaintext]
    else:
        key = findingTheKey(ciphertext, guessedM)
        plaintext = ""
        for j in range(0, len(ciphertext)):
            plaintext += Alphabet[(Alphabet.index(ciphertext[j].lower()) - key[j%guessedM])%26]
        allPossiblePlainTexts[guessedM] = [key, plaintext]
    return allPossiblePlainTexts
