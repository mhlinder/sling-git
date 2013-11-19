import os
import time, datetime
from git import *

# push_to = 1 if pushing from local to dropbox
push_to = 1
txt_ext = '.txt'

structure_dirs = ['index', 'archive', 'active']
exts = ['.txt', '.otl']

dirs = {'dropbox_dir': '/Users/henry/Dropbox/Notes/', 'local_dir': '/Users/henry/Programming/Notes/'}

# commit each directory first
repo = Repo(dirs['local_dir'])
ts = time.time()
current_time = datetime.datetime.fromtimestamp(ts).strftime('%a %b %d %I:%M:%S %Y')


if push_to:
    notes_dir = dirs['local_dir']
    dst_dir = dirs['dropbox_dir']
else:
    notes_dir = dirs['dropbox_dir']
    dst_dir = dirs['local_dir']

mv_list = [] # (from, to)
for dirname, dirnames, filenames in os.walk(notes_dir):
    if dirname.split('/')[-1] in structure_dirs:
        for filename in filenames:
            src = os.path.join(dirname, filename)
            dst = os.path.join(dst_dir, filename)
            if filename[-4:] == '.otl':
                dst = dst[:-4] + txt_ext

            mv_list.append( (src, dst) )
