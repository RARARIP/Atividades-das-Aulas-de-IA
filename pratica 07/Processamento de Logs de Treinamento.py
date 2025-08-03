"""
1- Processamento de Logs de Treinamento  
Crie um programa que analisa um arquivo CSV contendo dados de execução de um processo de treinamento. O programa deve:

* Solicitar ao usuário o nome do arquivo CSV (ex: logs_treinamento.csv).  
* Ler os dados usando a biblioteca `pandas`.  
* Calcular a média e o desvio padrão da coluna `tempo_execucao`.  
* Exibir os resultados com duas casas decimais.  
* Tratar erros como arquivo inexistente ou formatação incorreta.

Dica: Use `df['coluna'].mean()` e `df['coluna'].std()` para obter os resultados estatísticos.

"""

import pandas as pd

def analisar_treinamento():

    arquivo = input("Por favor, informe o nome do arquivo CSV (ex: logs_treinamento.csv): ")

    try:
        df = pd.read_csv(arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado. Verifique o nome e tente novamente.")
        return
    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo '{arquivo}' está vazio ou possui formato incorreto.")
        return
    except pd.errors.ParserError:
        print(f"Erro: Houve um problema ao interpretar o arquivo '{arquivo}'. Verifique se o formato está correto.")
        return
    if 'tempo_execucao' not in df.columns:
        print("Erro: A coluna 'tempo_execucao' não foi encontrada no arquivo.")
        return
    media = df['tempo_execucao'].mean()
    desvio = df['tempo_execucao'].std()

    print(f"Média de tempo de execução: {media:.2f}")
    print(f"Desvio padrão de tempo de execução: {desvio:.2f}")

analisar_treinamento()