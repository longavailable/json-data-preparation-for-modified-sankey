# -*- coding: utf-8 -*-
"""
* Updated on 2023/06/05
* Python3
**
* - Concatenate links and nodes for M-Sankey charting
"""

import json
import csv
import pathlib
from pprint import pprint

dataset = {}

# convert nodes.csv to dictionary
filenameNodes = pathlib.Path('nodes.csv')
with open(filenameNodes) as f:
	reader = csv.DictReader(f)
	dataNode = [r for r in reader]	
#pprint(dataNode)

# re-organize nodes into dataset
dataset['nodes'] = []
for row in dataNode:
	dataset['nodes'].append({
		'node': int(row['node']),
		'name': 'Class-' + row['class'] + '-in-' + row['year']
	})	

# convert links.csv to dictionary
filenameLinks = pathlib.Path('links.csv')
with open(filenameLinks) as f:
	reader = csv.DictReader(f)
	dataLink = [r for r in reader]
#pprint(dataLink)

# re-organize nodes into dataset
dataset['links'] = []
for row in dataLink:
	dataset['links'].append({
		'source': int(row['source']),
		'target': int(row['target']),
		'value': float(row['value'])
	})

# export
filename = pathlib.Path('data-msankey.json')
with open(filename,'w') as outfile:
	json.dump(dataset,outfile)

print('Done')