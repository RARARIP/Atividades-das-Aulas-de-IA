"""
4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.
"""

import requests
from datetime import datetime

def consultar_cotacao():
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").upper()

    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Código de moeda inválido ou não encontrado.")
            return

        cotacao = float(dados[chave]['ask'])
        maximo = float(dados[chave]['high'])
        minimo = float(dados[chave]['low'])
        timestamp = int(dados[chave]['timestamp'])
        data_hora = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        print(f"\nCotação do {moeda} em relação ao Real:")
        print(f"Valor atual: R$ {cotacao:.4f}")
        print(f"Valor máximo do dia: R$ {maximo:.4f}")
        print(f"Valor mínimo do dia: R$ {minimo:.4f}")
        print(f"Última atualização: {data_hora}")

    except requests.exceptions.RequestException:
        print("Falha na conexão ou erro ao acessar a API.")
    except ValueError:
        print("Erro ao processar os dados recebidos.")

if __name__ == "__main__":
    consultar_cotacao()