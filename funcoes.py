# This file is part of AudyPy 2.0 do Pimentel.
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
from pydub import AudioSegment
from natsort import natsorted
from tkinter import filedialog, Tk
from datetime import datetime

def gera_wav(path_arquivo):
    """Gera arquivo 'wav' a partir do arquivo 'asf' obtido no eSAJ."""
    if not os.path.exists('arquivos_gerados'):
        os.makedirs('arquivos_gerados')
    print ('Gerando o arquivo wav. Aguarde...')
    videoclip = mp.VideoFileClip(path_arquivo)
    audio = videoclip.audio
    audio.write_audiofile('./arquivos_gerados/audio_base.wav')
    print ('Arquivo wav criado com sucesso!')


def divide_wav (arquivo_wav):
    """Divide o arquivo wav em arquivos de 60 seg. com o uso da biblioteca pydub."""
    sound_file = AudioSegment.from_wav(arquivo_wav)
    #if not os.path.exists('arquivos_gerados'): 
    #    os.makedirs('arquivos_gerados')
    for num, pedaco in enumerate(sound_file[::60000]):
        with open(f'./arquivos_gerados/audio_{num}.wav', "wb") as f:
            pedaco.export(f, format="wav")
            print (f'Arquivo audio_{num}.wav gerado!')


def lista_wav (path = 'arquivos_gerados'):
    """Lista os arquivos 'wav' divididos usando a ordenação natural (biblioteca natsort)"""
    files = [f for f in os.listdir(path) if f.endswith('.wav') and f!='audio_base.wav'and os.path.isfile(os.path.join(path, f))]
    return(natsorted(files)) # ordenação não lexicográfica


def gera_nome():
    """Gera nome de arquivo texto único baseado na data/horário"""
    now = datetime.now().strftime('%Y%m%d%H%M')
    nome_arquivo_texto = 'texto_' + now + '.txt'
    return nome_arquivo_texto


def gera_texto (resultado, nome_arquivo_texto):
    """Exporta o resultado para o arquivo texto, gerando-o, caso ainda não exista."""
    
    if not (os.path.isfile(nome_arquivo_texto)):
        print (f'Gerando o arquivo {nome_arquivo_texto}...')
        with open(nome_arquivo_texto, mode ='w') as f:
            f.write(resultado)
    else:
        with open(nome_arquivo_texto, mode ='a') as f:
            print (f'Escrevendo o arquivo {nome_arquivo_texto}...')
            f.write(resultado)

# Menu principal

# Opção 1
def escolhe_arquivo():
    """Seleciona o arquivo ocultando a janela raiz"""
    root = Tk()
    root.withdraw()
    path_arquivo = filedialog.askopenfilename()
    gera_wav(path_arquivo)
    divide_wav('./arquivos_gerados/audio_base.wav')


# Opções 2 e 3
def transcrever_google(language, nome_arquivo_texto):
    """Obtém o texto do arquivo wav com a IA do Google"""
    arquivos_wav = lista_wav('arquivos_gerados')
    print ('Iniciando a transcrição com a IA do Google. Aguarde...')
    for arquivo in arquivos_wav:
        try:
            r = sr.Recognizer()
            audio = sr.AudioFile(f'./arquivos_gerados/{arquivo}')
            with audio as source:
                audio_file = r.record(source)
            resultado_google = r.recognize_google(audio_file, language=language)
            print(f'Texto de {arquivo}:\n{resultado_google}')
            gera_texto (resultado_google, nome_arquivo_texto)
        except:
            print('Ops... Algo deu errado!')
            print(f'Verifique o arquivo {arquivo} ou o limite de 10 MB de cada segmento\n')

         
# Opção 4
def remove_wav():
    """Deleta os arquivos 'wav' da pasta 'arquivos_gerados'."""
    wav_files = glob.glob('./arquivos_gerados/*.wav')
    for wav_file in wav_files:
        try:
            os.remove(wav_file)
            print (f'{wav_file} foi deletado com sucesso!')
        except OSError as e:
            print(f'Não consegui concluir a operação. Erro:{ e.strerror}')