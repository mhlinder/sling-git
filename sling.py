import os, sys
from git import *
import requests

# set as environment variables
gituser = os.environ.get('GITUSER')
gitpass = os.environ.get('GITPASS')
home_dir = os.environ.get('HOME') + '/Programming/'

data = requests.get('https://api.github.com/user/repos',auth=(gituser,gitpass))
json = data.json()

repos = []
for repo in json:
    repos.append(repo['full_name'])

localrepos = {}
local = []
for dirname, dirnames, filenames in os.walk(home_dir):
    dirsplit = dirname.split("/")
    if dirsplit[-1]=='.git' and '.vim' not in dirsplit:
        f = open(dirname+"/description",'r')
        name = f.readlines()[0].rstrip()
        f.close()
        if name in repos:
            localrepos[name] = dirname
