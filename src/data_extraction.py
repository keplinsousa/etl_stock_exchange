# importando bibliotecas
import yfinance as yf
import pandas as pd

# variaveis 
papeis = ['ABEV3.SA', 'BBDC3.SA', 'ELET3.SA', 'ITSA4.SA', 'PETR4.SA', 'TOTS3.SA', 'TEND3.SA', 'MXRF11.SA', 'VALE3.SA', 'TAEE3.SA', 'VIVT3.SA']

# pegar a cotação dos ativos
def buscar_dados_ativos(simbolo):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period='1d', interval='1d')
    dados['simbolo'] = simbolo
    return dados

# concatenar os papeis
def buscar_todos_dados_ativos(ativos):
    todos_dados = []
    for simbolo in papeis:
        dados = buscar_dados_ativos(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)

dados_concatenados = buscar_todos_dados_ativos(papeis)

#print(buscar_dados_ativos('VIVT3.SA'))
#print(dados_concatenados)
print(type(dados_concatenados))

'''
# pegar dividendos
def buscar_dados_dividendos(simbolo):
    ticker = yf.Ticker(simbolo)
    dividendos = ticker.dividends
    dividendos['simbolo'] = simbolo
    return dividendos

# concatenar dividendos
def buscar_todos_dados_dividendos(dividendos):
    todos_dividendos = []
    for simbolo in papeis:
        dividendos = buscar_dados_dividendos(simbolo)
        todos_dividendos.append(dividendos)
    return pd.concat(todos_dividendos)

dados_concatenados_dividendos = buscar_todos_dados_dividendos(papeis)
print(dados_concatenados_dividendos)
'''