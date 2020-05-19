from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def performSentimentAnalysis(text):
    threshold = 0.05
    analyzer = SentimentIntensityAnalyzer()
    results = analyzer.polarity_scores(text)
    results.update(text=text, predicted_sentiment='positive' if results['compound'] >= threshold else 'negative')
    return results