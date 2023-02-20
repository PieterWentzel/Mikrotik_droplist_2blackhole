#!/bin/bash

#Remove old files

rm "drop.txt"
rm "ips.txt"
rm "output_file.rsc"

# Download the file using wget
wget https://www.spamhaus.org/drop/drop.txt

# Execute the first Python script
python bListtoIPs.py

# Execute the second Python script
python generate.py
