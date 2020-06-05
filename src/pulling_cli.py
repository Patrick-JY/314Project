# cli for the pulling
import argparse as cliparse


def create_parser():
    parser = cliparse.ArgumentParser()
    # number of input data
    parser.add_argument('-i', '--input', dest='amount', type=int,default=10,
                        required=True, help="Define amount of data to process")
    pass
    return parser

