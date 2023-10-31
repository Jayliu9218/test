import os, sys

try:  
    print(os.environ['GITHUB_TOKEN'])
except KeyError:
    print('Please define the environment variable GITHUB_TOKEN')
    sys.exit(1)

