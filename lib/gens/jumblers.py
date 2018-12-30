import os
import sys
import random


def word_morph(wordlist_a, wordlist_b, word_count, pre="", suf=""):
    result = []
    wrdct = int(word_count * 0.5)

    for i in range(wrdct):
        word_a = random.choice(wordlist_a)
        word_b = random.choice(wordlist_b)

        first_a = word_a[:int(len(word_a) * 0.5)]
        first_b = word_b[:int(len(word_b) * 0.5)]

        last_a  = word_a[int(len(word_a)  * 0.5):]
        last_b  = word_b[int(len(word_b)  * 0.5):]

        word_a = (first_a.lower() + last_b.lower())
        word_b = (first_b.lower() + last_a.lower())

        result.append((word_a.upper()))
        result.append((word_b.upper()))

    return result


def word_mix(wordlist_a, wordlist_b, word_count, pre="", suf="", separator=" "):
    result = []

    for i in range(word_count):
        word_a = random.choice(wordlist_a).lower()
        word_b = random.choice(wordlist_b).lower()

        result.append(word_a.upper() + separator + word_b.upper())

    return result
