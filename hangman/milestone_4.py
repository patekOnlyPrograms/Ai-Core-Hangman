import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.world_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in range((len(self.word) - 1))]
        self.num_letters = len(self.word) - 1
        self.list_of_guesses = []


word_list = ["apple", "banana", "cherry", "date", "elderberry"]
hangmanGame = Hangman(word_list)
print(hangmanGame.word)
print(hangmanGame.word_guessed)
print(hangmanGame.num_letters)
print(hangmanGame.list_of_guesses)
