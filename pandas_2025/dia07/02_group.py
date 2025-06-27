# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", delimiter=";")
transacoes.head()

# %%
transacoes.groupby(by=["IdCliente"]).count()

# %%
transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()

# %%
# qtde_transacoes
# total_pontos
# pontos / transacoes

# Podemos fazer agregações no groupby, aqui agrupamos por clientes, mas quero ver a contagem, soma e média de algumas colunas
summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
                     .agg({
                         "IdTransacao": ['count'],
                         "QtdePontos": ['sum', 'mean']
                        }))

summary

# %%
summary[('QtdePontos','mean')]

# %%
summary.columns = ['IdCliente', 'QtdeTransacao', "totalPontos", "avgPontos"]
summary