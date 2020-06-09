import pytest
import json
import pandas as pd
from src.testing_logic import run_tests, run_sentiment_mr0, run_sentiment_mr4, replace_with_synonyms, capitalise_all_words, uncapitalise_all_words, prepare_data_mr1, run_sentiment_mr1, run_sentiment_mr2, remove_positive_words, prepare_data_mr2, remove_negative_words, prepare_data_mr3, run_sentiment_mr3
from src.pulling_logic import pulling_amazon
from src.utils import get_positive_words, get_negative_words
from pkg_resources import resource_filename

@pytest.fixture(scope="session")
def amazon_data_frame():
    return pulling_amazon(resource_filename("vadertester", "json/Amazon_githubdata.json.gz"))

def test_capitalise_all_words(amazon_data_frame):
    # get a copy of the dataframe so that it is unaffected by other tests
    df = amazon_data_frame.copy()
    
    capitalise_all_words(df)
    capitalised_words = df[~df.ReviewTextUpper.str.isupper()]
    assert capitalised_words.empty, "Word capitalisation failed, {0} word(s) were not capitalised ".format(len(capitalised_words))

def test_uncapitalise_all_words(amazon_data_frame):
    # get a copy of the dataframe so that it is unaffected by other tests
    df = amazon_data_frame.copy()

    uncapitalise_all_words(df)
    uncapitalised_words = df[~df.ReviewTextLower.str.islower()]
    assert uncapitalised_words.empty, "Word uncapitalisation failed, {0} word(s) were capitalised ".format(len(uncapitalised_words))

def test_prepare_data_mr1(amazon_data_frame):
    """Mr1 -> capitalise vs uncapitalise all words"""
    # get a copy of the dataframe so that it is unaffected by other tests
    df = amazon_data_frame.copy()

    prepare_data_mr1(df)
    capitalised_words = df[~df.ReviewTextUpper.str.isupper()]
    assert capitalised_words.empty, "Word capitalisation failed, {0} word(s) were not capitalised ".format(len(capitalised_words))
    uncapitalised_words = df[~df.ReviewTextLower.str.islower()]
    assert uncapitalised_words.empty, "Word uncapitalisation failed, {0} word(s) were capitalised ".format(len(uncapitalised_words))

def test_run_sentiment_mr1(amazon_data_frame):
    # get a copy of the dataframe so that it is unaffected by other tests
    df = amazon_data_frame.copy()

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

def test_remove_positive_words():
    text = "You are bad and good. I love you. You are terrific and I like the cut of your jib."
    positive_words = get_positive_words()
    text_positive_removed = remove_positive_words(text, positive_words)
    assert text_positive_removed == "You are bad and. I you. You are and I the cut of your jib."


def test_prepare_data_mr2(amazon_data_frame):
    # get a copy of the dataframe so that it is unaffected by other tests
    df = amazon_data_frame.copy()
    positive_words = get_positive_words()
    prepare_data_mr2(df)
    assert not df["ReviewText"].equals(df["ReviewTextPositiveRemoved"])
    for w in positive_words:
        assert df[df["ReviewTextPositiveRemoved"].str.lower().str.contains(' ' + w.lower() + ' ', regex=False)].empty
        assert df[df["ReviewTextPositiveRemoved"].str.lower().str.contains(' ' + w.lower() + '; ', regex=False)].empty
        assert df[df["ReviewTextPositiveRemoved"].str.lower().str.contains(' ' + w.lower() + '. ', regex=False)].empty
        assert df[df["ReviewTextPositiveRemoved"].str.lower().str.contains(' ' + w.lower() + ', ', regex=False)].empty

def test_run_sentiment_mr2(amazon_data_frame):
    # get a copy of the dataframe so that it is unaffected by other tests
    df = amazon_data_frame.copy()

    run_sentiment_mr2(df)
    for row in df["Mr2"]:
        assert type(row) == dict
        assert "text" in row, "text key missing from row"
        assert "predicted_sentiment" in row, "predicted_sentiment key missing from row"
        assert "pos" in row, "pos key missing from row"
        assert "neg" in row, "neg key missing from row"
        assert "neu" in row, "neu key missing from row"
        assert "compound" in row, "compound key missing from row dictionary"

