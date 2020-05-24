import pytest
import json
import pandas as pd
from src.testing_logic import capitalise_all_words, uncapitalise_all_words, prepare_data_mr1, run_sentiment_mr1
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
    """Mr1 -> capitalise vs uncapitalise all words"""
    prepare_data_mr1(df)
    capitalised_words = df[~df.ReviewTextUpper.str.isupper()]
    assert capitalised_words.empty, "Word capitalisation failed, {0} word(s) were not capitalised ".format(len(capitalised_words))
    uncapitalised_words = df[~df.ReviewTextLower.str.islower()]
    assert uncapitalised_words.empty, "Word uncapitalisation failed, {0} word(s) were capitalised ".format(len(uncapitalised_words))

def test_run_sentiment_mr1(df):
    run_sentiment_mr1(df)

    for row in df["Mr1"]:
        assert type(row) == dict
        assert "capitalised" in row
        assert "text" in row["capitalised"], "text key missing from row[\"capitalised\"]"
        assert "predicted_sentiment" in row["capitalised"], "predicted_sentiment key missing from row[\"capitalised\"]"
        assert "pos" in row["capitalised"], "pos key missing from row[\"capitalised\"]"
        assert "neg" in row["capitalised"], "neg key missing from row[\"capitalised\"]"
        assert "neu" in row["capitalised"], "neu key missing from row[\"capitalised\"]"
        assert "compound" in row["capitalised"], "compound key missing from row[\"capitalised\"] dictionary"
    
        assert "uncapitalised" in row
        assert "text" in row["uncapitalised"], "text key missing from row[\"uncapitalised\"]"
        assert "predicted_sentiment" in row["uncapitalised"], "predicted_sentiment key missing from row[\"uncapitalised\"]"
        assert "pos" in row["uncapitalised"], "pos key missing from row[\"uncapitalised\"]"
        assert "neg" in row["uncapitalised"], "neg key missing from row[\"uncapitalised\"]"
        assert "neu" in row["uncapitalised"], "neu key missing from row[\"uncapitalised\"]"
        assert "compound" in row["uncapitalised"], "compound key missing from row[\"uncapitalised\"] dictionary"
