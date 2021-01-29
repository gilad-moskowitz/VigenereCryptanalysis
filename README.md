# VigenereCryptanalysis

## Base Algorithm

This algorithm uses the Kasiski test to try to find the most likely "m" value for the Vigenere Cipher. 
If it get's an "m" value, it makes sure that the corresponding index of coincidence is close to 0.065.
If it doesn't get a result from the Kasiski test, or the result from the Kasiski test has a poor index of coincidence (not close to 0.065), it checks the index of coincidence for all the "m" values between 1 and the integer approximation of the square root of the cipher length. 
It takes the top "m" values with index of coincidence in range 0.05 and 0.08 and solves for the most likely key for a given "m" value. 
Finally, it outputs a dictionary of "m" values, where for each "m" the corresponding dictionary value is an array with the most likely key and plaintext corresponding to that key. 
