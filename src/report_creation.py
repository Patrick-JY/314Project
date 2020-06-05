import pandas as pd


def report_generation(df):
    # Create new data from input argument
    df = pd.DataFrame()

    # Create new headers for analysis of data
    df.columns = ['Correctness(%)', 'Positive/Negative', 'Number of Reviews', 'Score Ratio']

    # Test print
    print(df.head(10))


#Gonna make the graph in this file if you encounter a conflict just keep both peoples work
def column_graph_word_length(df):
    pass


def prepare_word_length(df):
    pass
