import random as rd
from word_list_in_list_form import word_list

def make_word_guessed(word):
    list_of_blanks=[]
    list_of_letters=set({})
    for letter in word:
        list_of_blanks.append('_')
        list_of_letters.add(letter)
    return [list_of_blanks, list_of_letters]

def make_num_letters(word, word_guessed):
    unique_letters=make_word_guessed(word)[1]
    num_of_unique_letters=len(unique_letters)



class Hangman:
    def __init__(self,word,num_lives,vowel_answer):
        self.num_lives = num_lives
        self.word = word
        self.vowel_answer=vowel_answer
        self.word_guessed = make_word_guessed(self.word)[0]
        self.num_letters = len(make_word_guessed(self.word)[1])
        self.list_of_guesses = []
    

    def check_guess(self,guess):
        print(guess)
        if guess in self.word:
            print(f'Good guess, {guess} is in the word')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} isn\'t in the word, so you lose a life, you now have {self.num_lives} lives left')

    def add_vowels(self):
        if self.vowel_answer == True:
            for vowel in ['a','e','i','o','u']:
                if vowel in self.word:
                    for i in range(len(self.word)):
                        if self.word[i] == vowel:
                            self.word_guessed[i] = vowel
                    self.num_letters -= 1
            print(f'The current state of the game is {self.word_guessed}, get to guessing:')
    def ask_for_input(self):
            guess = input("Guess a letter that might be in the word ").strip().lower()
            if not guess.isalpha() or len(guess) > 1:
                print('Invalid entry, guess a single letter')
            elif guess in self.list_of_guesses:
                print('You already tried that letter')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


def play_game(word_list):
    word=rd.choice(word_list)
    while len(word) <= 3 or len(word) >= 10:
        word=rd.choice(word_list)
    vowel_answer=input(f"Do you want all the vowels to be given already, the word is {len(word)} long? (answer either 'True' or 'False')")
    if vowel_answer.strip() in ['True', 'true','yes','yeah']:
        vowel_answer=True
    else:
        vowel_answer=False
    num_lives=int(input(f'How much you  back yourself, boss; i.e. how many lives do you want?'))
    game=Hangman(word,num_lives, vowel_answer)
    game.add_vowels()
    while True:
        if game.num_lives == 0:
            print(f'You lose, the answer was {word}')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print(f'Congrats, you won the game! And you had {game.num_lives} lives left')
            break
        

play_game(word_list)

