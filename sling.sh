#!/bin/bash
# This script requires that the notes and dropbox directories are set up with
# local git repos, cloned from a private Github repository.

dir1=/Programming/Notes
dir2=/Dropbox/Notes

src=$HOME$dir1
dst=$HOME$dir2

# get options
while getopts s:d: option
do
    case "${option}"
    in
        s) src=${OPTARG};;
        d) dst=${OPTARG};;
    esac
done

shift $(($OPTIND-1))
# slang, if necessary
if [ "$1" == "slang" ]; then
    src_old=$src
    src=$dst
    dst=$src_old
fi


# get timestamp
td=`date`
echo $td

# commit and push from source
cd $src
git add .
git commit -a -m "$td" --allow-empty
git push origin master

# pull to dest
cd $dst
git add .
git pull origin master
