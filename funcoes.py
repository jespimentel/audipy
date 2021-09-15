# This file is part of AudyPy 1.0 do Pimentel.
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

import os
import glob
import moviepy.editor as mp
import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pydub import AudioSegment
from natsort import natsorted

def gera_texto (resultado, ia):
    """Exporta o resultado para o arquivo texto, gerando-o, caso ainda não exista."""
    nome_arquivo = 'texto_' + ia + '.txt'
    if not (os.path.isfile(nome_arquivo)):
        print (f'Gerando o arquivo {nome_arquivo}...')
        with open(nome_arquivo, mode ='w') as f:
            f.write(resultado)
    else:
        with open(nome_arquivo, mode ='a') as f:
            print (f'Escrevendo o arquivo {nome_arquivo}...')
            f.write(resultado)

def obtem_url_key ():
    """Obtém informações de login do IBM Watson gravadas em arquivo txt."""
    try:
        f = open('info_login.txt', 'r')
        url = str(f.readline().replace('\n', ''))
        apikey = str(f.readline().replace('\n', ''))
        print ('A informação de login do IBM Watson foi lida com sucesso!')
        return url, apikey
    except:
        print('Ops... Algo deu errado com o arquivo info_login.txt!\n')

def divide_wav (arquivo_wav):
    """Divide o arquivo wav em arquivos de 60 seg. com o uso da biblioteca pydub."""
    sound_file = AudioSegment.from_wav(arquivo_wav)
    if not os.path.exists('arquivos_gerados'): 
        os.makedirs('arquivos_gerados')
    for num, pedaco in enumerate(sound_file[::60000]):
        with open(f'.\\arquivos_gerados\\audiencia_{num}.wav', "wb") as f:
            pedaco.export(f, format="wav")
            print (f'Arquivo audiencia_{num}.wav gerado!')

def lista_wav (path = 'arquivos_gerados'):
    """Lista os arquivos 'wav' divididos usando a ordenação natural (biblioteca natsort)"""
    files = [f for f in os.listdir(path) if f.endswith('.wav') and f!='audiencia.wav'and os.path.isfile(os.path.join(path, f))]
    return(natsorted(files)) # ordenação não lexicográfica

# Menu principal
# Opção 1
def gera_wav(path_arquivo):
    """Gera arquivo 'wav' a partir do arquivo 'asf' obtido no eSAJ."""
    if not os.path.exists('arquivos_gerados'):
        os.makedirs('arquivos_gerados')
    print ('Gerando o arquivo wav. Aguarde...')
    videoclip = mp.VideoFileClip(path_arquivo)
    audio = videoclip.audio
    audio.write_audiofile('.\\arquivos_gerados\\audiencia.wav')
    print ('Arquivo wav criado com sucesso!')

# Opção 2 
def transcrever_google():
    """Obtém o texto do arquivo wav com a IA do Google"""
    arquivos_wav = lista_wav('arquivos_gerados')
    print ('Iniciando a transcrição com a IA do Google. Aguarde...')
    for arquivo in arquivos_wav:
        try:
            r = sr.Recognizer()
            audio = sr.AudioFile(f'.\\arquivos_gerados\\{arquivo}')
            with audio as source:
                audio_file = r.record(source)
            resultado_google = r.recognize_google(audio_file, language='pt-BR')
            print(resultado_google, arquivo)
            gera_texto (resultado_google, 'google')
        except:
            print('Ops... Algo deu errado!')
            print(f'Verifique o arquivo {arquivo} ou o limite de 10 MB de cada segmento\n')

# Opção 3
def transcrever_ibm():
    """ Obtém o texto do arquivo wav com a ajuda da IA do IBM Watson."""
    arquivos_wav = lista_wav('arquivos_gerados')
    print ('Iniciando a transcrição com a IA da IBM. Aguarde...')
    for arquivo in arquivos_wav:
        try:
            # Autenticação
            url, apikey = obtem_url_key()
            authenticator = IAMAuthenticator(apikey)
            stt = SpeechToTextV1(authenticator=authenticator)
            stt.set_service_url(url)

            # Extração do texto 
            with open(f'.\\arquivos_gerados\\{arquivo}', 'rb') as f:
                resultado = stt.recognize(audio=f, content_type='audio/wav', model='pt-BR_Telephony', continuous=True).get_result()

            # Reúne os 'transcripts'
            texto = ''
            for r in resultado['results']:
                texto += r['alternatives'][0]['transcript'].rstrip()+'\n'
            print (texto)
            gera_texto(texto, 'ibm')
        except:
            print(f'Algo deu errado com o arquivo {arquivo}')
            print('Verifique o arquivo ou a sua autenticação no serviço IBM Watson')
        
# Opção 4
def salva_credenciais_ibm():
    """Grava o arquivo de credenciais (chave e url) do IBM Watson."""
    url = input('Entre com a url: ')
    apikey = input ('Entre com a apikey: ')
    with open('info_login.txt' ,mode ='w') as f:
        f.write(url+'\n')
        f.write(apikey+'\n')
    print ('Arquivo de credenciais gerado com sucesso!')

# Opção 5
def remove_wav():
    """Deleta os arquivos 'wav' da pasta 'arquivos_gerados'."""
    wav_files = glob.glob('.\\arquivos_gerados\\*.wav')
    for wav_file in wav_files:
        try:
            os.remove(wav_file)
            print (f'{wav_file} foi deletado com sucesso!')
        except OSError as e:
            print(f'Não consegui concluir a operação. Erro:{ e.strerror}')
