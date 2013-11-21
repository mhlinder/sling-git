#!/bin/bash
# pull a directory

# get options
if [ $# -eq 0 ]; then
    dst=`pwd`
elif [ $# -eq 1 ]; then
    dst=$1
else
    echo 'Usage: sling repo'
    exit
fi

# get timestamp
td=`date`
echo $td

# pull to dest
cd $dst
git add .
git commit -a -m "$td" --allow-empty
git pull origin
