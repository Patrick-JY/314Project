import argparse

import pytest

from src.pulling_cli import *


class Test:
    def setup_class(self):
        self.parser = create_parser()

    def test_argsi(self):
        print('test argument -i')
        parsed = self.parser.parse_args(['-i','10'])
        assert parsed.amount == 10
    def test_argsinput(self):
        print('test argument --input')
        parsed = self.parser.parse_args(['--input','50'])
        assert parsed.amount == 50
    def test_mock_parser(self):
        self.parser.add_argument('-o','--output',action="store_true",dest="output",default=False)
        parsed = self.parser.parse_args(['-i','10','-o'])
        assert parsed.output == True

