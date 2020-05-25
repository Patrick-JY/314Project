import src.pulling_logic as pulling_logic
import pytest
import pandas


# Checks if github workflow is working by just doing a simple auto succeed test
def test_github():
    pass


# Checks the amazon data pulling from the amazon data sets
def test_amazon_pulling():
    df = pulling_logic.pulling_amazon("Amazon_githubdata.json.gz")
    errors = []
    github_line_amount = 37
    # First checks if the data is being put into a form properly
    if not len(df.columns) == 3:
        errors.append("incorrect column amount")

    # This error needs to be asserted because the key is used later on in the test
    assert df.columns[0] == "ID", "ID incorrectly labeled"

    if not df.columns[1] == "ReviewText":
        errors.append("ReviewText Column incorrectly labeled")

    # This error needs to be asserted because the key is used later on in the test
    assert df.columns[2] == "ReviewScore", "ReviewScore Column incorrectly labeled"

    # Checks if the IDs are Unique (test may take a long time on large data)
    if not df['ID'].is_unique:
        errors.append("ID column values are not unique")

    # Check if ReviewScore is all numeric
    if not df['ReviewScore'].dtype == "float64":
        errors.append("Rating column not numeric")

    # Checks if all lines from github data imported (github data contains 37 lines)
    if not len(df.index) == github_line_amount:
        errors.append("Not All data is imported correctly")

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


@pytest.fixture
def amazon_data_frame():
    return pulling_logic.pulling_amazon("Amazon_githubdata.json.gz")


# Tests the synonym_replacement function
def test_synonym_replacement(amazon_data_frame):
    old_df = amazon_data_frame
    replaced_df = pulling_logic.replace_with_synonyms(amazon_data_frame.copy())
    assert 'SynonymReplaced' in replaced_df.columns
    try:
        pandas.testing.assert_series_equal(replaced_df['SynonymReplaced'], replaced_df['ReviewText'], True, "equiv",
                                           True, False, False)
    except AssertionError:
        pass
    else:
        raise AssertionError
    pandas.testing.assert_series_equal(replaced_df['ReviewText'], old_df['ReviewText'])





    




