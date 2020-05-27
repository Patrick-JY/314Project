from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

_analyzer = SentimentIntensityAnalyzer()

def performSentimentAnalysis(text):
    threshold = 0.05
    results = _analyzer.polarity_scores(text)
    if results['compound'] >= threshold:
        predicted_sentiment = 'positive'
    elif results['compound'] <= -threshold:
        predicted_sentiment = 'negative'
    else:
        predicted_sentiment = 'neutral'
    results.update(text=text, predicted_sentiment=predicted_sentiment)
    return results