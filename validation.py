#!/usr/bin/env python3

import re
import requests

print("Checking URL integrity...")
readme = open("README.md", "r")
lines = readme.readlines() 

for line in lines: 
    # Anything that isn't a square closing bracket
    name_regex = "[^]]+"
    # http:// or https:// followed by anything but a closing paren
    url_regex = "http[s]?://[^)]+"
    markup_regex = '\[({0})]\(\s*({1})\s*\)'.format(name_regex, url_regex)

    for match in re.findall(markup_regex, line):
        length = len(match)
        if length == 2:
            source_name = match[0]
            source_url = match[1]
            try:
                r = requests.get(source_url)
                r.raise_for_status()
                print ("✅ {}".format(source_name))
            except Exception as e:
                print ("❌ {} - {}".format(source_name, e))

        elif length == 1:
            source_name = match[0]
            print ("❌ {} - Malformed markdown link.".format(source_name))
        else:
            print ("❌ {}".format(line))
print("Done.")            