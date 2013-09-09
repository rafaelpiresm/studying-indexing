import nltk
import simplejson as json

class Index(object):
	
	def __init__(self):		
		self.table = HashTable()

	def create_index(self, documentos):
		for d in documentos:
			tokens = nltk.wordpunct_tokenize(nltk.clean_html(d.texto))
			tokens = [token.lower() for token in tokens]
			tokens = set(tokens)
			for t in set(tokens):
				chave = KeyValue(t.lower(),d.url)
				if self.table.lookup(chave):
					self.table.append(chave)
				else:
					self.table.add(chave)
		return self.table
	
	def get_index_as_json(self):
		d = {}
		for l,k in self.table.lista.items():
			d[l] = k
		return json.dumps(d)

	def get_document_items(self):		
		return self.table.lista.items()
		
		#return type(self.table.lista['asdadsad']) isso e lista



class KeyValue(object):
	def __init__(self, key, value):
		self.key = key
		self.value = []
		self.value.append(value)

class HashTable(object):
	def __init__(self):
		self.lista = {}

	def add(self,keyValue):		
		self.lista[keyValue.key] = keyValue.value		

	def append(self,keyValue):		
		self.lista.get(keyValue.key).append(keyValue.value)

	def lookup(self,keyvalue):
		return self.lista.has_key(keyvalue.key)
