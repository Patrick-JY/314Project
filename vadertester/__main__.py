from src.pulling_cli import create_parser
from src.pulling_logic import pulling_amazon, random_sample
from src.testing_logic import run_tests
# from src.report_creation import report_generation

def main():
    print("Vader tester started")
    parser = create_parser()
    args = parser.parse_args()
    df = random_sample(pulling_amazon("Amazon_githubdata.json.gz"), args.amount)

    run_tests(df)
    #report_generation(df)
    print("Vader tester finished")

if __name__=="__main__":
    main()