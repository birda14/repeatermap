#! usr/bin/env python

from os.path import exists
from sys import argv

import simplejson as json

in_file = 'input.json'
data = json.load(open(in_file))
wantedKeys =["State ID"]
csv_output = []
result = ""

for key in wantedKeys:    
        result += key+","
csv_output.append(result)

for d in data:
    result = ""
    for key in d.keys():
            if key in wantedKeys:
                result += d[key]+","
    csv_output.append(result)

output = open("out_file.csv", 'w')
for line in csv_output:
    output.write(line)

