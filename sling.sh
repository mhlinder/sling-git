#!/bin/bash
# This script requires that the notes and dropbox directories are set up with
# local git repos, cloned from a private Github repository.
src=$HOME/Programming/Notes/
dst=$HOME/Dropbox/Notes/
if [ "$1" == "slang" ]; then
    src=$HOME/Dropbox/Notes/
    dst=$HOME/Programming/Notes/
fi

td=`date`
echo $td

cd $src
git add .
git commit -a -m "$td" --allow-empty
git push origin master

cd $dst
git add .
git pull origin master
