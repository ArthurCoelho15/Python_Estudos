# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", delimiter=";")
df.head()

# %%

def get_last_id(IdCliente):
    return IdCliente.split("-")[-1]

# %%

get_last_id("0033b737-8235-4c0f-9801-dc4ca185af00")

# %%
"""Forma 1: Não tão recomendada"""
id_novo = []

for i in df["IdCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["novo_id"] = id_novo
df.head()

# %%
"""Forma 2: Mais recomendada"""
id_novo2 = df["IdCliente"].apply(get_last_id) # Cada elemento da série será aplicado na função getlastID

df["novo_id2"] = id_novo2
df.head(10)
# %%
