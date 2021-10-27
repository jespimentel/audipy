#!D:\audipy\env\Scripts\python.exe
# This file is part of AudiPy 2.0 do Pimentel.
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

import funcoes, sys

print ('\nBem vindo ao AudiPy 2.0 do Pimentel!')
print ('------------------------------------------\n')

while (True):
    print ('Selecione:')
    print ('1 - Gerar os arquivos wav')
    print ('2 - Obter o texto em Português (Br)')
    print ('3 - Obter o texto em Inglês')
    print ('4 - Deletar arquivos wav gerados.')
    print ('5 - Sair')
    opcao = input('\n')
    
    if opcao == '1':
        funcoes.escolhe_arquivo()

    elif opcao == '2':
        funcoes.transcrever_google('pt-BR', funcoes.gera_nome())
   
    elif opcao == '3':
        funcoes.transcrever_google('en-US', funcoes.gera_nome())
    
    elif opcao == '4':
        funcoes.remove_wav()
    
    elif opcao == '5':
        funcoes.remove_wav()
        sys.exit()

    else:
        print ('Opção inválida. Tente novamente.\n')