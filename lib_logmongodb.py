#!/user/bin/env python
# -*- coding: utf-8 -*-
#
# nome arquivo: lib_log.mongdb.py
#				lib_log.mongdb.txt 
# por: @neviim	
#			 				criado..: 27/06/2013
#			 				alterado: 28/06/2013 
# ----------------------------------------------
from pymongo import Connection

__author__  = 'Neviim Jads <neviimdev@gmail.com>'
__date__    = '26 junho 2013'
__version__ = 0, 2, 0

# Class logDuplica, armazena os logs dos status da gravação.
#
class logDuplica:
	""" doString logDuplica
	"""
	# inicializa class 
	def __init__(self):
		# ip e porta do servidor mongoDB
		self.ipServer = 'localhost'
		self.porta = 27017

	# set um novo ip do server mongoDB
	def set_ipServer(self, ip):
		self.ipServer = ip

	# retorna o ip do server		
	def get_ipServer(self):
		return self.ipServer

	# set nova porta do server
	def set_porta(self, porta):
		self.porta = porta 

	# retorna a porta do server
	def get_porta(self):
		return self.porta

	# alaga um documento especifico 
	def apagaDocumento():
		pass # não implementado

	# efetua alteraçoes em um documento especifico 	
	def alteraDocumento():
		pass # não implementado

	# abre ou cria um banco de dados
	def conectaBanco(self, banco="test"):
		try: # não esta funcionando como quero que funcione. (rever este codigo)
			connection = Connection(self.ipServer, self.porta)
			self.db = connection[banco] # abri ou cria o banco
		except:
			print "Error: Não foi possivel conectar ao banco de dados." 
			return False

		self.dbcolection = self.db['log'] # retorna colection do obj
		return True

	# grava um registro no banco
	def gravaDocumento(self, registro):
		# registro é um jSON ex: registro = {"autor": "Neviim Jads",
		#            						 "texto": "O Senhor e meu pastor",
		#            						 "tags" : ["nada", "me", "faltara"]}
		self.tabela = self.db.log
		self.tabela.insert(registro)
		return 0

	# le um registro espacifico, parametro por "filtro"
	def get_documento(self, filtro):
		# filtro é um jSON ex: {"autor": "Carlos Silva"}
		tabela = self.db.log
		return tabela.find_one(filtro)

	# retorna quantidade de registro na tabela "log"
	def get_totalDocumento(self):
		tabela = self.db.log
		return tabela.count()

	# retorna multiplos documentos
	def listaDocumentos(self, filtro, num_de_registros=5, pagina=1):
		# filtro: é um jSON ex: {"autor": "Neviim Jads"}
		# num_de_registros: numero de registros que sera retornado
		# pagina: numero de paginas 
		linha = num_de_registros * (pagina - 1)
		# retorna um dicionario com o numero de registros encontrados
		return self.dbcolection.find(filtro).sort('_id', -1)[linha: linha + num_de_registros]