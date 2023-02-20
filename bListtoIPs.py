import re

# Define the regular expression pattern to match an IP address with subnet
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b/\d{1,2}'

# Open the input file for reading
with open('drop.txt', 'r') as infile:
    # Open the output file for writing
    with open('ips.txt', 'w') as outfile:
        # Iterate through each line in the input file
        for line in infile:
            # Find all matches of the IP address pattern in the line
            matches = re.findall(ip_pattern, line)
            # Write each IP address and subnet mask to the output file on a new line
            for match in matches:
                outfile.write(match + '\n')
