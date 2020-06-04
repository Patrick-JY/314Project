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

def test_calculate_test1(df):
    results = calculate_test1(df)
    assert "positive_accuracy" in results
    assert "neutral_accuracy" in results
    assert "negative_accuracy" in results
    assert "overall_accuracy" in results
    # check it is an float etc.
    
    #write test here then code
    raise

