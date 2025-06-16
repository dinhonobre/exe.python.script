import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
from io import StringIO

# Verifica se o nome do gráfico foi passado como argumento
if len(sys.argv) < 2:
    print("Uso: python analise.py <nome-do-grafico>")
    sys.exit(1)

nome_grafico = sys.argv[1]

# === PARTE 1: Extração dos dados ===
print("Baixando dados da taxa SELIC...")

URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados?formato=csv"
response = requests.get(URL)
csv_text = response.text

# Lê os dados do CSV direto da resposta
df = pd.read_csv(StringIO(csv_text), sep=';', parse_dates=['data'])
df['valor'] = df['valor'].str.replace(',', '.', regex=False).astype(float)

# Salva o arquivo CSV tratado
df.to_csv("dados_selic_tratados.csv", index=False)
print("Arquivo dados_selic_tratados.csv salvo com sucesso.")

# === PARTE 2: Visualização dos dados ===
print("Gerando gráfico...")

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))
grafico = sns.lineplot(x='data', y='valor', data=df)
grafico.set_title("Taxa SELIC ao longo do tempo")
grafico.set_xlabel("Data")
grafico.set_ylabel("Valor (%)")
plt.xticks(rotation=45)
plt.tight_layout()

# Salva o gráfico com o nome passado via argumento
plt.savefig(f"{nome_grafico}.png")
print(f"Gráfico salvo como {nome_grafico}.png")
