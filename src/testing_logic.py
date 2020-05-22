def capitalise_all_words(df):
    df['reviewTextUpper'] = df['reviewText'].str.upper()

def uncapitalise_all_words(df):
    df['reviewTextUpper'] = df['reviewText'].str.lower()

