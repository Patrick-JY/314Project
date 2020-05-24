from pathlib import Path
import vaderSentiment
import os

def join_base_path(path):
    return Path(__file__).parent.parent.joinpath(path)

def load_vadersentiment_lexicon_data():
    lexicon_data = {}
    with open(os.path.join(vaderSentiment.__path__[0], "vader_lexicon.txt")) as f:
        for line in f:
            lexicon_data[line.split("\t")[0]] = float(line.split("\t")[1])

    return lexicon_data

def get_positive_words():
    lexicon_data = load_vadersentiment_lexicon_data()
    positive_words = []
    for key, value in lexicon_data.items():
        if value > 0:
            positive_words.append(key)
    return positive_words

def get_negative_words():
    pass