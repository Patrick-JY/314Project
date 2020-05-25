from src.utils import join_base_path, load_vadersentiment_lexicon_data, get_positive_words, get_negative_words
import os

def test_join_base_path():
    assert os.path.exists(join_base_path(".314ProjectBaseDir")) == True
    assert os.path.exists(join_base_path(".314ProjectBaseDirs")) == False

def test_load_vadersentiment_lexicon_data():
    lexicon_data = load_vadersentiment_lexicon_data()
    assert lexicon_data is not None, "No lexicon data was loaded"
    assert type(lexicon_data) == dict, "Lexicon data should be a data dictionary"
    for key, value in lexicon_data.items():
        assert type(key) == str, "key should be a string"
        assert type(value) == float, "value should be a float"

def test_get_positive_words():
    lexicon_data = load_vadersentiment_lexicon_data()
    positive_words = get_positive_words()
    assert positive_words is not None, "Positive words list cannot be empty"
    for word in positive_words:
        assert lexicon_data[word] > 0, "Negative or neutral word found in positive words"

def test_get_negative_words():
    lexicon_data = load_vadersentiment_lexicon_data()
    negative_words = get_negative_words()
    assert negative_words is not None, "Negative words list cannot be empty"
    for word in negative_words:
        assert lexicon_data[word] < 0, "Positive or neutral word found in negative words"
