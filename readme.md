# CSIT 314 Sentiment Analysis
Find  Amazon datasource at https://nijianmo.github.io/amazon/index.html#complete-data

Datasource used for development - Amazon instant videos 5-core (filename: Amazon_Instant_Video_5.json) this is a smaller dataset.
    
### To install program from zip file
```bash
pip install filename.zip
```  
NOTE: run this from the directory of the zip file
### To install from unzipped folder
```bash
pip install . 
```
NOTE: run this command from the unzipped folder
### If pip is not installed
```bash
python setup.py install
```
NOTE: run this command from the unzipped folder
### To run this program
```bash
python -m vadertester 
```
#### command line options
* -i AMOUNT or --input AMOUNT , where amount is the amount of rows to use for testing (default=1000)
* -f FILENAME or --file FILENAME, were filename is the name of the json.gz file
(default for -f is {vadertester_installed_dir}/vadertester/json/reviews_Amazon_Instant_Video_5.json.gz with 37127 rows of data))

Data downloaded from [here](https://nijianmo.github.io/amazon/index.html#complete-data)

### the program will output a 3 files to the current directory
1. output.txt with the command line output
    ```
       Vader tester started
       Loading test data from "\314Project\vadertester\json\reviews_Amazon_Instant_Video_5.json.gz"
       Getting 1000 random rows from data
       Finished loading test data
       Running tests
       Finished running tests
       Displaying output
       Tests Running 
       Test 1: Accuracy of the Un-Modified DataSet
       Overall Accuracy: 75.7%
       Positive Accuracy: 89.8%
       Negative Accuracy: 46.74%
       Neutral Accuracy: 0.88%
       Test 1 Passed
       Test 2: 
       Comparing the capitalised dataset and the un-capitalised dataset: 
       They are 65.0% the same
       Test 2 Failed
       Test 3: 
       Comparing Mr2 to the original Dataset
       Mr2 is 98.9% similar to Mr0
       Test 3 Passed
       Test 4: 
       Comparing Mr3 to the original Dataset
       Mr3 is 95.2% similar to Mr0
       Test 4 Passed
       Test 5: 
       Comparing Mr4 within a threshold of the original Dataset
       Mr4 is 87.2% within a threshold similar to Mr0
       Test 5 passed
       Outputting Graphs:
       Column Graph grouped by Word length
       Outputting Summary: 
       |   Test Numbers | Passed   |
       |----------------|----------|
       |              1 | True     |
       |              2 | False    |
       |              3 | True     |
       |              4 | True     |
       |              5 | True     |
       Vader tester finished
    ```
2. column_graph.png which is a column graph and each MR versus compound value grouped by word length
      
3. summary_table.png which is table with the summary of the test results
