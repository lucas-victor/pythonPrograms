import os

#metodos os.path

isDir = os.path.isdir('./tmp')
print('os.path.isdir', isDir)

isFile = os.path.isfile('C:/Users/Luks/PycharmProjects/cursoPython')
print('os.path.isfile', isFile)

existS = os.path.exists('C:/Users/Luks/PycharmProjects/cursoPython')
print('os.path.exists', existS)

#separa o caminho inteiro do arquivo.
splitCaminho = os.path.split('C:/Users/Luks/PycharmProjects/cursoPython/arquivoTeste3.txt')
print('os.path.split', splitCaminho)

#usado somente para obter o caminho.
joinPathName = os.path.join('C:/Users/Luks/PycharmProjects/cursoPython', 'arquivoTeste3.txt')
print('os.path.join', joinPathName)

#pega o caminho inteiro.
dirName = os.path.dirname('C:/Users/Luks/PycharmProjects/cursoPython/arquivoTeste3.txt')
print('os.path.dirname', dirName)

#pega o somente o nome do arquivo no final do caminho.
baseName = os.path.basename('C:/Users/Luks/PycharmProjects/cursoPython/arquivoTeste3.txt')
print('os.path.basename', baseName)

#vai separar o que é nome do arquivo da extensão.
splitText = os.path.splitext('C:/Users/Luks/PycharmProjects/cursoPython/arquivoTeste3.txt')
print('os.path.splitext', splitText)

#pega o caminho com separadores misturados e converte no separador do SO utilizado pela aplicação.
norm = os.path.normpath("C:\\Users\Luks\PycharmProjects/cursoPython/arquivoTeste3.txt")
print('os.path.normpath', norm)

absPathVazio = os.path.abspath('')
print('os.path.abspath("")', absPathVazio)

absPathDir = os.path.abspath('tmp')
print("os.path.abspath('tmp')", absPathDir)

absPath = os.path.abspath('.')
print('os.path.abspath(".")', 'currentDir', absPath)

absPath2 = os.path.abspath('..')
print('os.path.abspath("..")', 'parentDir' , absPath2)

