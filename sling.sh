#!/bin/bash
# push a directory

# get options
src=$1

# get timestamp
td=`date`
echo $td

# commit and push from source
cd $src
git add .
git commit -a -m "$td" --allow-empty
git push origin
