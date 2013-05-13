# -*- coding: utf-8 -*-
#!/user/bin/env python
from duplica import *

# -> Início da rotina duplicação
path = "/home/gustavo/iso/" # -> Local onde as isos estao 
idcodigo = "26_07577" # -> Alguem informara esse id
gravadora = 2

localizaArquivo = duplicaISO(path, idcodigo)
grava = ""

if grava:
	nomeArquivo = duplicaISO()
	colocaBarra = duplicaISO()


'''
grava, arquivo = localizaArquivo(path, idcodigo)

if grava:
	nomeArquivo = colocaBarra(arquivo)
	gravaISO(path,nomeArquivo,gravadora)
	#thread.start_new_thread(gravaISO(path,nomeArquivo,gravadora), ())
'''

print localizaArquivo
print nomeArquivo

# -> Fim da rotina de duplicação

#Criar um arquivo config
#USar o web2py para chamar os númeors (tornado)
#falta tratar o erro
#falta tratar o tred (processos)