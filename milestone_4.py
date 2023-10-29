import random as rd
from milestone_2 import word_list, characters

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
    def __init__(self,word_list,num_lives=5):
        self.num_lives=num_lives
        self.word_list=word_list
        self.word=rd.choice(word_list)
        self.word_guessed=make_word_guessed(self.word)[0]
        self.num_letters=len(make_word_guessed(self.word)[1])
        self.list_of_guesses=[]
    
    def check_guess(self,guess):
        guess=guess.lower().strip()
        if guess in self.word:
            print(f'Good guess, {guess} is in the word')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i]=guess
            self.num_letters-=1
            print(self.word_guessed,self.num_letters)
        else:
            self.num_lives-=1
            print(f'Sorry, {guess} isn\'t in the word')
            print(f'Sorry, you lose a life, you now have {self.num_lives} lives left')

    def ask_for_input(self):
        while True:
            guess=input("Guess a letter that might be in the word")
            if not guess.isalpha():
                print('Invalid letter, guess again')
            elif guess in self.list_of_guesses:
                print('You already tried that letter')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

guesss=Hangman(word_list,5)
guesss.ask_for_input()

