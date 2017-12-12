import os
import sys
import requests

if __name__ == "__main__":
    lang = sys.argv[1]
    reqURL = 'https://raw.githubusercontent.com/github/gitignore/master/%s.gitignore' % lang
    resp = requests.get(reqURL)
    with open('.gitignore','w') as file:
        file.write(resp.content)