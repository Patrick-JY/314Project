import pytest
from src.pulling_logic import pulling_amazon
import src.report_creation as report_creation
import src.testing_logic as testing_logic
import matplotlib.pyplot as plt
from pkg_resources import resource_filename
import os

@pytest.fixture(scope="session")
def tested_data_frame():
    df = pulling_amazon(resource_filename("vadertester", "json/Amazon_githubdata.json.gz"))
    testing_logic.run_tests(df)
    return df

def test_report_generation(tmpdir, tested_data_frame, capsys):
    os.chdir(tmpdir)
    report_creation.report_generation(tested_data_frame.copy())
    captured = capsys.readouterr()
    assert captured.out.startswith("Tests Running \n Test 1: Accuracy of the Un-Modified DataSet")
    assert "Overall Accuracy: " in captured.out
    assert "Positive Accuracy:" in captured.out
    assert "Negative Accuracy" in captured.out
    assert "Neutral Accuracy" in captured.out
    assert "Test 2: " in captured.out
    assert "Test 3: " in captured.out
    assert "Test 4: " in captured.out
    assert "Test 5: " in captured.out
    assert "Outputting Graphs:" in captured.out
    assert "Column Graph grouped by Word length" in captured.out
    assert os.path.exists(os.path.join(tmpdir, "column_graph.png"))
    assert os.path.exists(os.path.join(tmpdir, "summary_table.png"))




def test_column_graph_word_length(tmpdir, tested_data_frame):
    os.chdir(tmpdir)
    num_figs_before = plt.gcf().number
    df = tested_data_frame.copy()
    report_creation.column_graph_word_length(df)
    num_figs_after = plt.gcf().number
    assert num_figs_before <= num_figs_after
    assert os.path.exists(os.path.join(tmpdir, "column_graph.png"))


def test_prepare_word_length(tested_data_frame):
    df = tested_data_frame.copy()
    output_df = report_creation.improved_calculation(df)

    # Pre Defined Values for the github dataset
    cat1 = 24
    cat2 = 6
    cat3 = 3
    cat4 = 1
    cat5 = 3
    # This test currently feels bare bones tbh
    assert 'Mr#' in output_df
    assert 'cat1' in output_df
    assert 'cat2' in output_df
    assert 'cat3' in output_df
    assert 'cat4' in output_df
    assert 'cat5' in output_df

def test_summary_table(tmpdir, tested_data_frame):
    os.chdir(tmpdir)
    num_figs_before = plt.gcf().number
    df = tested_data_frame.copy()
    test_pass = [False, True, False, True, False]
    report_creation.summary_table(test_pass)
    num_figs_after = plt.gcf().number
    assert num_figs_before <= num_figs_after
    assert os.path.exists(os.path.join(tmpdir, "summary_table.png"))





