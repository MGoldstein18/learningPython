# count how many unique English letters there in a string

def unique_english_letters(word):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    count = 0
    for letter in letters:
        if letter in word:
        count += 1
    return count


# count how many time a letter appears in a String
def count_char_x(word, x):
    count = 0
    for letter in word:
        if letter == x:
            count += 1
    return count


# count how many time a phrase appears in a String
def count_multi_char_x(word, x):
    count = 0
    return(len(word.split(x)) - 1)


# find a substring in between the provided letters of a String
def substring_between_letters(word, start, end):
    if not start in word or not end in word:
        return word
    else:
        return word[word.find(start) + 1:word.find(end)]


# check that all words in a given sentence are longer than x characters
def x_length_words(sentence, x):
    words = sentence.split()
    for word in words:
        if len(word) < x:
            return False
    return True


# check if a word appears in a sentence which may upper and lower case letters
def check_for_name(sentence, word):
    if word.lower() in sentence.lower():
        return True
    return False


# function to return every other letter of a given word
def every_other_letter(word):
    new_word = ""
    for i in range(len(word)):
        if i % 2 == 0:
            new_word += word[i]
    return new_word


# reverse a String
def reverse_string(word):
    new_word = ""
    for i in range(len(word) - 1, -1, -1):
        new_word += word[i]
    return new_word


# 