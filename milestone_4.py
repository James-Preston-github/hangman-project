import random as rd


def make_word_guessed(word):
    list_of_blanks=[]
    list_of_letters={}
    for letter in word:
        list_of_blanks.append('_')
        list_of_letters.append(letter)
    return [list_of_blanks, list_of_letters]

def make_num_letters(word, word_guessed):
    unique_letters=make_word_guessed(word)[1]
    num_of_unique_letters=len(unique_letters)
    


class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.num_lives=num_lives
        self.word_list=word_list
        self.word=rd.choice(word_list)
        self.word_guessed=make_word_guessed(self.word)
