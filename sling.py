import os, sys
from git import *
import requests

prefix = os.environ.get('HOME') + '/Programming/'
repos = {'mhlinder/docs':'Docs'

# set as environment variables
gituser = os.environ.get('GITUSER')
gitpass = os.environ.get('GITPASS')
data = requests.get('https://api.github.com/user/repos',auth=(gituser,gitpass))
json = data.json()

repos = []
for repo in json:
    repos.append(repo['full_name'])

localrepos = {}
for dirname, dirnames, filenames in os.walk(home_dir):
    dirsplit = dirname.split("/")
    if dirsplit[-1]=='.git' and '.vim' not in dirsplit:
        f = open(dirname+"/description",'r')
        name = f.readlines()[0].rstrip()
        f.close()
        if name in repos:
            localrepos[name] = dirname


# home = os.environ.get('HOME')

# dir1 = '/Programming/Notes'
# dir2 = '/Dropbox/Notes'

# src = home + dir1
# dest = home + dir2

# print len(sys.argv)
# if len(sys.argv)>=5:
    # args = str(sys.argv)
    # src = args[2]
    # dest = args[4]
    # print args
# #     if len(args)>=7 and args[5]=='slang':
# #         src, dest = dest, src
    # print src, dest
# else:
    # print 'Usage: sling -s src -d dst [slang]'
