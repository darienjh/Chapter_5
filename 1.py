import random

words = [""]

while words != "":
    for i in words:
        word = input("Please enter a word: ")
        words.append(word)
        print(random.choice(words))
        
