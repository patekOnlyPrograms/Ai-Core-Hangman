import random

word_list = ["apple", "banana", "cherry", "date", "elderberry"]
print(word_list)
choice = random.choice(word_list)
word = choice
print(word)



def check_guess(guess):
    lowerCaseguess = guess.lower()
    if len(lowerCaseguess) == 1 and lowerCaseguess.isalpha():
        if lowerCaseguess in word:
            print(f"Good guess {lowerCaseguess} is in the word")
        else:
            print(f"Sorry, {lowerCaseguess} is not in the word, try again")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

def ask_for_input():
    while True:
        guess = input("Enter a singe letter to guess the word \n")
        check_guess(guess)

ask_for_input()
