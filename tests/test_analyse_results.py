from src.testing_logic import run_tests
from src.pulling_logic import pulling_amazon, random_sample
from src.analyse_results import calculate_test1, calculate_test5, calculate_test4, calculate_test3, calculate_test2
import pytest
from pkg_resources import resource_filename

#update this test
@pytest.fixture(scope="session")
def amazon_data_frame_tested():
    df = pulling_amazon(resource_filename("vadertester",  "json/Amazon_githubdata.json.gz"))
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
    assert results["positive_accuracy"] is not None, "positive_accuracy cannot be null"
    assert type(results["positive_accuracy"]) == float, "positive_accuracy should be a float"
    assert 0 <= results["positive_accuracy"] <= 100, "result positive_accuracy be in range 0 to 100"

    assert results["neutral_accuracy"] is not None, "neutral_accuracy cannot be null"
    assert type(results["neutral_accuracy"]) == float, "neutral_accuracy should be a float"
    assert 0 <= results["neutral_accuracy"] <= 100, "result neutral_accuracy be in range 0 to 100"

    assert results["negative_accuracy"] is not None, "negative_accuracy cannot be null"
    assert type(results["negative_accuracy"]) == float, "negative_accuracy should be a float"
    assert 0 <= results["negative_accuracy"] <= 100, "result negative_accuracy be in range 0 to 100"

    assert results["overall_accuracy"] is not None, "overall_accuracy cannot be null"
    assert type(results["overall_accuracy"]) == float, "overall_accuracy should be a float"
    assert 0 <= results["overall_accuracy"] <= 100, "result overall_accuracy be in range 0 to 100"

def test_calculate_test2(amazon_data_frame_tested):
    result = calculate_test2(amazon_data_frame_tested)
    assert result is not None, "result cannot be null"
    assert type(result) == float, "result should be a float"
    assert 0 <= result <= 100, "result should be in range 0 to 100"

def test_calculate_test3(amazon_data_frame_tested):
    result = calculate_test3(amazon_data_frame_tested)
    assert result is not None, "result cannot be null"
    assert type(result) == float, "result should be a float"
    assert 0 <= result <= 100, "result should be in range 0 to 100"

def test_calculate_test4(amazon_data_frame_tested):
    result = calculate_test4(amazon_data_frame_tested)
    assert result is not None, "result cannot be null"
    assert type(result) == float, "result should be a float"
    assert 0 <= result <= 100, "result should be in range 0 to 100"

def test_calculate_test5(amazon_data_frame_tested):
    result = calculate_test5(amazon_data_frame_tested)
    assert result is not None, "result cannot be null"
    assert type(result) == float, "result should be a float"
    assert 0 <= result <= 100, "result should be in range 0 to 100"

