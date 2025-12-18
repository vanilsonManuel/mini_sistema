# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 13:55:53 2025

@author: Vanilson Manuel by curso em video
"""

import lib.interface as it # Importar com alias (mais limpo)
import lib.arquivo as ar

arquivo ='arquivo.txt'
if not ar.arquivoExiste(arquivo):
    ar.criarArquivo(arquivo)
    
    


while True:
    resp=it.menu(['LISTAR PESSOAS','CADASTRAR PESSOA','SAIR'])
    
    if resp ==1:
        ar.lerArquivo(arquivo)
    elif resp ==2:
        print('Novo Cadastro:')
        nome=input(str('Nome: '))
        idade=it.leiaInt('Idade: ')
        ar.cadastrar(arquivo,nome,idade)

    elif resp == 3:
        it.cabecalho('\033[1;31mSAIU DO PROGRAMA\033[m')
        break
    else:
        print('\033[1;31m\n opção invalida \033[m')
            



