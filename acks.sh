#!/bin/bash
# fuzzy matching with ack (ack must be installed)

query=$1
file=$2

tmp='.*'
len=${#query}
len=$((len-1))

for i in `seq 0 $len`; do
    tmp=$tmp${query:$i:1}'.*'
done

ack $tmp $file
