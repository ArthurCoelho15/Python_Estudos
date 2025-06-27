# %%

hl = "hello world"
hl
# %%
import pandas as pd

lista = [
    1, 5 , 2, 8,3,2 ,4 ,5
]

series_lista = pd.Series(lista)
series_lista
df = pd.DataFrame()
df["lista"] = series_lista
df

# %%

