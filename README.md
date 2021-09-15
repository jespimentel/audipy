# AudiPy

Transcreve audiências gravadas em formato 'asf' (usado pelo SAJ) usando Inteligência Artificial (Google e IBM Watson).

## Tutorial (para Windows)

1. Criar uma pasta com um nome qualquer (ex. ‘audpy’) e nela copiar os arquivos ‘main.py’ e ‘funcoes.py’.

2. Criar o ambiente virtual, se for o caso (indicado para quem tem outros projetos com Python).

python -m venv env

3. Ativar o ambiente virtual (se for o caso).

env\Scripts\activate.bat 

4. Instalar as bibliotecas necessárias.

pip install SpeechRecognition moviepy ibm_watson pydub natsort

  Ou:

pip install -r requirements.txt

5. Rodar o programa:

py main.py 

6. Sugestão: usar o shebang (#!) para indicar o interpretador Python a ser usado:

#!D:\audpy\env\Scripts\python.exe
