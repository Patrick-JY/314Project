def capitalise_all_words(df):
    df['ReviewTextUpper'] = df['ReviewText'].str.upper()

def uncapitalise_all_words(df):
    df['ReviewTextUpper'] = df['ReviewText'].str.lower()

def prepare_data_mr1(df):
    return df