import pytest
import pandas as pd
from src.pulling_logic import pulling_amazon
import src.report_creation as report_creation
import src.testing_logic as testing_logic
import matplotlib.pyplot as plt


@pytest.fixture(scope="session")
def tested_data_frame():
    df = pulling_amazon("Amazon_githubdata.json.gz")
    testing_logic.run_tests(df)
    return df


def test_report_generation():
    df = pd.DataFrame
    assert df is not df.empty
    #print(df.head(5))


def test_column_graph_word_length(tested_data_frame):
    num_figs_before = plt.gcf().number
    df = tested_data_frame.copy()
    num_figs_after = plt.gcf().number
    assert num_figs_before < num_figs_after


def test_prepare_word_length(tested_data_frame):
    df = tested_data_frame.copy()
    report_creation.prepare_word_length(df)
    assert []



