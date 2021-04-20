from setuptools import setup, find_packages

setup(name='vadertester',
      version='1.0',
      url='https://github.com/Patrick-JY/314Project',
      author='314 Project',
      license='MIT',
      packages=find_packages(include=['vadertester', 'src', 'tests']),
      package_data={'vadertester': ['json/*.json.gz']},
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      test_suite='tests',
      install_requires=['atomicwrites==1.4.0', 'attrs==19.3.0', 'beautifulsoup4==4.9.0', 'certifi==2020.4.5.1', 'chardet==3.0.4', 'click==7.1.2', 'colorama==0.4.3', 'cycler==0.10.0', 'futures==3.1.1', 'goslate==1.5.1', 'idna==2.9', 'importlib-metadata==1.6.0', 'kiwisolver==1.2.0', 'matplotlib==3.2.1', 'more-itertools==8.2.0', 'nltk~=3.5', 'numpy==1.18.4', 'packaging==20.3', 'pandas==1.0.3', 'pluggy==0.13.1', 'py==1.10.0', 'PyDictionary==1.5.2', 'pyparsing==2.4.7', 'python-dateutil==2.8.1', 'pytz==2020.1', 'requests==2.23.0', 'six==1.14.0', 'soupsieve==2.0', 'urllib3==1.25.9', 'vaderSentiment==3.3.2', 'wcwidth==0.1.9', 'zipp==3.1.0', 'tqdm~=4.46.0', 'tabulate~=0.8.7'],
      zip_safe=False)
