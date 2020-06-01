from src.sentiment_analyser_interface import performSentimentAnalysis
from nltk import sent_tokenize
import nltk
nltk.download('punkt', quiet=True)

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
    df['Mr1'] = df.apply(lambda row: {"capitalised": performSentimentAnalysis(row["ReviewTextUpper"]), "uncapitalised": performSentimentAnalysis(row["ReviewTextLower"])}, axis=1)

    # Remove columns that are not needed anymore
    del df["ReviewTextUpper"]
    del df["ReviewTextLower"]

def remove_positive_words(text, positive_words):
    sentences = sent_tokenize(text)
    result = ""
    for sentence in sentences:
        words = sentence.split(" ")

        result_words = [word for word in words if word.replace(".", "").replace(",", "").lower() not in positive_words]
        if result != "":
            result += " "
        result += ' '.join(result_words)
        if sentence.endswith(".") and not result.endswith("."):
            result += "."
    return result

def prepare_data_mr2(df):
    positive_words = get_positive_words()
    df["ReviewTextPositiveRemoved"] = df["ReviewText"].apply(lambda row: remove_positive_words(row, positive_words))

def run_sentiment_mr2(df):
    prepare_data_mr2(df)
    df['Mr2'] = df["ReviewTextPositiveRemoved"].apply(lambda row: performSentimentAnalysis(row))
    # Remove columns that are not needed anymore
    del df["ReviewTextPositiveRemoved"]

def remove_negative_words(text, negative_words):
    sentences = sent_tokenize(text)
    result = ""
    for sentence in sentences:
        words = sentence.split(" ")

        result_words = [word for word in words if word.replace(".", "").replace(",", "").replace(";", "").lower() not in negative_words]
        if result != "":
            result += " "
        result += ' '.join(result_words)
        if sentence.endswith(".") and not result.endswith("."):
            result += "."
    return result

def prepare_data_mr3(df):
    negative_words = get_negative_words()
    df["ReviewTextNegativeRemoved"] = df["ReviewText"].apply(lambda row: remove_negative_words(row, negative_words))

def run_sentiment_mr3(df):
    prepare_data_mr3(df)
    df['Mr3'] = df["ReviewTextNegativeRemoved"].apply(lambda row: performSentimentAnalysis(row))
    # Remove columns that are not needed anymore
    del df["ReviewTextNegativeRemoved"]

def run_sentiment_mr0(df):
    df["Mr0"] = df["ReviewText"].apply(lambda row: performSentimentAnalysis(row))

def run_tests(df):
    run_sentiment_mr0(df)
    run_sentiment_mr1(df)
    run_sentiment_mr2(df)
    run_sentiment_mr3(df)