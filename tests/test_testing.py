import pytest
import json
import pandas as pd
from src.testing_logic import capitalise_all_words, uncapitalise_all_words

@pytest.fixture
def df():
    # replace with pulling amazon data
    dataframe = pd.read_json("../json/githubdata.json", orient="records", lines=True)
    return dataframe[["reviewerID","reviewText", "overall"]]

def test_capitalise_all_words(df):
    capitalise_all_words(df)
    capitalised_words = df[~df.reviewTextUpper.str.isupper()]
    assert capitalised_words.empty, "Word capitalisation failed, {0} word(s) were not capitalised ".format(len(capitalised_words))

def test_uncapitalise_all_words(df):
    uncapitalise_all_words(df)
    uncapitalise_words = df[~df.reviewTextUpper.str.islower()]
    assert uncapitalise_words.empty, "Word uncapitalisation failed, {0} word(s) were capitalised ".format(len(uncapitalised_words))