def test_remove_negative_words():
    text = "You are bad and good. I love you. You are terrific and I like the cut of your jib."
    negative_words = get_negative_words()
    text_positive_removed = remove_negative_words(text, negative_words)
    assert text_positive_removed == "You are and good. I love you. You are terrific and I like the of your jib."

def test_prepare_data_mr3(amazon_data_frame):
    # get a copy of the dataframe so that it is unaffected by other tests
    df = amazon_data_frame.copy()
    negative_words = get_negative_words()
    prepare_data_mr3(df)
    assert not df["ReviewText"].equals(df["ReviewTextNegativeRemoved"])
    for w in negative_words:
        assert df[df["ReviewTextNegativeRemoved"].str.lower().str.contains(' ' + w.lower() + ' ', regex=False)].empty
        assert df[df["ReviewTextNegativeRemoved"].str.lower().str.contains(' ' + w.lower() + '; ', regex=False)].empty
        assert df[df["ReviewTextNegativeRemoved"].str.lower().str.contains(' ' + w.lower() + '. ', regex=False)].empty
        assert df[df["ReviewTextNegativeRemoved"].str.lower().str.contains(' ' + w.lower() + ', ', regex=False)].empty


def test_run_sentiment_mr3(amazon_data_frame):
    # get a copy of the dataframe so that it is unaffected by other tests
    df = amazon_data_frame.copy()

    run_sentiment_mr3(df)
    for row in df["Mr3"]:
        assert type(row) == dict
        assert "text" in row, "text key missing from row"
        assert "predicted_sentiment" in row, "predicted_sentiment key missing from row"
        assert "pos" in row, "pos key missing from row"
        assert "neg" in row, "neg key missing from row"
        assert "neu" in row, "neu key missing from row"
        assert "compound" in row, "compound key missing from row dictionary"

# Tests the synonym_replacement function
def test_synonym_replacement(amazon_data_frame):
    old_df = amazon_data_frame
    replaced_df = amazon_data_frame.copy()
    replace_with_synonyms(replaced_df)
    assert 'SynonymReplaced' in replaced_df.columns
    try:
        pd.testing.assert_series_equal(replaced_df['SynonymReplaced'], replaced_df['ReviewText'], True, "equiv",
                                           True, False, False)
    except AssertionError:
        pass
    else:
        raise AssertionError
    pd.testing.assert_series_equal(replaced_df['ReviewText'], old_df['ReviewText'])


def test_run_sentiment_mr4(amazon_data_frame):
    # get a copy of the dataframe so that it is unaffected by other tests
    df = amazon_data_frame.copy()

    run_sentiment_mr4(df)
    for row in df["Mr4"]:
        assert type(row) == dict
        assert "text" in row, "text key missing from row"
        assert "predicted_sentiment" in row, "predicted_sentiment key missing from row"
        assert "pos" in row, "pos key missing from row"
        assert "neg" in row, "neg key missing from row"
        assert "neu" in row, "neu key missing from row"
        assert "compound" in row, "compound key missing from row dictionary"

def test_run_sentiment_mr0(amazon_data_frame):
    # get a copy of the dataframe so that it is unaffected by other tests
    df = amazon_data_frame.copy()

    run_sentiment_mr0(df)

    for row in df["Mr0"]:
        assert type(row) == dict
        assert "text" in row, "text key missing from row"
        assert "predicted_sentiment" in row, "predicted_sentiment key missing from row"
        assert "pos" in row, "pos key missing from row"
        assert "neg" in row, "neg key missing from row"
        assert "neu" in row, "neu key missing from row"
        assert "compound" in row, "compound key missing from row dictionary"

def test_run_tests(amazon_data_frame):
    # get a copy of the dataframe so that it is unaffected by other tests
    df = amazon_data_frame.copy()

    run_tests(df)

    assert "Mr0" in df, "Mr0 missing from dataframe"
    assert "Mr1" in df, "Mr1 missing from dataframe"
    assert "Mr2" in df, "Mr2 missing from dataframe"
    assert "Mr3" in df, "Mr3 missing from dataframe"
    assert "Mr4" in df, "Mr4 missing from dataframe"