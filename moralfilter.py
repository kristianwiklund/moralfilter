#!/usr/bin/python

# this file does two things:
# 1) It consumes a file with patterns suitable for use with iptables string match. 
#    See https://www.netfilter.org/documentation/HOWTO/netfilter-extensions-HOWTO-3.html#ss3.18
#    The information in the pattern file (one pattern per line) is used to produce a file with iptables commands
# 2) It invokes the generated file to set up the firewall

# This script is intended to be used in the "custom rules" section of the openwrt firewall configuration in luci
# Add it with full path

with open("rules.txt",'r') as f:
	with open("iptables.sh", 'w') as o:
		for x in f:
			x = x.rstrip()
			if not x:
				continue
			print >>o, "iptables  -I rstr 1 -p tcp -m string --string \""+x+"\" --algo bm  --from 1 --to 600 -j REJECT --reject-with tcp-reset"
			print >>o, "iptables  -I rstr 1 -p udp -m string --string \""+x+"\" --algo bm  --from 1 --to 600 -j REJECT"
