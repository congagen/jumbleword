import re
import random
from collections import Counter
import pprint


def sort_text_basic(i_text, exc=[], ignore_list=[], min_w_len=1):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    i_text = ansi_escape.sub('', i_text)

    if len(exc) == 0:
        exc = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?", ";", ":"]

    w_clean = [(i.lower() if i not in exc else "") for i in i_text]
    clean = "".join(w_clean).split(" ")

    w_dct = {}

    for i in range(len(clean)):
        if i < len(clean)-1:
            cur_w = clean[i].lower()
            nxt_w = clean[i + 1].lower()

            if nxt_w.lower not in ignore_list and len(nxt_w) > min_w_len:

                if nxt_w not in w_dct.keys():
                    w_dct[nxt_w] = []
                    w_dct[nxt_w].append("")

                if cur_w not in w_dct.keys():
                    w_dct[cur_w] = []

                w_dct[cur_w].append(nxt_w)

    return w_dct


def write_basic(w_dct, sent_count=10, sent_len=[18, 22]):
    random.seed()
    pre_w = ""
    pre_w = random.choice(list(w_dct.keys()))
    o_text = {}

    for s in range(sent_count):
        o_text[s] = pre_w + " "

        temp_wd = w_dct
        cur_sel = []
        w_pos = "start"

        while len(o_text[s].split(" ")) < random.randrange(sent_len[0], sent_len[1]):
            #print("Writing...")

            if len(temp_wd[pre_w]) > 1:
                most_com = Counter(temp_wd[pre_w]).most_common()

                scoreboard = {i[0]: i[1] for i in most_com}
                scoreboard.pop("")
                new_w = random.choices(*zip(*scoreboard.items()))[0]

                # TODO: Check sentposition / gramm / neighbours
                #if len(o_text[s].split(" ")) == sent_len-1:
                #    w_pos = "stop"
                #    new_w = random.choices(*zip(*scoreboard.items()))[0]

                if new_w == pre_w:
                    if new_w in temp_wd[pre_w]:
                        temp_wd[pre_w].remove(new_w)

                    pre_w = new_w

                else:
                    if w_pos == "stop":
                        o_text[s] += str("Stop: ") + new_w
                    else:
                        o_text[s] += str(new_w) + " "

                    pre_w = str(new_w)
            else:
                pre_w = random.choice(list(temp_wd.keys()))

        o_text[s] = o_text[s][:-1].capitalize() + "."

    return o_text


def basic_gen(i_paths, min_w_len=2, sent_count=10, sent_wcount=[18, 22]):
    raw_text = ""

    for p in i_paths:
        with open(p) as f:
            raw_text += f.read().replace('\n', ' ')

    dct = sort_text_basic(raw_text, min_w_len=min_w_len)
    txt = write_basic(
        dct,
        sent_count=sent_count,
        sent_len=sent_wcount
    )

    return txt
