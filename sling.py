import os, sys
from git import *

# home = os.environ.get('HOME')

# dir1 = '/Programming/Notes'
# dir2 = '/Dropbox/Notes'

# src = home + dir1
# dest = home + dir2

print len(sys.argv)
if len(sys.argv)>=5:
    args = str(sys.argv)
    src = args[2]
    dest = args[4]
    print args
#     if len(args)>=7 and args[5]=='slang':
#         src, dest = dest, src
    print src, dest
else:
    print 'Usage: sling -s src -d dst [slang]'
