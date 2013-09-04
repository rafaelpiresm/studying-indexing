from HashTable import HashTable,KeyValue,Index
from WebCrawler import Document
import simplejson as json

MAX = 5
table = HashTable()
lista_documentos = []

for i in range(MAX):
	d = Document('ID' + str(i),'asdadsad asdasd asd asdadasd asdasd aasd asddada asdasd asd asdasd asdad')
	lista_documentos.append(d)

for i in range(MAX):
	d = Document('ID' + str(i),'asdadsad asdasd asd asdadasd asdasd aasd asddada asdasd asd asdasd asdad')
	lista_documentos.append(d)

for i in range(MAX):
	d = Document('ID' + str(i),'asdadsad asdasd asd asdadasd asdasd aasd asddada asdasd asd asdasd asdad')
	lista_documentos.append(d)

for i in range(MAX):
	d = Document('ID' + str(i),'asdadsad asdasd asd asdadasd asdasd aasd asddada asdasd asd asdasd asdad')
	lista_documentos.append(d)

index = Index()
index.create_index(lista_documentos)
print index.get_index_as_json()

