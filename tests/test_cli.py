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
        print('test argument --input')
        parsed = self.parser.parse_args(['--input', '50'])
        assert parsed.amount == 50

    def test_inputstring(self):
        with pytest.raises(SystemExit):
            self.parser.parse_args(['-i', 'Hi'])
    def test_inputfile(self):
        parsed = self.parser.parse_args(["-f","Demo.json"])
        assert parsed.file == "Demo.json"