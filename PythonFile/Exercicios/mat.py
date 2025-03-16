from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title('Nominal GDP')

plt.ylabel('Billions of $')
plt.show()


# --------------------------

movies = ["Tumulo dos vagalumes", "flow", "castelo encantado", "soul"]
num_oscars = [5, 2, 1, 3]

plt.title("Meus filmes favoritos")

plt.bar(range(len(movies)), num_oscars)

plt.ylabel("# de premiações")

plt.xticks(range(len(movies)), movies)

plt.show()

#---------------------------

movies = ["Tumulo dos vagalumes", "flow", "castelo encantado", "soul"]
num_oscars = [5, 2, 1, 3]

# Criando o gráfico de barras
plt.title("Meus filmes favoritos")
bars = plt.bar(range(len(movies)), num_oscars, color="skyblue")

# Adicionando data labels nas barras
plt.bar_label(bars, fmt='%d', padding=5)

# Adicionando rótulos e título
plt.ylabel("# de premiações")
plt.xticks(range(len(movies)), movies)

# Exibir o gráfico
plt.show()
