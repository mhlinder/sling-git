# I am very reluctant about having my notes overwritten; so we stage them twice,
# once as a throw-away Dropbox git repo (iPhone access), and once as production
# directory (commandline access), both clones of a private Github repo.
import os
import time, datetime
from git import *

# push_to = 1 if pushing from local to dropbox
push_to = 1
txt_ext = '.txt'

structure_dirs = ['index', 'archive', 'active']
exts = ['.txt', '.otl']

dirs = {'dropbox_dir': '/Users/henry/Dropbox/Notes/', 'local_dir': '/Users/henry/Programming/Notes/'}

for git in dirs.keys():
    repo = Repo(dirs[git])
    repo.git.add('.')
    ts = time.time()
    current_time = datetime.datetime.fromtimestamp(ts).strftime('%a %b %d %I:%M:%S %Y')
    repo.git.commit('-a', "-m '%s'" % current_time)


repo.git.commit('-a','-m %s' % current_time)


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
