import src.pulling_logic as pulling_logic


# Checks if github workflow is working by just doing a simple auto succeed test
def test_github():
    pass


# Checks the amazon data pulling from the amazon data sets
def test_amazon_pulling():
    df = pulling_logic.pulling_amazon("Amazon_githubdata.json.gz")

    # First checks if the data is being put into a form properly
    assert len(df.columns) == 3
    assert df.columns[0] == "ID"
    assert df.columns[1] == "ReviewText"
    assert df.columns[2] == "ReviewScore"

    # Checks if the IDs are Unique (test may take a long time on large data)
    assert df['ID'].value_counts().is_unique

    # Check if ReviewScore is all numeric
    assert df['overall'].dtype == "float64"




