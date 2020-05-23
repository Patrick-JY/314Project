Find  Amazon datasource at http://jmcauley.ucsd.edu/data/amazon/

Datasource used for development - Amazon instant videos 5-core (filename: Amazon_Instant_Video_5.json) this is a smaller dataset.

Datasource placed in folder named json (lowercase) in main directory

To update the requirements.txt file use this cmd in the cmd window
pip freeze > requirements.txt

run tests with 
python -m pytest

for file paths to get a path relative to the base package directory use

    from src.utils import join_base_path

    relative_path = join_base_path(path)
