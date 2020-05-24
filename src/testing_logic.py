from src.sentiment_analyser_interface import performSentimentAnalysis
from nltk import sent_tokenize

def capitalise_all_words(df):
    df['ReviewTextUpper'] = df['ReviewText'].str.upper()

def uncapitalise_all_words(df):
    df['ReviewTextLower'] = df['ReviewText'].str.lower()

def prepare_data_mr1(df):
    """MR1 -> capitalise vs uncapitalise all words"""
    capitalise_all_words(df)
    uncapitalise_all_words(df)
    return df

def run_sentiment_mr1(df):
    prepare_data_mr1(df)
    df['Mr1'] = df.apply(lambda row: {"capitalised": performSentimentAnalysis(row["ReviewTextUpper"]), "uncapitalised": performSentimentAnalysis(row["ReviewTextLower"])}, axis=1)
    # Remove columns that are not needed anymore
    del df["ReviewTextUpper"]
    del df["ReviewTextLower"]
    return df

def remove_positive_words(text, positive_words):
    sentences = sent_tokenize(text)
    result = ""
    for sentence in sentences:
        words = sentence.split(" ")

        result_words = [word for word in words if word.replace(".", "").lower() not in positive_words]
        if result != "":
            result += " "
        result += ' '.join(result_words)
        if sentence.endswith(".") and not result.endswith("."):
            result += "."
    return result

def prepare_data_mr2(df):
    pass