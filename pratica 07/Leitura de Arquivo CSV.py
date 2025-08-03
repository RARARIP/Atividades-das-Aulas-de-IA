"""
3- Leitura de Arquivo CSV  
Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela. Para isso:

* Solicite ao usuário o nome do arquivo CSV a ser lido.  
* Utilize o módulo `csv` para abrir o arquivo e ler os dados.  
* Exiba cada linha completa como uma lista.  
* Trate erros como arquivo inexistente ou problemas na leitura.

Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.


"""
import csv
nome_arquivo = input("Imposto_de_renda.csv")
try:
  with open(imposto_de_renda, newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)
except FileNotFoundError:
    print("o arquivo não foi encontrado. Verifique o nome e tente novamente.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")