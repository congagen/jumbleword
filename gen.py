import os
import sys
import json
import random

from lib import data_mgm
from lib import generators


def main(order_json):
    order_dct = data_mgm.json_to_dict(order_json)

    word_count_mixed = int(order_dct["word_count_mixed"])
    word_count_morph = int(order_dct["word_count_morph"])

    all_words = data_mgm.path_to_wordlist(order_dct["root_wordlist_path"])
    wordlist_a = data_mgm.path_to_wordlist(order_dct["wordlist_a_path"])
    wordlist_b = data_mgm.path_to_wordlist(order_dct["wordlist_b_path"])

    mixed = generators.get_multiword(wordlist_a[0],
                                    wordlist_b[0],
                                    word_count_mixed)

    morph = generators.get_morphword(all_words[0],
                                    all_words[0],
                                    word_count_morph)

    clean_mixed = data_mgm.wash_wlist(mixed, order_dct["remove"])
    clean_morph = data_mgm.wash_wlist(morph, order_dct["remove"])

    if order_dct["print_to_console"]:
        print("-" * 80)
        print(clean_mixed)

        print("-" * 80)
        print(clean_morph)


    if order_dct["save_to_disk"]:
        data_mgm.write_text(order_dct["output_path_mixed"], str(clean_mixed))
        data_mgm.write_text(order_dct["output_path_morph"], str(clean_morph))


main("order.json")
