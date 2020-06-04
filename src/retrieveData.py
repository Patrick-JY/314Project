import pandas as pd
import testing_logic, pulling_logic

def init():
    # Pulls data from amazon json and prepares for analysis
    df = pulling_logic.amazon_get_df('Amazon_githubdata.json.gz')
    df = pulling_logic.prepare_amazon(df)
    # Runs sentiment analysis
    testing_logic.run_tests(df)

    # Goes through each 'MR' and determines positive and negative outcomes to compare
    df2 = df.loc[:, "Mr0"]
    print('Mr0 (Original):')
    calculate_data(df,df2, 0)
    df2 = df.loc[:, "Mr1"]
    print('Mr1 (Capitalised):')
    calculate_data(df,df2, 1)
    print('Mr1 (Lower Case):')
    calculate_data(df, df2, 2)
    df2 = df.loc[:, "Mr2"]
    print('Mr2 (Positive removed):')
    calculate_data(df,df2, 3)
    df2 = df.loc[:, "Mr3"]
    print('Mr3 (Negative removed):')
    calculate_data(df,df2, 3)


# Used for calculating overall positive/negative ratio
def calculate_data(df,df2,check):

    correct = 0
    pos_correct = 0
    neg_correct = 0
    neu_correct = 0
    k = 0

    # Needs a check as one of the dictionaries is categorised in to capitalised and non capitalised
    if check == 0:

        for x in df2:
            if x['predicted_sentiment'] == 'positive':
                if df['ReviewScore'][k] > 3:
                    correct += 1
                    pos_correct += 1

            elif x['predicted_sentiment'] == 'negative':
                if df['ReviewScore'][k] < 3:
                    correct += 1
                    neg_correct += 1

            elif x['predicted_sentiment'] == 'neutral':
                if df['ReviewScore'][k] == 3:
                    correct += 1
                    neu_correct += 1

            k += 1

        f_score = correct / k
        print("Total reviews: " + str(k) + " | Analysis match: " + str(correct))
        print("Positive Correct: " + str(pos_correct))
        print("Negative Correct: " + str(neg_correct))
        print("Neutral Correct: " + str(neu_correct))
        print("Accuracy " + str(round(f_score * 100, 2)) + "%")
        return

    elif check == 1:
        for x in df2:
            if x['capitalised']['predicted_sentiment'] == 'positive':
                if df['ReviewScore'][k] > 3:
                    correct += 1

            elif x['capitalised']['predicted_sentiment'] == 'negative':
                if df['ReviewScore'][k] < 3:
                    correct += 1

            elif x['capitalised']['predicted_sentiment'] == 'neutral':
                if df['ReviewScore'][k] == 3:
                    correct += 1
            k += 1

        f_score = correct / k
        print("Total reviews " + str(k) + " | Analysis match: " + str(correct))
        print("Accuracy " + str(round(f_score * 100, 2)) + "%")

    elif check == 2:
        for x in df2:
            if x['uncapitalised']['predicted_sentiment'] == 'positive':
                if df['ReviewScore'][k] > 3:
                    correct += 1

            elif x['uncapitalised']['predicted_sentiment'] == 'negative':
                if df['ReviewScore'][k] < 3:
                    correct += 1

            elif x['uncapitalised']['predicted_sentiment'] == 'neutral':
                if df['ReviewScore'][k] == 3:
                    correct += 1
            k += 1

        f_score = correct / k
        print("Total reviews " + str(k) + " | Analysis match: " + str(correct))
        print("Accuracy " + str(round(f_score * 100, 2)) + "%")

    elif check == 3:
        for x in df2:
            if x['predicted_sentiment'] == 'positive':
                if df['ReviewScore'][k] > 3:
                    correct += 1

            elif x['predicted_sentiment'] == 'negative':
                if df['ReviewScore'][k] < 3:
                    correct += 1

            elif x['predicted_sentiment'] == 'neutral':
                if df['ReviewScore'][k] == 3:
                    correct += 1

            k += 1

        f_score = correct / k
        print("Total reviews: " + str(k) + " | Analysis match: " + str(correct))
        print("Accuracy " + str(round(f_score * 100, 2)) + "%")


init()
