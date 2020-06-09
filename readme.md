Find  Amazon datasource at https://nijianmo.github.io/amazon/index.html#complete-data

Datasource used for development - Amazon instant videos 5-core (filename: Amazon_Instant_Video_5.json) this is a smaller dataset.
    
To install program from zip file:

    use 'pip install filename.zip' from the directory of the zip file
    
To install from unzipped folder:

    use 'pip install .' from the unzipped folder
    
If pip is not install:

    use 'python setup.py install' from the unzipped folder

To run program:
    
    use 'python -m vadertester'
    command line options:
    -i amount, where amount is the amount of rows to use for testing (default=5000)
    -f filename, were filename is the name of the json.gz file,
    downloaded from https://nijianmo.github.io/amazon/index.html#complete-data (default={vadertester_installed_dir}/json/reviews_Amazon_Instant_Video_5.json.gz with 37127 rows of data)
    

the program will output a 3 files to the current directory: 

output.txt with the command line output

column_graph.png which is a column graph and each MR versus compound value grouped by word length

summary_table.png which is table with the summary of the test results
