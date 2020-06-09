# cli for the pulling
import argparse as cliparse
from pkg_resources import resource_filename

def create_parser():
    parser = cliparse.ArgumentParser()
    # number of input data
    parser.add_argument('-i', '--input', dest='amount', type=int, default=1000,
                        required=False, help="Define amount of data to process")
    #file input
    parser.add_argument('-f', '--file', dest='file_input', type=str, default=resource_filename('vadertester', 'json/reviews_Amazon_Instant_Video_5.json.gz'),
                        required=False, help='Input json file to be processed')
    return parser
