# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:09:30 2023

@author: Acer
"""
#importando o arquivo excel

import pandas as pd
best_selling = "C:\Users\Acer\Documents\SQL estudos\PYTHON CODERHOUSE\best-selling games consoles.xlsx"
base_nintendo = pd.read_excel(best-selling, sheet_name = consoles)
print(base_nintendo.head(15))

#Contar quantos consoles tem na base por Company
contagem_empresas = base_nintendo.groupby("Company").agg({"Company": 'count'}).rename(columns={"Company": "Número de Consoles"})
print(contagem_empresas)

#Ordenar o resultado de forma decrescente de consoles
contagem_empresas = contagem_empresas.sort_values(by='Número de Consoles', ascending=False)
print(contagem_empresas)

#Adicionar a coluna Market Value presente no arquivo company.txt

# Carregando o arquivo .txt 'Company.txt'
company = pd.read_csv("C:\Users\Acer\Documents\SQL estudos\PYTHON CODERHOUSE\Company.txt", delimiter=',')

# Mesclando as informações de 'Market Value' com 'contagem_empresas' pelo nome da empresa (Company)
contagem_empresas = contagem_empresas.merge(company, on='Company', how='left')

# Exibindo o DataFrame resultante
print(contagem_empresas)

#Respondendo a pergunta: Qual o valor médio de Market Value por console?
contagem_empresas['Valor Médio de Market Value'] = (contagem_empresas['Market Value'] / contagem_empresas['Número de Consoles']).round(2)
print(contagem_empresas)

