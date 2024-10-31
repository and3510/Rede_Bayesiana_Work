# Exploração e Pré-processamento dos Dados

import pandas as pd

columns = ["age", "workclass", "fnlwgt", "education", "education_num", "marital_status",
           "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss",
           "hours_per_week", "native_country", "income"]

pegar_dados = pd.read_csv('./adult/adult.data', names=columns, sep=',\s*', engine='python')

teste_dados = pd.read_csv('./adult/adult.test', names=columns, sep=',\s*', engine='python', skiprows=1)


# print(pegar_dados)

# print(pegar_dados.shape)

# print(teste_dados)

# pegar_dados.info()
    
# pegar_dados.describe()

# pegar_dados.head()