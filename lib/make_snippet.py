def make_snippet(string):
#make string a list of words
    word_list = string.split(" ")
    if len(word_list) > 5:
#return the first five words from the list 
        five_words = word_list[0:5]
#join the first 5 words in a list with a space in between
        new_words_joined = ' '.join(five_words)
        return new_words_joined + '...'
    else:
        return string 