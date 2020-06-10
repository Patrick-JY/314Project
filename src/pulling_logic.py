# logic for the pulling of data
import pandas as pd
import gzip
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
        data = json.loads(l)
        keys_to_del = [k for k in data.keys() if k not in ["reviewerID", "unixReviewTime", "reviewText", "overall"]]
        for k in keys_to_del:
            del data[k]
        yield data, len(l)


def amazon_get_df(path):
    df = []

    with tqdm(total= get_file_size(path),unit="bytes",unit_scale=True,unit_divisor=1024, desc="Loading data") as pbar:
        for d, l in amazon_parse(path):
            pbar.update(l)
            df.append(d)
    return pd.DataFrame.from_records(df)


def pulling_amazon(dataset):
    df = prepare_amazon(amazon_get_df(dataset))
    return df


def prepare_amazon(data_frame):
    df = pd.concat([data_frame['reviewerID'] + data_frame['unixReviewTime'].astype('str'), data_frame['reviewText'].astype('str')
                       , data_frame['overall']], axis=1, keys=['ID', 'ReviewText', 'ReviewScore'])
    return df

def random_sample(df, n):
    sample = df.sample(n)
    sample.reset_index(inplace = True, drop=True)
    # adapted from https://stackoverflow.com/questions/43935592/add-space-after-full-stops
    # Sanitise data
    rx = r"\.(?=\S)"
    tqdm.pandas(desc="Sanitising text", unit="rows")
    sample['ReviewText'] = sample["ReviewText"].progress_apply(lambda row: unicodedata.normalize('NFKD', str(
        html.unescape(re.sub(r"\s+", " ", re.sub(rx, ". ", row))))).replace(". . .", ""))
    return sample

# code thanks to mark adler at
# https://stackoverflow.com/questions/24332295/how-to-determine-the-content-length-of-a-gzipped-file-in-python
def get_file_size(path):
    with open(path, "rb") as f:
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