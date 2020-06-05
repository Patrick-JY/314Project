import argparse
import pytest

import src.pulling_cli as cli


class Test:
    def setup_class(self):
        self.parser = cli.create_parser()

    def test_argsi(self):
        parsed = self.parser.parse_args(['-i', '10'])
        assert parsed.amount == 10

    def test_argsinput(self):
        parsed = self.parser.parse_args(['--input', '50'])
        assert parsed.amount == 50

    def test_inputstring(self):
        with pytest.raises(SystemExit):
            self.parser.parse_args(['-i', 'Hi'])
    def test_inputfile(self):
        parsed = self.parser.parse_args(['-i','100','-f','Demo.json'])
        assert parsed.file_input == "Demo.json"
        assert parsed.amount == 100
    def test_inputfile1(self):
        parsed = self.parser.parse_args(['-i','10'])
        assert parsed.file_input == 'Amazon_githubdata.json'