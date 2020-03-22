import sys
import json
import pprint

from lib import utils
from lib.gens import jumblers
from lib.gens import markov
from lib.gens import ml
from lib.analysis import sentiment

# ------------------------------------------------------------------------------

def main(args):
    response = {}

    with open(args[1]) as json_data:
        order = json.load(json_data)

    if "w_mix" in order.keys():
        response["w_mix"] = {}
        wordlist_a = utils.path_to_wordlist(order["w_mix"]["wordlist_path_a"])
        wordlist_b = utils.path_to_wordlist(order["w_mix"]["wordlist_path_b"])

        if order["w_mix"]["word_count"] > 0:
            mixed = jumblers.word_mix(
                wordlist_a[0],wordlist_b[0], int(order["w_mix"]["word_count"]))

            morph = jumblers.word_morph(
                wordlist_a[0], wordlist_b[0], int(order["w_mix"]["word_count"]))

            response["w_mix"]["mixed"] = utils.wash_wlist(mixed, order["w_mix"]["remove"])
            response["w_mix"]["morph"] = utils.wash_wlist(morph, order["w_mix"]["remove"])

    if "markov" in order.keys():
        response["markov"] = markov.basic_gen(
            order["markov"]["i_txt_paths"],
            sent_count=order["markov"]["sent_count"],
            sent_wcount=[order["markov"]["min_sent_w_count"], order["markov"]["max_sent_w_count"]]
        )

    # if "sentiment" in order.keys():
    #     i_text = order["sentiment"]["text"]
    #     response["sentiment"] = sentiment.naive_text_score(i_text)

    return response


if __name__ == "__main__":
    pprint.pprint(main(sys.argv))
