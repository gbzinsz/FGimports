
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

imagens_url = ['https://liravictor07.github.io/FormativaPY/PROJETO/img/dada.jpg']

# Criar uma pasta para armazenar as imagens baixadas
if not os.path.exists('IMAGENS_BAIXADAS'):
        os.makedirs('IMAGENS_BAIXADAS')

 # Fazer o download e salve as imagens na pasta
for idx, url_imagem in enumerate(imagens_url):
        response_imagem = requests.get(url_imagem)
        if response_imagem.status_code == 200:
            nome_arquivo_imagem = f'IMAGENS_BAIXADAS/imagem_{idx + 1}.jpg'
            with open(nome_arquivo_imagem, 'wb') as arquivo:
                arquivo.write(response_imagem.content)
        else:
            print(f'Falha ao baixar a imagem {idx + 1}')



