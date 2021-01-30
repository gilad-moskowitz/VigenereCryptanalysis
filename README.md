# VigenereCryptanalysis

## Base Algorithm

This algorithm uses the Kasiski test to try to find the most likely "m" value for the Vigenere Cipher. 
If it get's an "m" value, it makes sure that the corresponding index of coincidence is close to 0.065.
If it doesn't get a result from the Kasiski test, or the result from the Kasiski test has a poor index of coincidence (not close to 0.065), it checks the index of coincidence for all the "m" values between 1 and the integer approximation of the square root of the cipher length. 
It takes the top "m" values with index of coincidence in range 0.05 and 0.08 and solves for the most likely key for a given "m" value. 
Finally, it outputs a dictionary of "m" values, where for each "m" the corresponding dictionary value is an array with the most likely key and plaintext corresponding to that key. It find's the keys by calculating the M_g value for each potential element of the key and then puts the key together using the elements that gave the M_g value closest to 0.065.

## Bigram Algorithm

This algorithm uses the Kasiski test to try to find the most likely "m" value for the Vigenere Cipher. 
If it get's an "m" value, it makes sure that the corresponding index of coincidence is close to 0.065.
If it doesn't get a result from the Kasiski test, or the result from the Kasiski test has a poor index of coincidence (not close to 0.065), it checks the index of coincidence for all the "m" values between 1 and the integer approximation of the square root of the cipher length. 
It takes the top "m" values with index of coincidence in range 0.05 and 0.08 and solves for the most likely key for a given "m" value. 
Finally, it outputs a dictionary of "m" values, where for each "m" the corresponding dictionary value is an array with the most likely key and plaintext corresponding to that key. This algorithm calculates the key by looking at log of bigram frequencies for each potential bigram. It finds the bigram most likely corresponding to the key by breaking the ciphertext into bigrams and seeing which key bigram would best math the frequency of bigrams used in the English language. It creates an array of the most likely potential key bigrams and their corresponding score (frequency probability of the plaintext bigram if using this specific key bigram) and then calculates a potential key using the same methodology as the base algorithm. It then compares the calculated potential key to the array of key bigrams and picks the final key based on maximizing the probabilities. 

For this algorithm be sure to download the code for the algorithm and also the code for the bigramFreq in order to get the proper bigram frequencies. The data used in the bigramFreq file came from http://practicalcryptography.com/media/cryptanalysis/files/english_bigrams_1.txt on January 29th 2021.
