import os
import sys
import json
import random


def write_text(output_path="", text=""):
    text_file = open(output_path, "w")
    text_file.write(text)
    text_file.close()

def wash_wlist(wordlist, replace_list, title=True, upper=False):
    clensed_list = []

    for wrd in wordlist:
        clean = ""

        for i in wrd:
            if i not in replace_list:
                clean += i

        if upper:
            clean = clean.upper()
        else:
            clean = clean.lower()

        if title:
            clean = clean.title()

        clensed_list.append(clean)

    return clensed_list


def textfile_to_wordlist(txt_path, min_len=0):
    file = open(txt_path, "r")
    lines = file.readlines()
    words = []

    for l in lines:
        wrd = l.split()
        for w in wrd:
            if len(w) > min_len:
                words.append(w)

    return words


def path_to_wordlist(text_dir, ext=".txt", min_w_len=0):
    words = []
    file_dict = {}

    for filename in os.listdir(text_dir):
        if filename.endswith(ext):
            path = text_dir + "/" + filename
            words += textfile_to_wordlist(path)

            file_dict[str(filename)] = textfile_to_wordlist(path, min_w_len)

    return words, file_dict
