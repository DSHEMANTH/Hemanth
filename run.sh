#!/usr/bin/env bash

# example of the run script for running the word count

# first I'll load all my dependencies

# next I'll make sure that all my programs (written in Python in this example) have the proper permissions
chmod a+x ./src/word_count.py
chmod a+x running_median.py

# finally I'll execute my programs, with the input directory wc_input and output the files in the directory wc_output
python ./src/word_count.py ./wc_input ./wc_output
python ./src/running_median.py ./wc_input ./wc_output
