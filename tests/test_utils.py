from src.utils import join_base_path, load_vadersentiment_lexicon_data
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