import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega o dataset
df = sns.load_dataset('tips')

# Mostra as 5 primeiras linhas
print("Primeiras 5 linhas do dataset:")
print(df.head())

# Informações do dataset
print("\nInformações gerais:")
print(df.info())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())

# Geração do gráfico
print("\nGerando gráfico de boxplot de gorjetas por dia...")
sns.boxplot(x='day', y='tip', data=df)
plt.title("Distribuição de Gorjetas por Dia")
plt.savefig("boxplot_tips_por_dia.png")
plt.show()
