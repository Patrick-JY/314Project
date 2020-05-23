from src.sentiment_analyser_interface import performSentimentAnalysis

def test_sentiment_analyser_interface():
    result_neg = performSentimentAnalysis("This is bad")
    assert "text" in result_neg, "text key missing from result_neg"
    assert "predicted_sentiment" in result_neg, "predicted_sentiment key missing from result_neg"
    assert "pos" in result_neg, "pos key missing from result_neg"
    assert "neg" in result_neg, "neg key missing from result_neg"
    assert "neu" in result_neg, "neu key missing from result_neg"
    assert "compound" in result_neg, "compound key missing from result_neg dictionary"
    assert result_neg["predicted_sentiment"] == "negative", "wrong sentiment found for result_neg"

    result_pos = performSentimentAnalysis("This is good")
    assert "text" in result_neg, "text key missing from result_pos"
    assert "predicted_sentiment" in result_neg, "predicted_sentiment key missing from result_pos"
    assert "pos" in result_neg, "pos key missing from result_pos"
    assert "neg" in result_neg, "neg key missing from result_pos"
    assert "neu" in result_neg, "neu key missing from result_pos"
    assert "compound" in result_neg, "compound key missing from result_pos dictionary"
    assert result_pos["predicted_sentiment"] == "positive", "wrong sentiment found for result_pos"

