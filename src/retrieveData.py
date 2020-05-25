import pandas as pd
import testing_logic, pulling_logic


def init():
    # DataFrame to contain actual analysis of data
    df = pulling_logic.amazon_get_df('Amazon_githubdata.json.gz')
    df = pulling_logic.prepare_amazon(df)
    testing_logic.run_tests(df)
    x = 0
    pos = 0
    neg = 0
    overall = 0
    df2 = df.loc[:, "Mr1"]
    for x in df2:
        if x['capitalised']['predicted_sentiment'] == 'positive':
            pos += 1
        else:
            neg += 1

    overall = pos + neg
    pos_percent = round(pos/overall * 100, 2)
    neg_percent = round(neg/overall * 100, 2)

    print('Positive results: ' + str(pos) + " : " + str(pos_percent) + "%")
    print('Negative results: ' + str(neg) + " : " + str(neg_percent) + "%")


init()