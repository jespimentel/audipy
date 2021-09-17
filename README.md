# AudiPy

Transcreve audiências gravadas em formato 'asf' (usado pelo SAJ) usando Inteligência Artificial (Google e IBM Watson).

## Tutorial (para Windows)

1. Criar uma pasta com um nome qualquer (ex. ‘audpy’) e nela copiar os arquivos ‘main.py’ e ‘funcoes.py’.

2. Criar o ambiente virtual, se for o caso (indicado para quem tem outros projetos com Python).

python -m venv env

3. Ativar o ambiente virtual (se for o caso).

env\Scripts\activate.bat 

4. Instalar as bibliotecas necessárias.

py -m pip install SpeechRecognition moviepy ibm_watson pydub natsort

  Ou:

py -m pip install -r requirements.txt

5. Rodar o programa (o prompt tem que estar na mesma pasta do 'main.py'):

py main.py 

6. Sugestão: usar o shebang (#!) na primeira linha de 'main.py' para indicar o interpretador Python a ser usado. Desse modo, o duplo clique no arquivo 'main.py' faz com que o programa rode.

Exemplo:

#!D:\audpy\env\Scripts\python.exe

7. Sugestão: Deixar um atalho para o 'main.py' na barra de tarefas ou área de trabalho. Modificar propriedades do 'Prompt de Comando' (clicar com o botão direito na barra superior) para alterar fonte (tipo, tamanho, cor, etc.) e cor de fundo.
