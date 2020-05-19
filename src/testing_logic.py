def capitalize_all_words(df):
    df['reviewTextUpper'] = df['reviewText'].str.upper()
