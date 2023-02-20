#!/bin/bash

#Remove old files

rm "drop.txt"
rm "ips.txt"
rm "output_file.rsc"
rm /home/pi/FTP/files/droplist.rsc

# Download the file using wget
wget https://www.spamhaus.org/drop/drop.txt

# Execute the first Python script
python bListtoIPs.py

# Execute the second Python script
python generate.py

# Copy rsc file to ftp directory

cp output_file.rsc /home/pi/FTP/files/droplist.rsc
