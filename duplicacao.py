# -*- coding: utf-8 -*-
#!/user/bin/env python
from duplica import duplicaISO
import ConfigParser

# 
cfg = ConfigParser.ConfigParser()
cfg.read('config.ini')
path = cfg.get('section1', 'path')


idcodigo = "26_07577"
gravadora = "2" 

dup = duplicaISO()

grava, arquivo = dup.localizaArquivo(path, idcodigo)

if grava:
	nomeArquivo = dup.colocaBarra(arquivo)
	dup.gravaISO(path,nomeArquivo,gravadora)
	#thread.start_new_thread(dup.gravaISO(path,nom    eArquivo,gravadora), ())

print grava

# -> Fim da rotina de duplicação

#Criar um arquivo config
#USar o web2py para chamar os númeors (tornado)
#falta tratar o erro
#falta tratar o tred (processos)