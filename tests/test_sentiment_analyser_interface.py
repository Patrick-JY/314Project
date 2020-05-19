from src.sentiment_analyser_interface import performSentimentAnalysis
def test_sentiment_analyser_interface():
    data = performSentimentAnalysis("This is bad")
    assert "text" in data
    assert "predicted_sentiment" in data
    assert "pos" in data
    assert "neg" in data
    assert "neu" in data
    assert "compound" in data
    assert data["predicted_sentiment"] == "negative", "wrong sentiment found"
