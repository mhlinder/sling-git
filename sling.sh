#!/bin/bash
# This script requires that the notes and dropbox directories are set up with
# local git repos, cloned from a private Github repository.
dir1=/Programming/Notes
dir2=/Dropbox/Notes

src=$HOME$dir1
dst=$HOME$dir2
if [ "$1" == "slang" ]; then
    src=$HOME$dir2
    dst=$HOME$dir1
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
