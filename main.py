import couchdb
from WebCrawler import MrCrawler
from HashTable import Index
import simplejson as json

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
url = 'http://www.abstracaocoletiva.com.br'
raiz = 'abstracaocoletiva.com.br'
databaseName = 'abstracaocoletiva'

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

for l,k in newIndex.table.lista.items():
	d = {}
	d[l] = k
	db.save(json.loads(json.dumps(d)))

print 'Pronto! =]]'
