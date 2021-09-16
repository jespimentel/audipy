#!D:\audipy\env\Scripts\python.exe
# This file is part of AudiPy 1.0 do Pimentel.
# Copyright 2021, José Eduardo de Souza Pimentel.

""" Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. """

import sys
import funcoes
from tkinter import filedialog, Tk 

print ('\nBem vindo ao AudiPy 1.0 do Pimentel!')
print ('------------------------------------------\n')

while (True):
    print ('Selecione:')
    print ('1 - Gerar arquivos wav a partir do arquivo asf de audiência.')
    print ('2 - Obter o texto do arquivo wav com a ajuda do Google.')
    print ('3 - Obter o texto do arquivo wav com a ajuda do IBM Watson.')
    print ('4 - Inserir chave e url do IBM Watson.')
    print ('5 - Deletar arquivos wav gerados.')
    print ('6 - Sair')
    opcao = input('\n')
    
    if opcao == '1':
        # Seleciona a pasta ocultando a janela raiz
        root = Tk()
        root.withdraw()
        path_arquivo = filedialog.askopenfilename()
        funcoes.gera_wav(path_arquivo)
        funcoes.divide_wav('.\\arquivos_gerados\\audiencia.wav')

    elif opcao == '2':
        funcoes.transcrever_google()
   
    elif opcao == '3':
        funcoes.transcrever_ibm()
    
    elif opcao == '4':
        funcoes.salva_credenciais_ibm()

    elif opcao == '5':
        funcoes.remove_wav()
    
    elif opcao == '6':
        sys.exit()

    else:
        print ('Opção inválida. Tente novamente.\n')
