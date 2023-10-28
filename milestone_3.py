from milestone_2 import word_list, characters, word
print(word)

def check_guess(guess):
    guess=guess.lower()
    if guess in word:
        print(f'Good guess, {guess} is in the word')
    else:
        print(f'Sorry, that\'s not in the word, try again')

def ask_for_input():
    while True:
        guess=input('Guess a letter').strip()
        if guess.isalpha():
            break
        else:
            print('Invalid guess, try again with a SINGLE letter')
    check_guess(guess)


ask_for_input()
