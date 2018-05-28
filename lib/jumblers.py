import os
import sys
import random


def get_morphword(wordlist_a, wordlist_b, word_count):
    result = []
    wrdct = int(word_count*0.5)

    for i in range(wrdct):
        word_a = random.choice(wordlist_a)
        word_b = random.choice(wordlist_b)

        first_a = word_a[:int(len(word_a) * 0.5)]
        first_b = word_b[:int(len(word_b) * 0.5)]

        last_a = word_a[int(len(word_a) * 0.5):]
        last_b = word_b[int(len(word_b) * 0.5):]

        word_a = (first_a.lower() + last_b.lower())
        word_b = (first_b.lower() + last_a.lower())

        result.append((word_a.title()))
        result.append((word_b.title()))

    return result


def get_multiword(wordlist_a, wordlist_b, word_count):
    result = []

    for i in range(word_count):
        word_a = random.choice(wordlist_a).lower()
        word_b = random.choice(wordlist_b).lower()

        result.append(word_a.title() + " " + word_b.title())

    return result
