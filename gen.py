import os
import sys
import json
import time
import random
from lib import data_mgm
from lib import jumblers

# ------------------------------------------------------------------------------

def generate(order_dct):
    all_words = data_mgm.path_to_wordlist(order_dct["root_wordlist_path"])
    wordlist_a = data_mgm.path_to_wordlist(order_dct["wordlist_a_path"])
    wordlist_b = data_mgm.path_to_wordlist(order_dct["wordlist_b_path"])

    mixed = jumblers.get_multiword(wordlist_a[0],
                                   wordlist_b[0],
                                   int(order_dct["word_count_mixed"]))

    morph = jumblers.get_morphword(wordlist_a[0],
                                   wordlist_b[0],
                                   int(order_dct["word_count_morph"]))

    clean_mixed = data_mgm.wash_wlist(mixed, order_dct["remove"])
    clean_morph = data_mgm.wash_wlist(morph, order_dct["remove"])

    if order_dct["save_to_disk"]:
        data_mgm.write_text(order_dct["output_path_mixed"], str(clean_mixed))
        data_mgm.write_text(order_dct["output_path_morph"], str(clean_morph))

    return clean_mixed, clean_morph


def main(args):
    order_dct = data_mgm.json_to_dict(args[1])
    wrds = generate(order_dct)

    if int(order_dct["mode"]) == 0:
        if order_dct["print_to_console"]:
            print("")
            print("Mixed: " + str(wrds[0]))
            print("")
            print("Morph: " + str(wrds[1]))
    else:
        for i in wrds[0] + wrds[1]:
            current_settings = data_mgm.json_to_dict(args[1])
            print(i)
            print("-" * len(i))
            time.sleep(float(current_settings["interval"]))


main(sys.argv)
