#!/usr/bin/bash

mkdir -p outputs

for i in "merge_sort" "depth_first_search"; do
    python3 src/$i.py > outputs/$i.txt
done
