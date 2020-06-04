from src.testing_logic import run_tests
from src.pulling_logic import pulling_amazon, random_sample
from src.analyse_results import calculate_test1
import pytest

#update this test
@pytest.fixture(scope="session")
def amazon_data_frame_tested():
    df = pulling_amazon("Amazon_githubdata.json.gz")
    df = random_sample(df, 30)
    run_tests(df)
    return df

def test_calculate_test1():
    #write test here then code
    raise

