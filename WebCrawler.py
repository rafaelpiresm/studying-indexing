import nltk
from BeautifulSoup import BeautifulSoup as Soup
import requests
import simplejson as json
from HashTable import HashTable,KeyValue,Index
import couchdb
from couchdb.mapping import TextField, IntegerField, DateTimeField, Document, Mapping, DictField, ListField, DecimalField

MAX_DEPTH = 3


class Content(Document):	
	termo = TextField()
	urls = ListField(DictField(Mapping.build(url = TextField(), frequencia = DecimalField())))


class Document(object):	

	def __init__(self, url, texto):
		self.url = url
		self.texto = texto


class MrCrawler(object):
	
	def __init__(self, url,raiz):				
		self.raiz = raiz
		self.links = []
		self.links.append(url)
		self.linksVisitados = []
		self.textos = []
		self.documentos = []
		self.depth = 0

	def getLinks(self, content):
		soup = Soup(content)
		for link in soup.findAll('a'):
			if link is not None:				
				if link.get('href') is not None:
					if link.get('href') not in self.linksVisitados:								
						if self.raiz in link.get('href'):
							self.links.append(link.get('href'))

	def crawl(self):		
		if len(self.links) > 0 and self.depth < MAX_DEPTH:
			linkAVisitar = self.links.pop()
			if linkAVisitar is not None:
				if linkAVisitar  not in self.linksVisitados:
					print 'Crawling ' + str(linkAVisitar) + ' ...'				
					try:
						response = requests.get(linkAVisitar)
						self.depth += 1
						self.adicionaALinksVisitados(linkAVisitar)
						if 'image/jpeg' not in str(response.headers['content-type']):					
							self.getLinks(str(response.content))
							novoTexto = nltk.clean_html(response.content.decode('utf-8'))
							self.textos.append(novoTexto.encode('utf-8'))			
							novoDocumento = Document(linkAVisitar,novoTexto)
							self.documentos.append(novoDocumento)
					except:
						print 'Mais uma tentativa de conexao...'
						self.crawl()
				self.crawl()
		return

	def adicionaALinksVisitados(self,link):
		if str(link) not in self.linksVisitados:
			self.linksVisitados.append(str(link))

	def countTextos(self):
		return len(self.textos)

	def getTextos(self):
		return self.textos

	def getDocumentos(self):
		return self.documentos

	def getDocumentosIntoJson(self):
		lista = {}
		for d in self.documentos:
			lista[d.url] = d.texto.encode('utf-8')
		return lista



