import os, sys

try:  
    print(os.environ['GITHUB_TOKEN'])
    GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
except KeyError:
    print('Please define the environment variable GITHUB_TOKEN')
    sys.exit(1)


print(type(GITHUB_TOKEN))
print(len(GITHUB_TOKEN))
print(GITHUB_TOKEN[0])