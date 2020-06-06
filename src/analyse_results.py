def calculate_test1(df):
    pass

def calculate_test3(df):
    pass

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
