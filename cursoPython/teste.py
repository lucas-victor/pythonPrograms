import os
import datetime
import pathlib

ca = 'C:\\Users\\Luks\\Documents\\este\\arq1.txt'
arq = os.path.getctime('C:\\Users\\Luks\\Documents\\este\\arq1.txt')
mtime = datetime.datetime.fromtimestamp(os.path.getmtime(ca))
datastr = str(mtime)
ano = datastr[:4]
mes = datastr[5:7]
dia = datastr[8:10]

#print(arq)
print(mtime)
print(dia+mes+ano)
