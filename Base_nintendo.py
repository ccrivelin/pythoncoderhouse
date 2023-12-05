# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:58:01 2023

@author: Acer
"""

#Este programa é referente a aula 8 do curso de Python da Coderhouse
#Objetivo é fazer modificações na base de um arquivo Excel
#importando a base
import pandas as pd
best_selling = "C:\Users\Acer\Documents\SQL estudos\PYTHON CODERHOUSE\best-selling games consoles.xlsx"
base_nintendo = pd.read_excel(best-selling, sheet_name = consoles)
print(base_nintendo.head(15))

#trocando todos os NES por Nintendinho
base_nintendo['Console Name'] = base_nintendo['Console Name'].str.replace('NES','Nintendinho',case= False)
print(base_nintendo.head(15))

#este código modifica todos os nomes para letra maiúscula
base_nintendo['Console Name'] = base_nintendo['Console Name'].str.upper()
print(base_nintendo.head(15))

#este código filtra apenas consoles lançados após 2010 e traz os nomes sem duplicidade
consoles_apos2010 = base_nintendo[base_nintendo['Released Year']>2010]
consoles_apos2010 = consoles_apos2010['Console Name'].unique()
print(consoles_apos2010)

#Substituir os missing values pela string "missing"
print(base_nintendo.describe(include='all'))
base_nintendo.fillna("missing", inplace=True)
print(base_nintendo).describe(include='all')

#Filtrar consoles descontinuados a menos de 2 anos da data de release
consoles_descontinuados = base_nintendo[base_nintendo['Discontinuation Year'] - base_nintendo['Released Year'] <= -2]
print(consoles_descontinuados)