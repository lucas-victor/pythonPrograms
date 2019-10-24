#!/usr/bin/env python
import os
import sys
import datetime

if len(sys.argv) < 2:
    print('Obrigatorio informar o diretorio!')
    print('Usage: \npython renamer.py <diretorio>')
    exit()

dir = sys.argv[1]
#dir = "C:\\Users\\Luks\\Documents\\este"

def renomear(diretorio):
    formato = '.txt'
    prefix = 'PRJ37772-TS-'
    cont = 0

    for filename in os.listdir(diretorio):
        cont = cont + 1
        #corta o nome no .
        nomeantigo = filename.split(".")
        nomesemext = nomeantigo[0]

        #pega data de moficação do arquivo.
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(diretorio + '/' + filename))
        datastr = str(mtime)
        ano = datastr[:4]
        mes = datastr[5:7]
        dia = datastr[8:10]
        #constroi sufixo.
        sufix = '-' + dia + mes + ano + formato



        novonome = prefix + nomesemext + sufix

        if filename == 'renamer.py':
            continue

        os.rename(filename, novonome)
        print(f'Arquivo {cont} renomeado de: {filename} para: {novonome}')

#função renomeia arquivos.
renomear(dir)
