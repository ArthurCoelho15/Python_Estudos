# %%

import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv", delimiter=";")
transacoes.head()

# %%

def diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude-media)**2)


#idades = pd.Series([21,32,43,32,14,65,78,34,19])

# %%

# Fazendo uma agregação do IdCliente retornando Series de Qtd de trasações, soma de pontos, média de pontos e amplitude
summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
           .agg({
               "IdTransacao": ['count'],
               "QtdePontos": ["sum", "mean", diff_amp]
           })
)

# Renomeando as colunas do DataFrame
summary.columns = [
    "IdCliente",
    "qtdeTransacao",
    "totalPontos",
    "mediaPontos",
    "ampMeanDiff",
]

summary


# %%
