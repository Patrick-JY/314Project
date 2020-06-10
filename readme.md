# CSIT 314 Sentiment Analysis Testing Tool
The testing tool performs tests on the VADER Sentiment Analysis Python Package (https://github.com/cjhutto/vaderSentiment)
The tool has been tested on Python 3.7, 3.8
### To install program from zip file
```bash
pip install filename.zip
```  
NOTE: run this from the directory of the zip file
### To install from unzipped folder
```bash
pip install . 
```  
NOTE: run this from the directory of the unzipped file
### To install from github source
```bash
pip install git+https://github.com/Patrick-JY/314Project.git
```  
### If pip is not installed
```bash
python setup.py install
```
NOTE: run this from the directory of the unzipped file
### To run tests while installing with setup.py use 
```bash
python setup.py install pytest
```
NOTE: run this from the directory of the unzipped file
### To run this program
```bash
python -m vadertester 
```
#### command line options
* -i AMOUNT or --input AMOUNT , where amount is the amount of rows to use for testing (default=1000)
* -f FILENAME or --file FILENAME, were filename is the name of the json.gz file
(default for -f is {VADERTESTER_INSTALLED_DIR}/vadertester/json/reviews_Amazon_Instant_Video_5.json.gz with 37127 rows of data))

Data downloaded from [here](https://nijianmo.github.io/amazon/index.html#complete-data) (Note: specifically the 5-core review data)

### the program will output 3 files to the current directory
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
2. column_graph.png which is a column graph with each MR versus average compound value grouped by word length
      
3. summary_table.png which is table with the summary of the test results

The default version of the VADER Sentiment tested is 3.3.2

### To install other versions of vaderSentiment to use with the testing tool
```bash
pip install vaderSentiment==VERSION_NO 
where VERSION_NO is the version of vaderSentiment to install
or to install latest version
pip install vaderSentiment --upgrade
```
