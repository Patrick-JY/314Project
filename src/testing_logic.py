from src.sentiment_analyser_interface import performSentimentAnalysis

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
    pass