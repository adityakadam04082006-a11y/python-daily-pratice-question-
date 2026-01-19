# Problem Statement
# Write a Python program that:
# Takes a sentence as input
# Prints all words that contain at least one vowel
# Displays which vowels are present in the sentence
# Prints the total number of words containing vowels


sentence = input("write the sentence :")
words = sentence.split()

count = 0
vowel_found = []
print("words starting with a vowel :")

for w in words:
    w_lower = w.lower()
    if ('a' in w_lower  or 'e'in w_lower or 'i' in w_lower  or 'o'in w_lower or 'u'in w_lower ):
        print(w)
count += 1

for ch in sentence.lower():
    if ch in ['a','e','i','o','u']:  

      if ch not in vowel_found:
       vowel_found.append(ch)

       if count == 0 :
        print("no word with vowel found")
else:
    print("total count:",count)

print("vowel found :",vowel_found)
    
#steps of how this code works
#first loop _ word-level logic
#second loop - character-level logic
#if checks existence
#count tracks words
# vowwel_found tracks unique vowels
