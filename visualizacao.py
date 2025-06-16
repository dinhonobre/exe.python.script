import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Verifica se o nome do gráfico foi passado no argumento
if len(sys.argv) < 2:
    print("Uso: python visualizacao.py <nome-do-grafico>")
    sys.exit(1)

nome_grafico = sys.argv[1]

# Lê o CSV tratado
df = pd.read_csv("dados_selic_tratados.csv", parse_dates=['data'])

# Cria o gráfico
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12,6))
grafico = sns.lineplot(x='data', y='valor', data=df)
grafico.set_title("Taxa SELIC ao longo do tempo")
grafico.set_xlabel("Data")
grafico.set_ylabel("Valor (%)")
plt.xticks(rotation=45)

# Salva a figura no arquivo PNG com o nome passado como argumento
plt.tight_layout()
plt.savefig(f"{nome_grafico}.png")
print(f"Gráfico salvo como {nome_grafico}.png")
