#!/bin/bash

START=`pwd`
main=$HOME/Programming

# get timestamp
td=`date`
echo $td

# find all non-vim repos
for repo in `find $main -name .git | awk '!/\.vim/ { print }'`
do
    cd ${repo%\/\.git}
    git commit -a -m "scattering to github $td" --allow-empty
    git push origin master
    git push origin develop
done

cd $START
