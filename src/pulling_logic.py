# logic for the pulling of data
import pandas as pd
import gzip
# code for data prep is modified from the sample given in http://jmcauley.ucsd.edu/data/amazon/


def amazon_parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)


def amazon_get_df(path):
    i = 0
    df = {}
    for d in amazon_parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')


def pulling_amazon(dataset):
    pulled_df = amazon_get_df("../json/"+dataset)

    df = pd.concat([pulled_df['reviewerID'] + pulled_df['unixReviewTime'].astype('str'), pulled_df['reviewText']
                       , pulled_df['overall']], axis=1,keys=['ID', 'ReviewText', 'ReviewScore'])

    return df


