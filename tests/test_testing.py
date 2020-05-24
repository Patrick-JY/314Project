import pytest
import json
import pandas as pd
from src.testing_logic import capitalise_all_words, uncapitalise_all_words, prepare_data_mr1, run_mr1
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
    uncapitalised_words = df[~df.ReviewTextLower.str.islower()]
    assert uncapitalised_words.empty, "Word uncapitalisation failed, {0} word(s) were capitalised ".format(len(uncapitalised_words))

def test_prepare_data_mr1(df):
    """MR1 -> capitalise vs uncapitalise all words"""
    prepare_data_mr1(df)
    capitalised_words = df[~df.ReviewTextUpper.str.isupper()]
    assert capitalised_words.empty, "Word capitalisation failed, {0} word(s) were not capitalised ".format(len(capitalised_words))
    uncapitalised_words = df[~df.ReviewTextLower.str.islower()]
    assert uncapitalised_words.empty, "Word uncapitalisation failed, {0} word(s) were capitalised ".format(len(uncapitalised_words))

def test_run_mr1(df):
    assert df.mr1
    assert type(df.mr1[0]) == dict
    assert "capitalised" in df.mr1[0]
    assert "text" in df.mr1[0]["capitalised"], "text key missing from df.mr1[0][\"capitalised\"]"
    assert "predicted_sentiment" in df.mr1[0]["capitalised"], "predicted_sentiment key missing from df.mr1[0][\"capitalised\"]"
    assert "pos" in df.mr1[0]["capitalised"], "pos key missing from df.mr1[0][\"capitalised\"]"
    assert "neg" in df.mr1[0]["capitalised"], "neg key missing from df.mr1[0][\"capitalised\"]"
    assert "neu" in df.mr1[0]["capitalised"], "neu key missing from df.mr1[0][\"capitalised\"]"
    assert "compound" in df.mr1[0]["capitalised"], "compound key missing from df.mr1[0][\"capitalised\"] dictionary"

    assert "uncapitalised" in df.mr1[0]
    assert "text" in df.mr1[0]["uncapitalised"], "text key missing from df.mr1[0][\"uncapitalised\"]"
    assert "predicted_sentiment" in df.mr1[0]["uncapitalised"], "predicted_sentiment key missing from df.mr1[0][\"uncapitalised\"]"
    assert "pos" in df.mr1[0]["uncapitalised"], "pos key missing from df.mr1[0][\"uncapitalised\"]"
    assert "neg" in df.mr1[0]["uncapitalised"], "neg key missing from df.mr1[0][\"uncapitalised\"]"
    assert "neu" in df.mr1[0]["uncapitalised"], "neu key missing from df.mr1[0][\"uncapitalised\"]"
    assert "compound" in df.mr1[0]["uncapitalised"], "compound key missing from df.mr1[0][\"uncapitalised\"] dictionary"
