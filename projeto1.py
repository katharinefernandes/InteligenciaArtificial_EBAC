# -*- coding: utf-8 -*-
"""projeto1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kSr7cxUkPNrQcuOi5cWHIiimCPhMYjY5

# Etapa 1 - Entendimento do Problema 

## Melhorar a conversão de vendas a partir da análise de campanhas realizadas no Facebook.

# Etapa 2: Coleta de Dados

#### Você pode baixar esse conjunto de dados no site: https://www.kaggle.com/loveall/clicks-conversion-tracking

# Etapa 3: Análise, Interpretação e Visualização dos Dados

#### Importando as bibliotecas
"""

#Manipulação dos dados
import pandas as pd

#Visualização

#Machine Learning

"""#### Carregando os dados

"""

df = pd.read_csv("KAG_conversion_data.csv")

type(df)

"""#### Primeira Inspeção"""

df.head() # Lista por default as 5 primeiras linhas

df.tail() # Lista por default as 5 últimas linhas

df.columns

df.index # Quantidade de dados, inicio, final, contando de quanto em quanto

df.shape

linhas, colunas = df.shape

print(f"O numero de linhas eh {linhas}")

type(df)

ser_interest = df["interest"]

type(ser_interest)

df.info()

"""#### Dicionário dos dados



1.   ad_id - ID único para cada anúncio
2.   xyzcampaignid - ID associado a cada campanha publicitária da empresa XYZ
3.   fbcampaignid - ID associado a como o Facebook rastreia cada campanha.
4.   age - idade da pessoa a quem o anúncio é mostrado.
5.   gender - sexo da pessoa que deseja que o anúncio seja mostrado
6.   interest - código que especifica a categoria à qual pertence o interesse da pessoa (os interesses são mencionados no perfil público da pessoa no Facebook)
7.   Impression - o número de vezes que o anúncio foi mostrado.
8.   Clicks - número de cliques nesse anúncio.
9.   Spent - Valor pago pela empresa xyz ao Facebook, para exibir aquele anúncio.
10.  Total conversion - Número total de pessoas que fizeram perguntas sobre o produto depois de ver o anúncio.
11.  Approved conversion - Número total de pessoas que compraram o produto depois de ver o anúncio.
"""



"""#### Renomeando as Colunas"""



"""Informações Estatísticas

#### Dados Faltantes
"""



"""#### Outliers"""



"""#### Duplicatas"""



"""#### Matriz de Correlação"""



""""numero_exibicoes" e "conversao" estão mais correlacionados com "compras" do que "cliques_no_anuncio" e "valor_pago_anuncio".

#### Avaliando as Features (Colunas)
"""

















"""#### interesse - código que especifica a categoria à qual pertence o interesse da pessoa (os interesses são mencionados no perfil público da pessoa no Facebook)"""



"""#### valor_pago_anuncio - Valor pago pela empresa xyz ao Facebook, para exibir aquele anúncio."""



"""#### numero_exibicoes - o número de vezes que o anúncio foi mostrado."""



"""#### Pessoas que compraram (por idade/gênero)"""



"""# Etapa 4: Modelagem/Machine Learning"""



"""# Etapa 5: Avaliando o Modelo

"""

