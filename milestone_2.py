import random as rd

characters=[]
letters='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
for i in letters:
    characters.append(i)

word_list_basic=['banana', 'apple', 'orange', 'kiwi', 'pineapple']
word=rd.choice(word_list)

while __name__ == "__main__":
   

    guess=input('Input a letter you think is right').strip()
    if len(guess) == 1 and guess in characters:
        print('Good guess')
    else:
        print('That\'s not a valid guess, try again')
        print(len(guess))
        guess=input('Input a letter you think is right')
