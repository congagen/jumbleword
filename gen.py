import os
import sys
import json
import time
import random
from lib import data_mgm
from lib import jumblers

# ------------------------------------------------------------------------------

def generate(order):
    all_words = data_mgm.path_to_wordlist(order["root_wordlist_path"])
    wordlist_a = data_mgm.path_to_wordlist(order["wordlist_a_path"])
    wordlist_b = data_mgm.path_to_wordlist(order["wordlist_b_path"])

    mixed = jumblers.get_multiword(wordlist_a[0],
                                   wordlist_b[0],
                                   int(order["word_count_mixed"]))

    morph = jumblers.get_morphword(wordlist_a[0],
                                   wordlist_b[0],
                                   int(order["word_count_morph"]))

    clean_mixed = data_mgm.wash_wlist(mixed, order["remove"])
    clean_morph = data_mgm.wash_wlist(morph, order["remove"])

    return clean_mixed, clean_morph


def main(args):
    order = data_mgm.json_to_dict(args[1])
    wrds = generate(order)

    print("")
    print("Mixed: " + str(wrds[0]))
    print("")
    print("Morph: " + str(wrds[1]))

    if order["save_to_disk"]:
        data_mgm.write_text(order["output_path_mixed"], str(wrds[0]))
        data_mgm.write_text(order["output_path_morph"], str(wrds[1]))


main(sys.argv)
