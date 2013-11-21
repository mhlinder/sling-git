#!/bin/bash
# This script requires that the notes and dropbox directories are set up with
# local git repos, cloned from a private Github repository.

# get options
while getopts s:d: option
do
    case "${option}"
    in
        s) src=${OPTARG};;
        d) dst=${OPTARG};;
    esac
done

# shift to end of options
shift $(($OPTIND-1))

# get timestamp
td=`date`
echo $td

# commit and push from source
cd $src
git add .
git commit -a -m "$td" --allow-empty
git push origin

# slang, if necessary
if [ "$1" == "slang" ]; then
    # pull to dest
    cd $dst
    git add .
    git commit -a -m "$td" --allow-empty
    git pull origin
fi
