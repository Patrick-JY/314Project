from src.testing_logic import run_tests
from src.pulling_logic import pulling_amazon, random_sample
from src.analyse_results import calculate_test1, calculate_test5, calculate_test4, calculate_test3
import pytest

#update this test
@pytest.fixture(scope="session")
def amazon_data_frame_tested():
    df = pulling_amazon("Amazon_githubdata.json.gz")
    df = random_sample(df, 30)
    run_tests(df)
    return df

def test_calculate_test1(amazon_data_frame_tested):
    results = calculate_test1(amazon_data_frame_tested)
    assert "positive_accuracy" in results
    assert "neutral_accuracy" in results
    assert "negative_accuracy" in results
    assert "overall_accuracy" in results
    # check it is an float etc.

    #write test here then code
    raise

def test_calculate_test3(amazon_data_frame_tested):
    result = calculate_test3(amazon_data_frame_tested)
    assert result, "result cannot be null"
    assert type(result) == float, "result should be a float"
    assert 0 <= result <= 100, "result should be in range 0 to 100"

def test_calculate_test4(amazon_data_frame_tested):
    result = calculate_test4(amazon_data_frame_tested)
    assert result, "result cannot be null"
    assert type(result) == float, "result should be a float"
    assert 0 <= result <= 100, "result should be in range 0 to 100"

def test_calculate_test5(amazon_data_frame_tested):
    result = calculate_test5(amazon_data_frame_tested)
    assert result, "result cannot be null"
    assert type(result) == float, "result should be a float"
    assert 0 <= result <= 100, "result should be in range 0 to 100"

