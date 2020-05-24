from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

_analyzer = SentimentIntensityAnalyzer()

def performSentimentAnalysis(text):
    threshold = 0.05
    results = _analyzer.polarity_scores(text)
    results.update(text=text, predicted_sentiment='positive' if results['compound'] >= threshold else 'negative')
    return results