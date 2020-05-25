import pandas as pd


def report_generation(df):
    # Create new data from input argument
    df = pd.DataFrame()

    # Create new headers for analysis of data
    df.columns = ['Correctness(%)', 'Positive/Negative', 'Number of Reviews', 'Score Ratio']

    # Test print
    print(df.head(10))
