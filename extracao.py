import requests
import pandas as pd
from io import StringIO

URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados?formato=csv"

response = requests.get(URL)
csv_text = response.text

print("CSV baixado com sucesso!")

# Carregar CSV informando o separador ; e parse_dates com 'data'
df = pd.read_csv(StringIO(csv_text), sep=';', parse_dates=['data'])

# Converter a coluna 'valor' de string com vírgula para float
df['valor'] = df['valor'].str.replace(',', '.').astype(float)

print(df.head())

df.to_csv("dados_selic_tratados.csv", index=False)
print("Arquivo CSV salvo com sucesso!")
