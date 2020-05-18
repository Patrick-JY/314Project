import argparse
import importlib

import pytest

import src.pulling_cli as cli


class Test:
    def setup_class(self):
        self.parser = cli.create_parser()

    def test_argsi(self):
        print('test argument -i')
        parsed = self.parser.parse_args(['-i', '10'])
        assert parsed.amount == 10

    def test_argsinput(self):
        print('test argument --input')
        parsed = self.parser.parse_args(['--input', '50'])
        assert parsed.amount == 50

    def test_mock_parser(self):
        self.parser.add_argument('-o', '--output',
                                 action="store_true", dest="output", default=False)
        parsed = self.parser.parse_args(['-i', '10', '-o'])
        assert parsed.output == True
        with pytest.raises(SystemExit):
            self.parser.parse_args(['-i'])
    def test_inputstring(self):
        with pytest.raises(SystemExit):
            self.parser.parse_args(['-i', 'Hi'])
