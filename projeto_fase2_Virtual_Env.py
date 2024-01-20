# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 18:35:05 2024

@author: Acer
"""
!pip install virtualenv
!mkdir projeto_coderhouse
%cd projeto_coderhouse
!virtualenv venv
!venv\Scripts\activate

!pip install plyer
import requests
import pandas as pd
from plyer import notification

def baixar_dados_bancos(url):
    resposta = requests.get(url)

    if resposta.ok:
        dados_bancos = resposta.json()
        return dados_bancos
    else:
        notification.notify(
            title='Erro de integração na API',
            message='Não foi possível baixar os dados',
            app_name='erro',
            timeout=10
        )
        return None

# URL da API dos bancos brasileiros
url_api_bancos = 'https://brasilapi.com.br/api/banks/v1'

dados_bancos = baixar_dados_bancos(url_api_bancos)

if dados_bancos:
    # Criando DataFrame Bruto com as colunas selecionadas
    df_bancos = pd.DataFrame(dados_bancos)[['ispb','name', 'code', 'fullName']]

    # Exibindo as primeiras linhas de cada DataFrame
    print("DataFrame criado com sucesso:")
    display(df_bancos.head(5))

    # Modificando o nome de uma das colunas dos dfs
    df_bancos_modificado1 = df_bancos.rename(columns={'ispb': 'codigo_ispb'})
    display(df_bancos_modificado1.head(5))

    # Verificando os tipos de dados de cada coluna no DataFrame
    print(df_bancos_modificado1.dtypes)

    # Modificando o tipo de dado
    # Convertendo coluna 'codigo_ispb' para string
    df_bancos_modificado1['codigo_ispb'] = df_bancos_modificado1['codigo_ispb'].astype(str)

    # Convertendo coluna 'name' para string
    df_bancos_modificado1['name'] = df_bancos_modificado1['name'].astype(str)

    # Convertendo coluna 'fullName' para string
    df_bancos_modificado1['fullName'] = df_bancos_modificado1['fullName'].astype(str)

    # Verificar informações sobre espaços nulos no DataFrame
    df_bancos_modificado1.info()

    # Remover linhas com valores NaN na coluna 'code'
    df_bancos_modificado2 = df_bancos_modificado1.dropna(subset=['code'])

    # Convertendo a coluna code para Int
    df_bancos_modificado2['code'] = df_bancos_modificado2['code'].astype(int)

#Verificando se agora temos apenas as linhas com dados
df_bancos_modificado2.info()
display(df_bancos_modificado2.head(10))

df_bancos.to_excel( 'base_bruta_api.xlsx', index = False)
df_bancos_modificado1.to_excel('base_primeira_modificacao.xlsx', index = False)
df_bancos_modificado2.to_excel('base_segunda_modificacao.xlsx', index = False)

from google.colab import files

files.download('base_bruta_api.xlsx')
files.download('base_primeira_modificacao.xlsx')
files.download('base_segunda_modificacao.xlsx')