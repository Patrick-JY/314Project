import pandas as pd
import testing_logic, pulling_logic, report_creation

case_pos = 0
case_neg = 0

def init():
    # Pulls data from amazon json and prepares for analysis
    df = pulling_logic.amazon_get_df('Amazon_githubdata.json.gz')
    df = pulling_logic.prepare_amazon(df)
    # Runs sentiment analysis
    testing_logic.run_tests(df)

    # Goes through each 'MR' and determines positive and negative outcomes to compare
    df2 = df.loc[:, "Mr0"]
    print('Mr0 (Original):')
    calculate_data(df2, 0)
    df2 = df.loc[:, "Mr1"]
    print('Mr1 (Capitalised):')
    calculate_data(df2, 1)
    df2 = df.loc[:, "Mr2"]
    print('Mr2 (Positive Removed):')
    calculate_data(df2, 2)
    df2 = df.loc[:, "Mr3"]
    print('Mr3 (Negative removed):')
    calculate_data(df2, 2)


# Used for calculating overall positive/negative ratio
def calculate_data(df2,check):

    pos = 0
    neg = 0

    # Needs a check as one of the dictionaries is categorised in to capitalised and non capitalised
    if check == 0:
        for x in df2:
            if x['predicted_sentiment'] == 'positive':
                pos += 1
            else:
                neg += 1
        overall = pos + neg
        pos_percent = round(pos / overall * 100, 2)
        neg_percent = round(neg / overall * 100, 2)
        print('Positive results: ' + str(pos) + " : " + str(pos_percent) + "%")
        print('Negative results: ' + str(neg) + " : " + str(neg_percent) + "%")
        global case_pos
        global case_neg
        case_pos = pos_percent
        case_neg = neg_percent
        return

    elif check == 1:
        for x in df2:
            if x['capitalised']['predicted_sentiment'] == 'positive':
                pos += 1
            else:
                neg += 1

    elif check == 2:
        for x in df2:
            if x['predicted_sentiment'] == 'positive':
                pos += 1
            else:
                neg += 1

    overall = pos + neg
    pos_percent = round(pos/overall * 100, 2)
    neg_percent = round(neg/overall * 100, 2)
    margin_of_error = (abs(case_pos - pos_percent) + abs(case_neg - neg_percent)) / 2

    print('Positive results: ' + str(pos) + " : " + str(pos_percent) + "%")
    print('Negative results: ' + str(neg) + " : " + str(neg_percent) + "%")
    print('Margin of error: ' + str(margin_of_error))
    return


init()
