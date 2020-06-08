from src.sentiment_analyser_interface import performSentimentAnalysis
from nltk.corpus import wordnet as wn
from nltk import sent_tokenize
from nltk.tokenize import TweetTokenizer
import nltk
from tqdm import tqdm
nltk.download("punkt", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
import random
import string
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from src.utils import get_positive_words, get_negative_words

def capitalise_all_words(df):
    df['ReviewTextUpper'] = df['ReviewText'].str.upper()

def uncapitalise_all_words(df):
    df['ReviewTextLower'] = df['ReviewText'].str.lower()

def prepare_data_mr1(df):
    """MR1 -> capitalise vs uncapitalise all words"""
    capitalise_all_words(df)
    uncapitalise_all_words(df)

def run_sentiment_mr1(df):
    prepare_data_mr1(df)
    tqdm.pandas(desc="Mr1 Sentiment")
    df['Mr1'] = df.progress_apply(lambda row: {"capitalised": performSentimentAnalysis(row["ReviewTextUpper"]), "uncapitalised": performSentimentAnalysis(row["ReviewTextLower"])}, axis=1)

    # Remove columns that are not needed anymore
    del df["ReviewTextUpper"]
    del df["ReviewTextLower"]

def remove_positive_words(text, positive_words):
    sentences = sent_tokenize(text)
    result = ""
    for sentence in sentences:
        words = sentence.split(" ")

        result_words = [word for word in words if word.strip(string.punctuation).lower() not in positive_words]
        if result != "":
            result += " "
        result += ' '.join(result_words)
        if sentence.endswith(".") and not result.endswith("."):
            result += "."
    return result

def prepare_data_mr2(df):
    positive_words = get_positive_words()
    tqdm.pandas(desc="Mr2 Preparation")
    df["ReviewTextPositiveRemoved"] = df["ReviewText"].progress_apply(lambda row: remove_positive_words(row, positive_words))

def run_sentiment_mr2(df):
    prepare_data_mr2(df)
    tqdm.pandas(desc="Mr2 Sentiment")
    df['Mr2'] = df["ReviewTextPositiveRemoved"].progress_apply(lambda row: performSentimentAnalysis(row))
    # Remove columns that are not needed anymore
    del df["ReviewTextPositiveRemoved"]

def remove_negative_words(text, negative_words):
    sentences = sent_tokenize(text)
    result = ""
    for sentence in sentences:
        words = sentence.split(" ")

        result_words = [word for word in words if word.strip(string.punctuation).lower() not in negative_words]
        if result != "":
            result += " "
        result += ' '.join(result_words)
        if sentence.endswith(".") and not result.endswith("."):
            result += "."
    return result

def prepare_data_mr3(df):
    negative_words = get_negative_words()
    tqdm.pandas(desc="Mr3 Preparation")
    df["ReviewTextNegativeRemoved"] = df["ReviewText"].progress_apply(lambda row: remove_negative_words(row, negative_words))

def run_sentiment_mr3(df):
    prepare_data_mr3(df)
    tqdm.pandas(desc="Mr3 Sentiment")
    df['Mr3'] = df["ReviewTextNegativeRemoved"].progress_apply(lambda row: performSentimentAnalysis(row))
    # Remove columns that are not needed anymore
    del df["ReviewTextNegativeRemoved"]


def replace_with_synonyms(data_frame):
    positive_words = get_positive_words()
    negative_words = get_negative_words()
    word_list = positive_words + negative_words
    tqdm.pandas(desc="Mr4 Preparation")
    data_frame['SynonymReplaced'] = data_frame['ReviewText'].progress_apply(lambda row: synonym_replacer(row, word_list))


# Code for this function thanks to https://stackoverflow.com/questions/15586721/wordnet-lemmatization-and-pos-tagging-in-python
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return wn.NOUN  # Noun is probably the safest default tbh



def synonym_replacer(text, word_list):
    sentences = sent_tokenize(text)
    tokenizer = TweetTokenizer()
    result = ""
    for sentence in sentences:
        result_words = []
        pos_tag = nltk.pos_tag(tokenizer.tokenize(sentence))

        words = pos_tag
        for tuple_word in words:
            word = list(tuple_word)
            word_stripped_lower = word.copy()  # Setting it equal so all the second elements are the same

            word_stripped_lower[0] = word[0].lower()
            if word[0] in word_list:
                synonyms = []
                for syn in wn.synsets(word_stripped_lower[0], get_wordnet_pos(word_stripped_lower[1])):
                    for l in syn.lemmas():

                        # Skip words that are not in word_list as VaderSentiment can't evaluate these
                        # Skip words with _ as these can't be parsed either by VaderSentiment
                        # Skip words that are equal to the original word or are plurals etc. (Need to work on this to exclude all)
                        if l.name() not in word_list or l.name().lower() in word_stripped_lower[0] or "_" in l.name():
                            continue
                        synonyms.append((l.name()))
                if synonyms:
                    # fix adding punctuation at end of word
                    word[0] = random.choice(synonyms)
            result_words.append(word[0])
        for i, w in enumerate(result_words):
            if i < len(result_words) - 1:
                if w not in string.punctuation and result_words[i + 1] not in ['.', ',', '"', ")", "(", "'", '!', ':', ';']:
                    result += w + " "
                else:
                    if w in [".", ",", '!', ':', ';']:
                        result += w + " "
                    else:
                        result += w
            else:
                result += w + " "
    return result

def run_sentiment_mr4(df):
    replace_with_synonyms(df)
    tqdm.pandas(desc="Mr4 Sentiment")
    df['Mr4'] = df["SynonymReplaced"].progress_apply(lambda row: performSentimentAnalysis(row))
    # Remove columns that are not needed anymore
    del df["SynonymReplaced"]

def run_sentiment_mr0(df):
    tqdm.pandas(desc="Mr0 Sentiment")
    df["Mr0"] = df["ReviewText"].progress_apply(lambda row: performSentimentAnalysis(row))

def run_tests(df):
    run_sentiment_mr0(df)
    run_sentiment_mr1(df)
    run_sentiment_mr2(df)
    run_sentiment_mr3(df)
    run_sentiment_mr4(df)