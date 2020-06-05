import argparse
import pytest

import src.pulling_cli as cli


class Test:
    def setup_class(self):
        self.parser = cli.create_parser()

    def test_argsinput(self):
        parsed = self.parser.parse_args(['-i', '10'])
        assert parsed.amount == 10
        parsed = self.parser.parse_args(['--input', '50'])
        assert parsed.amount == 50

    def test_inputfile(self):
        parsed = self.parser.parse_args(['-i','100','-f','Demo.json'])
        assert parsed.file_input == "Demo.json"
        assert parsed.amount == 100
        parsed = self.parser.parse_args(['--input','10','--file','Amazon.json'])
        assert parsed.file_input == 'Amazon.json'
        parsed = self.parser.parse_args(['-i','10'])
        assert parsed.file_input == 'Amazon_githubdata.json'

    def test_inputfile3(self):
        with pytest.raises(SystemExit):
            self.parser.parse_args(['-i', 'Hi'])
        with pytest.raises(SystemExit):
            self.parser.parse_args(['-i','10','--file'])
        with pytest.raises(SystemExit):
            self.parser.parse_args(['-f'])
        with pytest.raises(SystemExit):
            self.parser.parse_args(['-i'])
        with pytest.raises(SystemExit):
            self.parser.parse_args(['--file'])