#!/user/bin/env python
# -*- coding: utf-8 -*-
#
# por: @neviim / @gugahb 	
#			 				criado..: 25/04/2013
#			 				alterado: 13/05/2013 
# -------

import os
import sys
import thread

#
class duplicaISO(object):

	def __init__(self, *args, **kwargs):
		pass

	""" 
		localizaArquivo(vPath, vIdCodigo)
		
		Descrição da Função:
			Verificar se o arquivo consta na pasta
		
		Como utilizar a funcao:
			Recebe os parametros necessários para gravação
			- Path
			- IDCodigo

		Sintax:
			localizaArquivo(string:IDCodigo)

		Uso:
			localizaArquivo("26_07577")

		Retorna: 
			Ele retorna o nome inteiro do arquivo
			"26_07577 PERMANECER EM DEUS PE FABIO DE MELO 080311.img"

	"""
	def localizaArquivo(self, vPath, vIdCodigo):
		diretorio = os.listdir( vPath ) # -> trazendo a lista pra dentro do programa
		lnome = []
		grava = False

		arquivo = ""
		for linha in diretorio: # -> localizar se o codigo consta em minha lista
			codigo, lnome = nomeIMG(linha)

			if vIdCodigo == codigo:
				arquivo = linha.split()
				grava = True

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
	def nomeIMG(self, vLinha): # -> Funcao by @neviim
		return vLinha.split()[0], vLinha.split() # retira o codigo da imagem da string

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
	def colocaBarra(self, vNomeArquivo): # vNomeArquivo = lnome = linhaComando.ISO
		nome = ""

		for barra in range(len(vNomeArquivo)):  #
			nome = nome + vNomeArquivo[barra]	# concatena a String colocando a barra.
			if barra < len(vNomeArquivo) -1 :   # se não for a ultima palavra da string.
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
	def gravaISO(self, vPath, vNome, vGravadora):
		# comando = "cdrecord -v -dao dev=2,0,0 speed=4 -eject " + path + colocaBarra(lnome) 
		comando = "cdrecord -v -dao dev=" + str(vGravadora) + ",0,0 speed=4 -eject " + vPath + vNome
		executar = "os.system('" + comando + "')"

		# executa
		print executar # falta escrever tratamento de erro.
		
		return True
