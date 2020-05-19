import pytest
import json
import pandas as pd
from src.testing_logic import capitalize_all_words

@pytest.fixture
def df():
    # replace with pulling amazon data
    dataframe = pd.read_json("../json/githubdata.json", orient="records", lines=True)
    return dataframe[["reviewerID","reviewText", "overall"]]

def test_capitalize_all_words(df):
    capitalize_all_words(df)
    assert df[~df.reviewTextUpper.str.isupper()].empty
