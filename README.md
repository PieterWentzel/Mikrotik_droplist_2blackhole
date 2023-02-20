# Mikrotik_droplist_2blackhole
A repo containing shell and python scripts to convert a .txt file to .rsc file to be run on mikrotik

The purpose of this project is to create a free and easy way to use the drop list from spamhaus on mikrotik routers.

1. update.sh will start by removing all previous generated files and downloading the drop.txt file from spamhaus.
2. update.sh will then run a python script bListtoIPs.py that extracts the ip address and subnet mask from drop.txt
3. Lastly generate.py will run to create output_file.rsc, it will take the ips and put them in a .rsc script to add them to a mikrotik address list

You will need to setup a cron job to run update.sh once a day to refresh the list and you will need to fetch the output_file.rsc with your mikrotik then import it.

You have 2 choices then first is to use a regular firewall rule do drop ips in the list called droplist or you can use mikrotiks new implementation of BGP to advertise these ips to other routers in your network and then blackhole them.

In order for ROS 7 to advertise routes, the routes must first be in the routing table. I have included the mikrotik scripts to take the address list and also add it to the ip routes.
