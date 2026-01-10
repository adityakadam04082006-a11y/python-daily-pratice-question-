# Problem Statement
# Write a Python program that:
# Takes a sentence as input
# Prints all words whose length is greater than or equal to 4
# Counts how many such words exist
# If no such word exists, print "No long words found"

sentence = (input("write the sentence :"))

words = sentence.split()
count = 0
print("words with length >= 1")

for w in words:
    if(len(w) >=4):
        print (w)
        count += 1

if (count == 0):
    print("no long words found")

else:
    print("total count:",count)    