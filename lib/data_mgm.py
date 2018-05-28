import os
import sys
import json
import random


def json_to_dict(json_request):
    j_dict = {}

    with open(json_request) as json_data:
        j_dict = json.load(json_data)

    return j_dict


def write_text(file_path="", text=""):
    text_file = open(file_path, "w")
    text_file.write(text)
    text_file.close()


def textfile_to_wordlist(input_data):
    file = open(input_data, "r")
    lines = file.readlines()
    words = []

    for l in lines:
        wrd = l.split()
        for w in wrd:
            if len(w) > 0:
                words.append(w)

    return words


def path_to_wordlist(w_list_folder):
    words = []
    file_dict = {}

    for filename in os.listdir(w_list_folder):
        if filename.endswith(".txt"):
            path = w_list_folder + "/" + filename
            words += textfile_to_wordlist(path)

            file_dict[str(filename)] = textfile_to_wordlist(path)

    return words, file_dict


def wash_wlist(wordlist, replace_list):
    clensed_list = []

    for wrd in wordlist:
        new_wrd = ""

        for i in wrd:
            if i not in replace_list:
                new_wrd += i

        clensed_list.append(new_wrd)

    return clensed_list


def path_to_wordlist(w_list_folder):
    words = []
    file_dict = {}

    for filename in os.listdir(w_list_folder):
        if filename.endswith(".txt"):
            path = w_list_folder + "/" + filename
            words += textfile_to_wordlist(path)

            file_dict[str(filename)] = textfile_to_wordlist(path)

    return words, file_dict
