from __future__ import division
import couchdb
from WebCrawler import MrCrawler, Content
from HashTable import Index
import simplejson as json
import nltk



SERVER_COUCHDB = 'http://208.68.38.13/couchdb'

def getDatabase(databaseName):
	server = couchdb.Server(SERVER_COUCHDB)
	if server.__contains__(databaseName):
		del server[databaseName]
	return server.create(databaseName)

def create_index():
	newIndex = Index()
	newIndex.create_index(crawler.getDocumentos())
	return newIndex


print 'Iniciando crawler...'
url = "http://www.abstracaocoletiva.com.br"
raiz = "abstracaocoletiva.com.br"
databaseName = "abstracaocoletiva"


crawler = MrCrawler(url,raiz)
crawler.crawl()
print 'Processo de crawling finalizado...'

print 'Criando indices a partir das palavras recolhidas...'
newIndex = create_index()
print 'Indice criado! Buscando server do CouchDB...'

db = getDatabase(databaseName)

#db.save(json.loads(newIndex.get_index_as_json()))
print 'Server OK!'
print 'Criando indices no CouchDB...'

for doc in newIndex.table.lista.items():
	content = Content()
	termo = doc[0]
	content.termo = termo
	tc = nltk.TextCollection(doc[1])
	for d in doc[1]:				
		tf = tc.tf_idf(termo,d)
		content.urls.append(url=d,frequencia=tf)
	try:
		content.store(db)
	except:
		print 'Nao foi possivel salvar o termo: ' + str(doc[0])
 

print 'Pronto! =]]'
