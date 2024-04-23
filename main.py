#!/usr/bin/env python
from collections import Counter

def get_word_count(content):
    return len(content.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(content):
    lowercase = content.lower()
    #return {x:lowercase.count(x) for x in lowercase}
    return dict(Counter(lowercase))

def dict_of_dict_to_list_of_dict(dict_of_dicts):
    #list_of_dict = list(dict_of_dicts,)
    list_of_dict = []
    for k, v in dict_of_dicts.items():
        some_dict = {"name": k, "num": v}
        list_of_dict.append(some_dict)
    return list_of_dict

def sort_char_count(content):
    # Sort char counts from most to least
    sorted_list = sorted(content, reverse=True, key=lambda d:d['num'])
    return sorted_list

def print_char_count(values):
    for value in values:
        if value["name"].isalpha():
            print(f"The '{value["name"]}' character was found {value['num']} times")

def print_report(book, count, char_count_list):
    print(f"--- Begin report of {book} ---")
    print(f"{count} words found in the document\n")
    print_char_count(char_count_list)
    print("--- End Report ---")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    list_of_dict = dict_of_dict_to_list_of_dict(char_count)
    sorted_list = sort_char_count(list_of_dict)

    print_report(book_path, word_count, sorted_list)

if __name__ == '__main__':
    main()