import src.pulling_logic as pulling_logic
import pytest
import pandas
from pkg_resources import resource_filename


# Checks if github workflow is working by just doing a simple auto succeed test
def test_github():
    pass


# Checks the amazon data pulling from the amazon data sets
def test_amazon_pulling():
    df = pulling_logic.pulling_amazon(resource_filename("vadertester", "json/Amazon_githubdata.json.gz"))
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


@pytest.fixture(scope="session")
def amazon_data_frame():
    return pulling_logic.pulling_amazon(resource_filename("vadertester", "json/Amazon_githubdata.json.gz"))

def test_random_sample(amazon_data_frame):
    for n in range(1, len(amazon_data_frame), 100):
        df = amazon_data_frame.copy()
        sample1 = pulling_logic.random_sample(df, n)
        assert len(sample1) == n
        sample2 = pulling_logic.random_sample(df, n)
        assert len(sample2) == n
        try:
            pandas.testing.assert_series_equal(sample1, sample2)
        except AssertionError:
            pass
        else:
            AssertionError("sample1 and sample2 should be different")




    




