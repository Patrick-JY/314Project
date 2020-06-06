def calculate_test1(df):
    total_rows = len(df)
    total_positive = len(df[df["ReviewScore"].isin([4, 5])])
    total_negative = len(df[df["ReviewScore"].isin([1, 2])])
    total_neutral = len(df[df["ReviewScore"] == 3])
    overall_correct = 0
    positive_correct = 0
    negative_correct = 0
    neutral_correct = 0
    for i, row in df.iterrows():
        if row["Mr0"]["predicted_sentiment"] == "positive":
            if row["ReviewScore"] in [4, 5]:
                overall_correct += 1
                positive_correct += 1
        if row["Mr0"]["predicted_sentiment"] == "neutral":
            if row["ReviewScore"] == 3:
                overall_correct += 1
                neutral_correct += 1
        if row["Mr0"]["predicted_sentiment"] == "negative":
            if row["ReviewScore"] in [1, 2]:
                overall_correct += 1
                negative_correct += 1
    return {
        "overall_accuracy": 100 * overall_correct / total_rows,
        "positive_accuracy": 100 * positive_correct / total_positive,
        "negative_accuracy": 100 * negative_correct / total_negative,
        "neutral_accuracy": 100 * neutral_correct / total_neutral}

def calculate_test2(df):
    total_rows = len(df)
    rows_passed = 0
    for row in df["Mr1"]:
        if row["capitalised"]["compound"] == row["uncapitalised"]["compound"]:
            rows_passed += 1
    return 100 * rows_passed / total_rows

def calculate_test3(df):
    total_rows = len(df)
    rows_passed = 0
    for i, row in df.iterrows():
        if row["Mr2"]["compound"] <= row["Mr0"]["compound"]:
            rows_passed += 1
    return 100 * rows_passed / total_rows

def calculate_test4(df):
    total_rows = len(df)
    rows_passed = 0
    for i, row in df.iterrows():
        if row["Mr3"]["compound"] >= row["Mr0"]["compound"]:
            rows_passed += 1
    return 100 * rows_passed / total_rows

def calculate_test5(df):
    threshold = 0.25
    total_rows = len(df)
    rows_passed = 0
    for i, row in df.iterrows():
        if abs(row["Mr0"]["compound"] - row["Mr4"]["compound"]) <= threshold:
            rows_passed += 1
    return 100 * rows_passed / total_rows
