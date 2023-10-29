# hangman-project
An attempt to code the classic game hangman as efficiently as possible.
To install this fun, little game. Just go into your terminal (assuming you've already got git) and use the code: git clone https://github.com/James-Preston-github/hangman-project.git

Huge long word list lets you try and guess almost any word in the english language (as long as it's longer than 4 letters long)! Happy hanging!!

## Update
Added a feature that lets you pick how many lives you'll want based on the length of the word. It also tells you the answer if you didn't get it in time



milestone_3.py update
So far, I've made a list of all the letters, and taken in an input that checks if your input is a single letter.
I've also done some encapsulation to make the code easier to read and any issues with it easier to diagnose, it's still small as of writing but it'll help in the long run
milestone_5.py update
I've made the game, I had to do some work to make sure that the game only accepted one letter inputs and that it wouldn't penalise you for guessing 'Q' and 'q', but now it works perfectly, my word list is small so I'm going to google a list online that contain more letters. Though it was handy for testing to know all the letters.

Thoughts:
There's an annoying "for i in range(len(self.word))" which I want to remove but I think this one might actually be necessary. 