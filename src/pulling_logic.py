# logic for the pulling of data
import pandas as pd
import gzip
from src.utils import join_base_path, get_negative_words, get_positive_words

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
    df = prepare_amazon(amazon_get_df(join_base_path("json/"+dataset)))
    return df


def prepare_amazon(data_frame):
    df = pd.concat([data_frame['reviewerID'] + data_frame['unixReviewTime'].astype('str'), data_frame['reviewText']
                       , data_frame['overall']], axis=1, keys=['ID', 'ReviewText', 'ReviewScore'])
    return df


def replace_with_synonyms(data_frame):
    data_frame['SynonymReplaced'] = data_frame['ReviewText']
    for index, row in data_frame.iterrows():
        row['SynonymReplaced'] = row['ReviewText']
    return data_frame


