import random

print("Word Scrambler")

while True:
    word = str(input("Enter a word to scramble or quit:- "))
    if word.lower() == 'quit':
        break
    letters = list(word)
    random.shuffle(letters)
    print(f"Scrambled Letters {"".join(letters)}")
