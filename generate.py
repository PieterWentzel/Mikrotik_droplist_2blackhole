# Open the input file for reading
with open('ips.txt', 'r') as infile:
    # Open the output file for writing
    with open('output_file.rsc', 'w') as outfile:
        # Write the beginning of the script to the output file
        outfile.write('/ip firewall address-list\n')
        # Iterate through each line in the input file
        for line in infile:
            # Strip whitespace from the line
            line = line.strip()
            # Check if the line contains a subnet mask
            if '/' in line:
                # Extract the IP address and subnet mask from the line
                ip_address, subnet_mask = line.split('/')
                # Write a command to add the address to the address list in the output file
                outfile.write('add address={0}/{1} list=drop_list\n'.format(ip_address, subnet_mask))
            else:
                # Write a command to add the address (without a subnet mask) to the address list in the output file
                outfile.write('add address={0} list=drop_list\n'.format(line))

