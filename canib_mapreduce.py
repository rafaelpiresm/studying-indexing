# -*- coding: utf-8 -*-
from __future__ import division
import mincemeat
import glob
import codecs
import simplejson as json
from collections import OrderedDict
import csv
import time
import pickle

PARTNERS = {
	'Criteo':'1294241712',
	'Mainadv': '1294241923',
	'My Things':'1294241902',
	'Sociomantic': '1294241744',
	'Teracent':'1294241770',
	'Triggit':'1294241860',
	'Twitter':'1294241947',
	'Vizury':'1294241849',
	'dyn1294241770':'1111111111'
}

CODE_PER_PARTNERS = {
	'1294241712':'Criteo',
	'1294241923':'Mainadv',
	'1294241902':'My Things',
	'1294241744':'Sociomantic',
	'1294241770':'Teracent',
	'1294241860':'Triggit',
	'1294241947':'Twitter',
	'1294241849':'Vizury',
	'1111111111':'dyn1294241770'
}



PATH = 'C:\\Kaggle\\dafiti\\analises\\canibalizacao\\ga\\*'

def mapfn(key,value):
	import csv
	with open(key,'r') as csv_ga:
		reader_ga = csv.reader(csv_ga, delimiter=';')
		reader_ga.next()		
		for line_ga in reader_ga:
			order_id_on_ga = line_ga[0]									
			list_partners = {}
			for line_dw in value:
				order_id_on_dw = line_dw[0]					
				if order_id_on_ga == order_id_on_dw:																	
					yield order_id_on_ga, dict({line_dw[2]:1})

def reducefn(key,value):		
	r = {}
	for d in value:
		for v in d.items():
			if not v[0] in r: 
				r[v[0]] = v[1]			
			else:
				r[v[0]] += v[1]			
	return key, r
	
	

lista = []
with open('canibalizacao.csv','r') as csv_dw:
		reader_dw = csv.reader(csv_dw, delimiter=';')
		reader_dw.next()				
		for l in reader_dw:
			lista.append(l)

text_files = glob.glob(PATH)
source = dict((file_name,lista)
			for file_name in text_files)


start = time.time()

s = mincemeat.Server()
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn
results = s.run_server(password="changeme")
end = time.time()

for r in results:
	print r
# write python dict to a file
'''output = open('myfile.pkl', 'wb')
pickle.dump(results, output)
output.close()'''

#print results
# read python dict back from the file
'''pkl_file = open('myfile.pkl', 'rb')
mydict2 = pickle.load(pkl_file)
pkl_file.close()'''

print 'Performance: '
print end - start

'''for r in results.keys():
	print results[r]'''

'''for r in results.items():	
	db.save({'author':r[0], 'termos': [{'termo':i,'frequencia':j} for i,j in OrderedDict(sorted(r[1][1].items(),key= lambda t: t[1],reverse=True)).items()]})'''