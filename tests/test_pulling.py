import src.pulling_logic as pulling_logic


# Checks if github workflow is working by just doing a simple auto succeed test
def test_github():
    pass


# Checks the amazon data pulling from the amazon data sets
def test_amazon_pulling():
    df = pulling_logic.prepare_amazon("Amazon_githubdata.json.gz")
    errors = []

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

    assert not errors, "errors occured:\n{}".format("\n".join(errors))



