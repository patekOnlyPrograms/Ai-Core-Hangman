while True:
    guess = input("Enter a singe letter to guess the word \n")
    if len(guess) == 1 and guess.isalpha():
        print("Good guess")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")