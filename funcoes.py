# This file is part of FalaPraTexto 1.0 do Pimentel.
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

import moviepy.editor as mp
import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Exporta o resultado para arquivo texto
def gera_texto (resultado, ia):
    print ('Gerando arquivo texto...')
    nome_arquivo = 'texto_' + ia + '.txt'
    with open(nome_arquivo, mode ='w') as f:
        f.write(resultado)
    print ('Arquivo txt gerado com sucesso!')

# Obtém informações de login do IBM Watson
def obtem_url_key ():
    print ('Tentando obter informações de login...')
    try:
        f = open('info_login.txt', 'r')
        url = str(f.readline().replace('\n', ''))
        apikey = str(f.readline().replace('\n', ''))
        return url, apikey
    except:
        print('Ops... Algo deu errado com o arquivo info_login.txt!\n')

# Opção 1 - Gerar arquivo wav a partir do arquivo asf de audiência.
def gera_wav(path_arquivo):
    print ('Gerando arquivo wav. Aguarde...')
    videoclip = mp.VideoFileClip(path_arquivo)
    audio = videoclip.audio
    audio.write_audiofile('audiencia.wav')
    print ('Arquivo wav criado com sucesso!')

# Opção 2 - Obter o texto do arquivo wav com a ajuda do Google
def transcrever_google():
    print ('Iniciando a transcrição com a IA do Google. Aguarde...')
    try:
        r = sr.Recognizer()
        audio = sr.AudioFile('audiencia.wav')
        with audio as source:
            audio_file = r.record(source)
        resultado_google = r.recognize_google(audio_file, language='pt-BR')
        print(resultado_google)
        gera_texto (resultado_google, 'google')
    except:
        print('Ops... Algo deu errado!')
        print('Verifique o arquivo audiencia.wav ou o limite de 10 MB\n')


# Opção 3 - Obter o texto do arquivo wav com a ajuda do IBM Watson.
def transcrever_ibm():
    try:
        # Autenticação
        url, apikey = obtem_url_key()
        authenticator = IAMAuthenticator(apikey)
        stt = SpeechToTextV1(authenticator=authenticator)
        stt.set_service_url(url)

        # Extração do texto 
        print ('Iniciando a transcrição com a IA IBM Watson. Aguarde...')
        with open('audiencia.wav', 'rb') as f:
            resultado = stt.recognize(audio=f, content_type='audio/wav', model='pt-BR_Telephony', continuous=True).get_result()

        # Reúne os 'transcripts'
        texto = ''
        for r in resultado['results']:
            texto += r['alternatives'][0]['transcript'].rstrip()+'\n'
        print (texto)
        gera_texto(texto, 'ibm')
    except:
        print('Algo deu errado')
        print('Verifique o arquivo audiencia.wav ou sua autenticação no serviço IBM Watson')
    
# Opção 4 - Inserir chave e url do IBM Watson.
def salva_credenciais_ibm():
    url = input('Entre com a url: ')
    apikey = input ('Entre com a apikey: ')
    with open('info_login.txt' ,mode ='w') as f:
        f.write(url+'\n')
        f.write(apikey+'\n')
    print ('Arquivo de credenciais gerado com sucesso!')