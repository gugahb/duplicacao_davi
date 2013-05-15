# -*- coding: utf-8 -*-
#!/user/bin/env python
from duplica import duplicaISO

# -> Início da rotina duplicação
path = "/home/gustavo/iso/" # -> Local onde as isos estao 
idcodigo = "26_07577" # -> Alguem informara esse id
gravadora = 2

dup = duplicaISO()

grava, arquivo = dup.localizaArquivo(path, idcodigo)

if grava:
	nomeArquivo = dup.colocaBarra(arquivo)
	dup.gravaISO(path,nomeArquivo,gravadora)

'''
grava, arquivo = localizaArquivo(path, idcodigo)

if grava:
	nomeArquivo = colocaBarra(arquivo)
	gravaISO(path,nomeArquivo,gravadora)
	#thread.start_new_thread(gravaISO(path,nomeArquivo,gravadora), ())
'''

# -> Fim da rotina de duplicação

#Criar um arquivo config
#USar o web2py para chamar os númeors (tornado)
#falta tratar o erro
#falta tratar o tred (processos)