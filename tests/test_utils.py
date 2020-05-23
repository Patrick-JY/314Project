from src.utils import join_base_path
import os

def test_join_base_path():
    assert os.path.exists(join_base_path(".314ProjectBaseDir")) == True