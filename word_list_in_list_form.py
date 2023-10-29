my_list_of_words = open('word_list.txt','r')
data = my_list_of_words.read()
word_list = data.split('\n')
my_list_of_words.close()
