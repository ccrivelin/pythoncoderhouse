# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:07:04 2024

@author: Acer
"""
from google.colab import files
import pandas as pd

# Faz o upload do arquivo CSV
#uploaded = files.upload()

# Obtém o nome do arquivo carregado
#dados_residenciais = list(uploaded.keys())[0]

# Carrega o arquivo CSV em um DataFrame
#dados = pd.read_csv(dados_residenciais)

# Calcular o maior tamanho de casa por cidade
maior_tamanho_por_cidade = dados.groupby('city')['house_size'].max().sort_values(ascending= False).head(15)
display(maior_tamanho_por_cidade)

# Calcular o menor tamanho de casa por cidade e ordenar do menor para o maior
menor_tamanho_por_cidade = dados.groupby('city')['house_size'].min().sort_values(ascending = True).head(15)
display(menor_tamanho_por_cidade)

# Tamanho de casa medio por cidade
tamanho_medio_por_cidade = dados.groupby('city')['house_size'].mean().sort_values(ascending = False).head(15)
display(tamanho_medio_por_cidade)

# Calculo de % de missing values
# Contagem total de registros por cidade
contagem_total_por_cidade = dados.groupby('city').size()

# Contagem de valores ausentes para tamanho da casa por cidade
contagem_missing_por_cidade = dados[dados['house_size'].isnull()].groupby('city').size()

# Calcular a porcentagem de valores ausentes por cidade
percent_missing_values = (contagem_missing_por_cidade / contagem_total_por_cidade) * 100

# Criar uma nova coluna 'percent_missing_values' no DataFrame original
dados['percent_missing_values'] = dados['city'].map(percent_missing_values)

# Exibir as primeiras linhas do DataFrame com a nova coluna
print(dados.head())


# Calculando o price_max / acre_min

# Calcula o preço máximo por cidade
max_price_por_cidade = dados.groupby('city')['price'].max().reset_index()

# Calcula o acre_lot mínimo por cidade
min_acre_lot_por_cidade = dados.groupby('city')['acre_lot'].min().reset_index()

# Combinando os dois DataFrames calculados acima
resultado = pd.merge(max_price_por_cidade, min_acre_lot_por_cidade, on='city', how='left')

# Substitui 0 em acre_lot por -1
resultado['acre_lot'].replace(0, -1, inplace=True)

# Calcula a razão do preço máximo pelo acre_lot mínimo
resultado['max_price_by_min_acre_lot'] = resultado['price'] / resultado['acre_lot']

# Exibir as primeiras linhas do DataFrame resultado
display(resultado.head(15))