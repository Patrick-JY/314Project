# logic for the pulling of data
import pandas as pd
import gzip
from src.utils import join_base_path, get_negative_words, get_positive_words
from nltk.corpus import wordnet as wn
from nltk import sent_tokenize
import nltk
nltk.download("punkt", quiet=True)
nltk.download("wordnet", quiet=True)
import random
# code for data prep is modified from the sample given in http://jmcauley.ucsd.edu/data/amazon/


def amazon_parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)


def amazon_get_df(path):
    i = 0
    df = {}
    for d in amazon_parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')


def pulling_amazon(dataset):
    df = prepare_amazon(amazon_get_df(join_base_path("json/"+dataset)))
    return df


def prepare_amazon(data_frame):
    df = pd.concat([data_frame['reviewerID'] + data_frame['unixReviewTime'].astype('str'), data_frame['reviewText']
                       , data_frame['overall']], axis=1, keys=['ID', 'ReviewText', 'ReviewScore'])
    return df

def replace_with_synonyms(data_frame):
    positive_words = get_positive_words()
    negative_words = get_negative_words()
    word_list = positive_words + negative_words
    data_frame['SynonymReplaced'] = data_frame['ReviewText'].apply(lambda row: synonym_replacer(row, word_list))

    return data_frame


def synonym_replacer(text, word_list):
    sentences = sent_tokenize(text)
    result = ""
    for sentence in sentences:
        result_words = []
        words = sentence.split(" ")
        for word in words:
            word_stripped_lower = word.replace(".", "").replace(",", "").replace(";", "").lower()
            if word in word_list:
                synonyms = []
                for syn in wn.synsets(word_stripped_lower):
                    for l in syn.lemmas():
                        # Skip words that are not in word_list as VaderSentiment can't evaluate these
                        # Skip words with _ as these can't be parsed either by VaderSentiment
                        # Skip words that are equal to the original word or are plurals etc. (Need to work on this to exclude all)
                        # https://stackoverflow.com/questions/14489309/convert-words-between-verb-noun-adjective-forms
                        # https://stackoverflow.com/questions/32411594/identify-the-word-as-a-noun-verb-or-adjective
                        if l.name() not in word_list or l.name().lower() in word_stripped_lower or "_" in l.name():
                            continue
                        synonyms.append((l.name()))
                if synonyms:
                    # fix adding punctuation at end of word
                    add_end_letter = ""
                    if word.endswith(","):
                        add_end_letter = ","
                    if word.endswith(";"):
                        add_end_letter = ";"
                    word = random.choice(synonyms) + add_end_letter
            result_words.append(word)
        if result != "":
            result += " "
        result += ' '.join(result_words)
        if sentence.endswith(".") and not result.endswith("."):
            result += "."
    return result

def random_sample(df, n):
    sample = df.sample(n)
    sample.reset_index(inplace = True, drop=True)
    return sample
