#!/bin/bash
notes=$HOME/Programming/Notes/
dropbox=$HOME/Dropbox/Notes/

td=`date`
echo $td

cd notes
git add .
git commit -a -m "$td" --allow-empty

cd $dropbox
git add .
git commit -a -m "$td" --allow-empty
