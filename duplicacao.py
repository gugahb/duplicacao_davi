#!/user/bin/env python
# -*- coding: utf-8 -*-
#
# por: @neviim / @gugahb 	
#			 				criado..: 25/04/2013
#			 				alterado: 21/05/2013 
# -------

from duplica import duplicaISO

# -> Início da rotina duplicação
path = "/home/gustavo/iso/" 	# -> Local onde as isos estao 
idcodigo = "26_07577" 			# -> Alguem informara esse id
gravadora = 2

# --- >
dup = duplicaISO()

grava, arquivo = dup.localizaArquivo(path, idcodigo)

if grava:
	nomeArquivo = dup.colocaBarra(arquivo)
	dup.gravaISO(path,nomeArquivo,gravadora)
	#thread.start_new_thread(gravaISO(path,nomeArquivo,gravadora), ())

# -> Fim da rotina de duplicação