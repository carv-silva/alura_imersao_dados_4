import pandas as pd
url = "https://gist.githubusercontent.com/tgcsantos/3bdb29eba6ce391e90df2b72205ba891/raw/22fa920e80c9fa209a9fccc8b52d74cc95d1599b/dados_imoveis.csv"
dados = pd.read_csv(url)
# print(dados.head()) # mostra as 5 primeiras linhas

# print(dados) # --> mostra quantas linhas e colunas tem o documento

print(dados.sample(10))
