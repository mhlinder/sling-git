#!/bin/bash
# scatter all remote-origin local repos to github

START=`pwd`
main=$HOME/Programming

# get timestamp
td=`date`
echo $td

if [ "$1" != "scetter" ]; then
    # find all non-vim repos
    for repo in `find $main -name .git | awk '!/\.vim/ { print }'`
    do
        cd ${repo%\/\.git}
        git commit -a -m "scattering to github $td" --allow-empty
        git push origin master
        git push origin develop
    done
else
    for repo in `find $main -name .git | awk '!/\.vim/ { print }'`
    do
        cd ${repo%\/\.git}
        git pull origin master
        git pull origin develop
    done
fi

cd $START
