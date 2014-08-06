from __future__ import division
import couchdb
from WebCrawler import MrCrawler#, Content
from HashTable import Index
import simplejson as json
import nltk



SERVER_COUCHDB = 'http://208.68.38.13/couchdb'

def getDatabase(databaseName):
	server = couchdb.Server(SERVER_COUCHDB)
	if server.__contains__(databaseName):
		del server[databaseName]
	return server.create(databaseName)

def create_index(documentos):
	newIndex = Index()
	newIndex.create_index(documentos)
	return newIndex


print 'Iniciando crawler...'
url = "http://www.imovelweb.com.br/"
raiz = "imovelweb.com.br/"
databaseName = "imovelweb"


crawler = MrCrawler(url,raiz)
crawler.crawl()
print 'Processo de crawling finalizado...'

print 'Criando indices a partir das palavras recolhidas...'
newIndex = create_index(crawler.getDocumentos())
print 'Indice criado! Buscando server do CouchDB...'

db = getDatabase(databaseName)

print 'Server OK!'
print 'Criando indices no CouchDB...'
for content in set(newIndex.contents):
	try:
		content.store(db)
	except:
		print 'Nao foi possivel salvar o termo: ' + str(content.termo)

print 'Pronto! =]]'
