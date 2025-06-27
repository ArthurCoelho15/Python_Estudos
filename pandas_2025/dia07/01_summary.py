# %%
import pandas as pd

# Criando uma lista
idades = [32,44,12,54,67,32,23,34,32,12,45,43,28,73,29]
# Transformando a lista em uma série
idades = pd.Series(idades)

# FUNÇÕES DE AGREGAÇÃO -> Devolvem um Valor, caso filtre mais de uma devolve uma Série, apenas o describe devolve um DataFrame

# Soma
idades.sum()
# Valor mínimo
idades.min()
# Valor máximo
idades.max()
# Valor médio, para valores 1 e 0 podemos utilizar a média como a frequência de ocorrência do 1, ou seja, proporção.
idades.mean()
# Contagem de valores
idades.count()
# Agregação de estatísticas (contagem, média aritimética, desvio padrao, quartis, valor mínimo e máximo)
idades.describe()


# %%

# Importando os dados do DataSet Clientes.csv
clientes = pd.read_csv("../data/clientes.csv", delimiter=";")
clientes

# %%

# Aqui só vai mostrar o primeiro output que botamos, no caso soma.

# Soma dos valores em 'FlTwitch'
clientes["FlTwitch"].sum()
# Média dos valores em 'FlTwitch'
clientes["FlTwitch"].mean()

# %%

# Fazendo o filtro de forma manual - Podemos criar um filtro para pegar apenas as colunas que tem valor (diferente de object, ou seja, float e int)
redes_sociais = ["FlEmail","FlTwitch","FlYouTube","FlBlueSky","FlInstagram"]
clientes[redes_sociais].sum()

# %%

# Fazendo o filtro de forma automatica - Podemos criar um filtro para pegar apenas as colunas que tem valor (diferente de object, ou seja, float e int)
num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.tolist()
clientes[num_columns].mean()

# %%

# DataFrame com as Estatísticas das colunas numéricas
clientes[num_columns].describe()

# %%

# DataFrame com as Estatísticas das colunas 'FlTwitch' e 'FlEmail'
clientes[["FlTwitch", "FlEmail"]].describe()
# %%
