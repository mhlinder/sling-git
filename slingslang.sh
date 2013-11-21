#!/bin/bash
# push in one directory and pull in another

# get options
src=$1
dst=$2

# get timestamp
td=`date`
echo $td

# commit and push from source
cd $src
git add .
git commit -a -m "$td" --allow-empty
git push origin

# pull to dest
cd $dst
git add .
git commit -a -m "$td" --allow-empty
git pull origin
