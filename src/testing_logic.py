def capitalise_all_words(df):
    df['ReviewTextUpper'] = df['ReviewText'].str.upper()

def uncapitalise_all_words(df):
    df['ReviewTextLower'] = df['ReviewText'].str.lower()

def prepare_data_mr1(df):
    """MR1 -> capitalise vs uncapitalise all words"""
    capitalise_all_words(df)
    uncapitalise_all_words(df)
    return df