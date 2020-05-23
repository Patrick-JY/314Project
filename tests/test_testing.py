import pytest
import json
import pandas as pd
from src.testing_logic import capitalise_all_words, uncapitalise_all_words
from src.pulling_logic import pulling_amazon

@pytest.fixture
def df():
    return pulling_amazon("Amazon_githubdata.json.gz")

def test_capitalise_all_words(df):
    capitalise_all_words(df)
    capitalised_words = df[~df.ReviewTextUpper.str.isupper()]
    assert capitalised_words.empty, "Word capitalisation failed, {0} word(s) were not capitalised ".format(len(capitalised_words))

def test_uncapitalise_all_words(df):
    uncapitalise_all_words(df)
    uncapitalised_words = df[~df.ReviewTextUpper.str.islower()]
    assert uncapitalised_words.empty, "Word uncapitalisation failed, {0} word(s) were capitalised ".format(len(uncapitalised_words))
