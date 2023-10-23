import random

word_list = ["apple", "banana", "cherry", "date", "elderberry"]
print(word_list)
choice = random.choice(word_list)
word = choice
print(word)
guess = input("Enter a singe letter to guess the word \n")
if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input.")
