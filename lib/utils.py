import os
import sys
import difflib
import json
import random


def diff_match(target_string, comp_string_list, composite=False):
    best_match_val = 0
    best_match_string = ""
    m_list = []
    
    for s in comp_string_list:
        di = difflib.SequenceMatcher(None, target_string, str(s)).ratio()
        m_list.append(di)
        
        if di > best_match_val:
            best_match_val = di
            best_match_string = s

    if composite:
        return sum(m_list)/len(m_list), best_match_string
    else:
        return best_match_val, best_match_string


def write_file(output_path="", text=""):
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
