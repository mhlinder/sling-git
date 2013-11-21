#!/bin/bash
# pull a directory

# get options
dst=$1

# get timestamp
td=`date`
echo $td

# pull to dest
cd $dst
git add .
git commit -a -m "$td" --allow-empty
git pull origin
