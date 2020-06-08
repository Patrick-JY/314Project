# logic for the pulling of data
import pandas as pd
import gzip
from src.utils import join_base_path
import re
import html
import unicodedata
from tqdm import tqdm
import zlib
import warnings
import json
import os
from sys import getsizeof
# code for data prep is modified from the sample given in http://jmcauley.ucsd.edu/data/amazon/


def amazon_parse(path):

    g = gzip.open(path, 'rb')
    for l in g:
        yield json.loads(l), l


def amazon_get_df(path):
    i = 0
    df = {}

    with tqdm(total= get_file_size(path),unit="bytes",unit_scale=True,unit_divisor=1024) as pbar:
        for d, l in amazon_parse(path):
            pbar.update(len(l))
            df[i] = d
            i += 1
    return pd.DataFrame.from_dict(df, orient='index')


def pulling_amazon(dataset):
    df = prepare_amazon(amazon_get_df(join_base_path("json/"+dataset)))
    return df


def prepare_amazon(data_frame):
    df = pd.concat([data_frame['reviewerID'] + data_frame['unixReviewTime'].astype('str'), data_frame['reviewText']
                       , data_frame['overall']], axis=1, keys=['ID', 'ReviewText', 'ReviewScore'])
    # adapted from https://stackoverflow.com/questions/43935592/add-space-after-full-stops
    # Sanitise data
    rx = r"\.(?=\S)"
    df['ReviewText'] = df["ReviewText"].apply(lambda row: unicodedata.normalize('NFKD',str(html.unescape(re.sub(r"\s+", " ", re.sub(rx, ". ", row))))).replace(". . .", ""))
    return df

def random_sample(df, n):
    sample = df.sample(n)
    sample.reset_index(inplace = True, drop=True)
    return sample

# code thanks to mark adler at
# https://stackoverflow.com/questions/24332295/how-to-determine-the-content-length-of-a-gzipped-file-in-python
def get_file_size(path):
    f = open(path, "rb")
    total = 0
    buf = f.read(1024)
    while True:  # loop through concatenated gzip streams
        z = zlib.decompressobj(15 + 16)
        while True:  # loop through one gzip stream
            while True:  # go through all output from one input buffer
                total += len(z.decompress(buf, 4096))
                buf = z.unconsumed_tail
                if buf == b"":
                    break
            if z.eof:
                break  # end of a gzip stream found
            buf = f.read(1024)
            if buf == b"":
                warnings.warn("incomplete gzip stream")
                break
        buf = z.unused_data
        z = None
        if buf == b"":
            buf = f.read(1024)
            if buf == b"":
                break
    return total