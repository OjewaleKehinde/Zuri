# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    file = open(filename, "r")
    
    return file.read()


def count_words():
    text = read_file_content("./story.txt")
    import re
    words = re.split("[^a-zA-Z]+", text)
    word_count = {}
    for i in words:
        freq=words.count(i)
        word_count[i]=freq
    return word_count





