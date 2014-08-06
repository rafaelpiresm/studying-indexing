import string
import nltk
import simplejson as json
import couchdb
from couchdb.mapping import TextField, IntegerField, DateTimeField, Document, Mapping, DictField, ListField, DecimalField



class Content(Document):	
	termo = TextField()
	urls = ListField(DictField(Mapping.build(url = TextField(), tf_idf = DecimalField(), frequencia = IntegerField())))

class Index(object):		
	def __init__(self):
		self.hashTable = HashTable()
		self.contents = []

	def remove_punctuation(self,termo):
		remove_punct_map = dict.fromkeys(map(ord, string.punctuation))
		return termo.translate(remove_punct_map)

	def create_index(self, documentos):
		listaTextos = []
		for d in documentos:
			listaTextos.append(nltk.wordpunct_tokenize(nltk.clean_html(d.texto.encode('utf-8'))))

		for d in documentos:
			tokens = nltk.wordpunct_tokenize(nltk.clean_html(d.texto))
			tokens = [token.lower() for token in tokens]			
			frequencency = nltk.FreqDist(tokens)			
			for i in frequencency.items():						
				termo = self.remove_punctuation(i[0])
				if len(termo) > 0:
					tc = nltk.TextCollection(listaTextos)
					tf_idf = tc.tf_idf(termo,d.texto)								
					achou = False
					index = 0
					for c in self.contents:
						index += 1
						if c.termo == termo:
							achou = True
							break
					content = Content()
					content.termo = termo
					if not achou:     
						content.urls.append(url=d.url,tf_idf=tf_idf,frequencia=i[1])        
						self.contents.append(content)
					else:
						try:
							self.contents[index].urls.append(url=d.url,tf_idf=tf_idf,frequencia=i[1])
						except:
							print 'Nao foi possivel adicionar um termo' 

				'''chave = KeyValue(i[0],d.url,tf_idf)
				if self.hashTable.lookup(chave):
					self.hashTable.append(chave)
				else:
					self.hashTable.add(chave)'''
		return self.contents


class KeyValue(object):
	def __init__(self, key, value, tf_idf):
		self.key = key
		self.tf_idf = tf_idf
		self.value = []
		self.value.append(value)


class HashTable(object):
	def __init__(self):
		self.lista = {}		

	def add(self,keyValue):		
		self.lista[keyValue.key] = keyValue.value		

	def append(self,keyValue):		
		self.lista.get(keyValue.key).append(keyValue.value.append('tf_idf:' + str(keyValue.tf_idf)))

	def lookup(self,keyvalue):
		return self.lista.has_key(keyvalue.key)
