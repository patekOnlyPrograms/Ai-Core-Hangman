import random


class Hangman:
    """
    A class to represent a hangman game

    Attributes

    word_list: list
        a list of available words that can be chosen at random
    num_lives: int
        number of lives available for the player
    word:
        random word chosen from random picker
    word_guessed: list
        a list showing letters that have been guessed
    num_letters: int
        number of letters in the word
    list_of_guesses: list
        shows a list of guesses that have been made
    """

    def __init__(self, word_list, num_lives=5):
        """

        :param word_list:
        :param num_lives:
        """

        self.world_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in range((len(self.word)))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess {guess} is in the word")
            self.num_letters -= 1
            for i, letter in enumerate(self.word):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Enter a singe letter to guess the word \n")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            if len(guess) == 1 and guess.isalpha() and guess not in self.list_of_guesses:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                # print(self.list_of_guesses)


word_list = ["apple", "banana", "cherry", "date", "elderberry"]
hangmanGame = Hangman(word_list)
print(hangmanGame.word)
print(hangmanGame.word_guessed)
print(hangmanGame.num_letters)
print(hangmanGame.list_of_guesses)
hangmanGame.ask_for_input()
