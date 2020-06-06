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
    output_df = report_creation.prepare_word_length(df)

    # Pre Defined Values for the github dataset
    cat1 = 24
    cat2 = 6
    cat3 = 3
    cat4 = 1
    cat5 = 3

    assert 'Mr0' in output_df
    assert 'Mr1' in output_df
    assert 'Mr2' in output_df
    assert 'Mr3' in output_df
    assert 'Mr4' in output_df
    assert 'cat' in output_df
    assert 'avgComp' in output_df

    assert len(output_df(output_df['cat'] == 'cat1')) == cat1*5
    assert len(output_df(output_df['cat'] == 'cat2')) == cat2*5
    assert len(output_df(output_df['cat'] == 'cat3')) == cat3*5
    assert len(output_df(output_df['cat'] == 'cat4')) == cat4*5
    assert len(output_df(output_df['cat'] == 'cat5')) == cat5*5






