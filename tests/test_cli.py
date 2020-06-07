import argparse
import pytest

import src.pulling_cli as cli


class TestCli:
    def setup_class(self):
        self.parser = cli.create_parser()

    def test_argsinput(self):
        parsed = self.parser.parse_args(['-i', '10'])
        assert parsed.amount is 10
    def test_input(self):
        parsed = self.parser.parse_args(['--input', '50'])
        assert parsed.amount is 50

    def test_inputfile1(self):
        parsed = self.parser.parse_args(['-i','100','-f','Demo.json'])
        assert parsed.file_input is "Demo.json"
        assert parsed.amount is 100

    def test_inputfile2(self):
        parsed = self.parser.parse_args(['--input','10','--file','Amazon.json'])
        assert parsed.file_input is 'Amazon.json'

    def test_inputfile3(self):
        parsed = self.parser.parse_args(['-i','10'])
        assert parsed.file_input == 'Amazon_githubdata.json.gz'

    def test_type(self):
        parsed = self.parser.parse_args(['-i','10'])
        assert type(parsed.amount) is int
        assert type(parsed.file_input) is str
        
    def test_type2(self):
        parsed = self.parser.parse_args(['-i','10','-f','hello'])
        assert type(parsed.file_input) is str

    def test_error1(self):
        with pytest.raises(SystemExit):
            self.parser.parse_args(['-i', 'Hi'])

    def test_error2(self):
        with pytest.raises(SystemExit):
            self.parser.parse_args(['-i','10','--file'])

    def test_error3(self):
        with pytest.raises(SystemExit):
            self.parser.parse_args(['-f'])

    def test_error4(self):
        with pytest.raises(SystemExit):
            self.parser.parse_args(['-i'])

    def test_error5(self):
        with pytest.raises(SystemExit):
            self.parser.parse_args(['--file'])

    def test_error6(self):
        with pytest.raises(SystemExit):
            self.parser.parse_args(['--input'])