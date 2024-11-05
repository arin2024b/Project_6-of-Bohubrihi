import string
from collections import Counter


def clean_text(text):

    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    return cleaned_text


def count_words_in_file(file_path):

    with open(file_path, 'r') as file:
        text = file.read()


    cleaned_text = clean_text(text)

    words = cleaned_text.split()
    word_count = Counter(words)

    return word_count


def check_word_count(word_count, word_list):

    for word in word_list:
        if word in word_count:
            print(f"'{word.upper()}' -> {word_count[word]} ")
        else:
            print(f"'{word.upper()}' -> 0")



file_path = 'input.txt'

word_list = ["python","c","oop","hello","java"]

word_count = count_words_in_file(file_path)

check_word_count(word_count, word_list)

