from src.testing_logic import run_tests
from src.pulling_logic import pulling_amazon, random_sample
from src.analyse_results import calculate_test1, calculate_test5
import pytest

#update this test
@pytest.fixture(scope="session")
def amazon_data_frame_tested():
    df = pulling_amazon("Amazon_githubdata.json.gz")
    df = random_sample(df, 30)
    run_tests(df)
    return df

def test_calculate_test1(amazon_data_frame_tested):
    calculate_test1(amazon_data_frame_tested)
    #write test here then code
    raise

def test_calculate_test5(amazon_data_frame_tested):
    result = calculate_test5(amazon_data_frame_tested)
    assert result and type(result) == float

