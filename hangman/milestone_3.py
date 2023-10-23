import random

word_list = ["apple", "banana", "cherry", "date", "elderberry"]
print(word_list)
choice = random.choice(word_list)
word = choice
print(word)
while True:
    guess = input("Enter a singe letter to guess the word \n")
    if len(guess) == 1 and guess.isalpha():
        print("Good guess")
        if guess in word:
            print(f"Good guess {guess} is in the word")
        else:
            print(f"Sorry, {guess} is not in the word, try again")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")