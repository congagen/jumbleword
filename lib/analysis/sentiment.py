import random
from statistics import mean


def naive_word_score(word, sent_dict, missing_sent=0.5):
    if word in sent_dict.keys():
        return sent_dict[word]
    else:
        return missing_sent


def naive_text_score(input_text, sent_dict={}, split_wrd=" ", scale_resolution=1):
    scores = []
    conviction = 0

    if len(sent_dict.keys()) > 0:
        for w in input_text.split(split_wrd):
            clean = w.lower()
            scores.append(naive_word_score(w, sent_dict))

        return {"score":mean(scores), "conviction":conviction}
    else:
        return {"score":0, "conviction":0}
