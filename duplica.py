#!/user/bin/env python
# -*- coding: utf-8 -*-
#
# por: @neviim / @gugahb 	
#			 				criado..: 25/04/2013
#			 				alterado: 21/05/2013 
# -------

import os
import sys
import shlex
import thread
import logging
import subprocess

#
class duplicaISO(object):

	def __init__(self, *args, **kwargs):
		#
		self.CONSOLE  = "CONSOLE"
		self.DEBUG    = "DEBUG"
		self.INFO     = "INFO"
		self.ALERTA   = "WARNING"
		self.ERROR    = "ERROR"
		self.CRITICAL = "CRITICAL"

		# parametros para uso no tratamento de erros.
		logging.basicConfig(level=logging.DEBUG,
							format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
							datefmt='%H:%M:%S',
							filename='/var/tmp/duplica.log',      # ler do arquivo duplog.conf
							filemode='w')

		# defini o formato a ser apresentado os dados no arquivo de log.
		self.formato = logging.Formatter('%(asctime)s %(name)-12s: %(levelname)s %(message)s')
		self.console = logging.StreamHandler()

		self.console.setLevel(logging.INFO)
		self.console.setFormatter(self.formato)

		# adiciona o cabeçalho para o root loger
		logging.getLogger('').addHandler(self.console)


	'''
		gravaLog(vTipoLog, vMensagem)

		Descrição:
			Grava em arquivo log as mensagem e erros ocorridos.

			É importante usar os níveis de gravidade de certas quando você escreve você registrar chamadas. 
			Eu costumo usar INFO para o material geralmente útil que eu gostaria de ver seguido durante o 
			desenvolvimento, mas não em tempo de execução, enquanto eu me reservo DEBUG para a informação 
			extra detalhado que só é útil quando algo está errado. A advertência e diminuir eu sempre tenho 
			em tempo de execução, e na produção são enviados para um console de operador.

		Parametros: 
				vtipolog:
						Nivel     N. Nivel   Descrição
						--------- ---------  ---------------------------------
						NOTSET      00 		 --> 
						DEBUG		10		 --> Mensagem para Debugar 
						INFO		20		 --> Informação do usuario root
						WARNING		30		 --> Alertas
						ERROR 		40		 --> Erros ocorridos e seu codigo
						CRITICAL	50		 --> Sistema interrompido, erro graves
						
				varea:
						Qual modulo ou area da rotina esta ativando o log.

				vmensagem: 
						Mensagem passada.

		Sintax:
			gravaLog(str:"ERROR", str:"localizaArquivo", str:"Mensagem de Error ocorrida")

		Uso:
			gravaLog("ERROR", "localizaArquivo", "Arquivo não encontrado, sertifique se o codigo esta correto.")

	'''
	def gravaLog(self, vtipolog, varea, vmensagem):

		logID = logging.getLogger(varea)

		if   vtipolog == self.INFO:
			logID.info(vmensagem)
			#
		elif vtipolog == self.ERROR:
			logID.error(vmensagem)
			#
		elif vtipolog == self.DEBUG:	
			logID.debug(vmensagem)
			#
		elif vtipolog == self.ALERTA:	
			logID.warning(vmensagem)
			#
		elif vtipolog == self.CRITICAL:	
			logID.critical(vmensagem)
			#
		elif vtipolog == self.CONSOLE:
			logging.getLogger('').addHandler(console)
			logID.info(vmensagem)
			#
		else:
			logID = logging.getLogger("gravaLog") # redefini com o nome deste metodo.
			logID.critical("Definição do tipo do log indefinida, em variavel vtipolog.")


	""" 
		localizaArquivo(vPath, vIdCodigo)
		
		Descrição da Função:
			Verificar se o arquivo consta na pasta
		
		Como utilizar a funcao:
			Recebe os parametros necessários para gravação
			- Path 		-> local onde o arquivo se encontra
			- IDCodigo 	-> código no inicio do arquivo que irá localizar o nome inteiro do arquivo no Path

		Sintax:
			localizaArquivo(str:/home/duplicacao/iso; str:IDCodigo)

		Uso:
			localizaArquivo("26_07577")

		Retorna: 
			Ele retorna o nome inteiro do arquivo
			"26_07577 PERMANECER EM DEUS PE FABIO DE MELO 080311.img"

	"""
	def localizaArquivo(self, vpath, vidcodigo):
		diretorio = os.listdir( vpath ) # -> trazendo a lista pra dentro do programa
		lnome = []

		arquivo = ""
		for linha in diretorio: # -> localizar se o codigo consta em minha lista
			codigo, lnome = self.nomeIMG(linha)

			if vidcodigo == codigo:
				arquivo = linha.split()
				grava = True
			else:
				self.gravaLog(self.ERROR, "localizaArquivo", "Codigo ID: "+ str(vidcodigo) +" arquivo não foi encontrado.")
				grava = False

		return (grava, arquivo)

	""" 
		nomeIMG(vLinha)
		
		Descrição da Função:
			Verifica o nome do arquivo e separa em uma lista
		
		Como utilizar a funcao:
			Recebe um parametro que é o nome do arquivo
			Variavel vLinha

		Sintax:
			nomeIMG(string:nome_do_iso)

		Uso:
			nomeIMG("26_46357 PERMANECER EM DEUS PE FABIO DE MELO 080311.img")

		Retorna: 
			Ele retorna uma lista
			[26_46357, PERMANECER, EM, DEUS, PE, FABIO, DE, MELO, 080311.img]

	"""
	def nomeIMG(self, vlinha): 
		return vlinha.split()[0], vlinha.split() # retira o codigo da imagem da string

	""" 
		colocaBarra(vNomeArquivo)
		
		Descrição da Função:
			Coloca barra nos espacos em branco no arquivo
		
		Como utilizar a funcao:
			Recebe um parametro que é o nome do arquivo com espacos
			Variavel vNomeArquivo

		Sintax:
			colocaBarra(string:nome_do_iso)

		Uso:
			colocaBarra("26_46357 PERMANECER EM DEUS PE FABIO DE MELO 080311.img")

		Retorna: 
			Ele retorna uma string
			"26_46357\ PERMANECER\ EM\ DEUS\ PE\ FABIO\ DE\ MELO\ 080311.img"

	"""
	def colocaBarra(self, vnomearquivo): # vnomearquivo = lnome = linhaComando.ISO
		nome = ""

		for barra in range(len(vnomearquivo)):  #
			nome = nome + vnomearquivo[barra]	# concatena a String colocando a barra.
			if barra < len(vnomearquivo) -1 :   # se não for a ultima palavra da string.
				nome = nome + "\ "				# adiciona barra.
		return nome

	""" 
		gravaISO(vPath, vNome, vGravadora)
		
		Descrição da Função:
			Gravar a ISO em um gravador específico
		
		Como utilizar a funcao:
			Recebe os parametros necessários para gravação
			- Path
			- Nome do arquivo
			- Gravadora

		Sintax:
			gravaISO(str:path, str:nome_do_iso, int:gravadora) 

		Uso:
			gravaISO(path, nome.img, gravadora)

		Retorna: 
			Ele retorna uma lista
			os.system('cdrecord -v -dao dev=2,0,0 speed=4 -eject /home/gustavo/iso/26_07577\ PERMANECER\ EM\ DEUS\ PE\ FABIO\ DE\ MELO\ 080311.img')

	"""
	def gravaISO(self, vpath, vnome, vgravadora):
		# comando = "cdrecord -v -dao dev=2,0,0 speed=4 -eject " + path + colocaBarra(lnome) 

		# *** Inicio try
		try:
			comando = "cdrecord -v -dao dev=" + str(vgravadora) + ",0,0 speed=4 -eject " + vpath + vnome
			proces1 = subprocess.Popen(shlex.split( comando ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

			# grava no arquivo log  
			gravaLog(self.CONSOLE, "Imagem: "+ vnome +" gaveta: "+ str(vgravadora) +", foi gravada corretamente.")

		except subprocess.CalledProcessError, e:
			pass

		except OSError, e:			# print "Error:", e.errno, "*", e.strerror
			gravaLog(self.ERROR, "gravaISO", e.errno +" - "+ e.strerror)

		# *** Fim try
		return True