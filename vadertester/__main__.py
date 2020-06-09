from src.pulling_cli import create_parser
from src.pulling_logic import pulling_amazon, random_sample
from src.testing_logic import run_tests
from src.report_creation import report_generation
from src.utils import join_base_path
#https://stackoverflow.com/questions/550470/overload-print-python
class writer :
    def __init__(self, *writers) :
        self.writers = writers

    def write(self, text) :
        for w in self.writers :
            w.write(text)

import sys

def main():
    saved = sys.stdout
    with open(join_base_path('output/output.txt'), 'w') as fout:
        sys.stdout = writer(sys.stdout, fout)
        print("Vader tester started")
        parser = create_parser()
        args = parser.parse_args()
        print("Loading test data")
        df = random_sample(pulling_amazon(args.file_input), args.amount)
        print("Finished loading test data")
        print("Running tests")
        run_tests(df)
        print("Finished running tests")
        print("Displaying output")
        report_generation(df)
        print("Vader tester finished")
    sys.stdout = saved

if __name__=="__main__":
    main()