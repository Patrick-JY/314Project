# CSIT 314 Sentiment Analysis
Find  Amazon datasource at https://nijianmo.github.io/amazon/index.html#complete-data

Datasource used for development - Amazon instant videos 5-core (filename: Amazon_Instant_Video_5.json) this is a smaller dataset.
    
### To install program from zip file:
```bash
pip install filename.zip
```  
NOTE: run this from the directory of the zip file
### To install from unzipped folder:
```bash
pip install . 
```
NOTE: run this command from the unzipped folder
### If pip is not installed:
```bash
python setup.py install
```
NOTE: run this command from the unzipped folder
### To run this program:
```bash
python -m vadertester 
```
#### command line options:
* -i AMOUNT or --input AMOUNT , where amount is the amount of rows to use for testing (default=1000)
* -f FILENAME or --file FILENAME, were filename is the name of the json.gz file
(default for -f is {vadertester_installed_dir}/vadertester/json/reviews_Amazon_Instant_Video_5.json.gz with 37127 rows of data))

Data downloaded from here [here](https://nijianmo.github.io/amazon/index.html#complete-data)

### the program will output a 3 files to the current directory: 
1. output.txt with the command line output
2. column_graph.png which is a column graph and each MR versus compound value grouped by word length
3. summary_table.png which is table with the summary of the test results
