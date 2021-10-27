# AudiPy

O programa Audipy (disponível em: https://github.com/jespimentel/AudiPy) foi concebido para transcrever as audiências judiciais gravadas no formato “asf” (de streaming de vídeo avançado), usado pelo SAJ/eSAJ.

O programa também pode ser eficiente para a transcrição de vídeos baixados do YouTube, o que pode ser feito com o programa baixador_youtube (disponível em:  https://github.com/jespimentel/baixador_youtube), do mesmo autor.


Audipy 1.0: 

•	Transcrição de texto com as IAs do Google e IBM Watson

Audipy 2.0 (versão atual; na raiz):

•	Requer menos configurações

•	Transcrição com a IA do Google (em Português Br ou Inglês)

•	Não sobrescreve os arquivos-texto gerados

•	Deleta arquivos wav gerados pelo programa ao sair
 

## Tutorial (para Windows)

1. Criar uma pasta com um nome qualquer (ex. ‘audpy’) e nela copiar os arquivos ‘main.py’ e ‘funcoes.py’.

2. Criar o ambiente virtual (se for o caso: indicado somente para quem tem outros projetos com Python).

python -m venv env

3. Ativar o ambiente virtual (se for o caso).

env\Scripts\activate.bat 

4. Instalar as bibliotecas necessárias.

Versão 1.0 (IAs do Google e IBM Watson)

py -m pip install SpeechRecognition moviepy ibm_watson pydub natsort


Versão 2.0 (IA do Google, opções Português Br e Inglês)

py -m pip install SpeechRecognition moviepy pydub natsort


Ou:

py -m pip install -r requirements.txt

5. Rodar o programa (o prompt tem que estar na mesma pasta do 'main.py'):

py main.py 

6. Sugestão: editar o arquivo 'main.py' com o IDLE Shell. Usar o shebang (#!) na primeira linha de 'main.py' indica o caminho para o interpretador Python. Desse modo, o duplo clique no arquivo 'main.py' faz com que o programa rode, facilitando o seu uso.

Exemplo da 1a. linha a ser incluída no 'main.py':
#!D:\audpy\env\Scripts\python.exe

7. Mais sugestões: deixar um atalho para o 'main.py' na barra de tarefas ou área de trabalho. Modificar propriedades do 'Prompt de Comando' (clicar com o botão direito na barra superior) para alterar fonte (tipo, tamanho, cor, etc.) e cor de fundo.
