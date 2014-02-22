# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#!/usr/bin/env python2
import json

italiajs = json.loads (open ('italia.json', 'r').read ())
comcsv = open ('comuni.csv', 'r'). read (). split ('\n')

# Creo una lista che associa comuni a provincia
comlist = {}
for comline in comcsv:
	com = comline.split (';')
	
	if len (com) < 6:
		continue;
		
	if not (com[2] in comlist):
		comlist[com[2]] = []
	comlist[com[2]].append ([ com[0], com[1], com[5] ])

# Modifico italia.js in modo che contenga, per ogni provincia, anche i comuni
for regione in italiajs["regioni"]:
	newprov = []
	for provincia in regione['province']:
		prov = {}
		prov['code'] = provincia
		prov['nome'] = regione['capoluoghi'][regione['province'].index (provincia)]
		prov['comuni'] = []
		
		for com in comlist[provincia]:
			nc = {}
			nc['nome'] = com[1].decode('latin1')
			nc['cap'] = com[2]
			nc['code'] = com[0]
			prov['comuni'].append (nc)
		
		newprov.append (prov)
	
	del regione['capoluoghi']
	regione['province'] = newprov


out = open ('italia_comuni.json', 'w')
json.dump(italiajs, out, indent=4)
out.close ();



