# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    story = open(filename, "r")
    txt = story.read()
    return txt


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    print(text)
    each_word = text.split()

    from collections import Counter
    word_count = Counter(each_word)
    #while x < len(each_word):
    for k in each_word:
        #print(k[-1])
        if (k[-1] != "." and k[-1] != "," and k[-1] != " " and k[-1] != "?"):
            print(k, " : ", word_count[k])
        else:
            print(k[:-1], " : ", word_count[k])
        #break
    return {k, " : ", word_count[k]}

count_words()