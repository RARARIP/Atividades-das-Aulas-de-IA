"""
2- Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.


"""
import csv

dados_pessoas = [
    ["Renata", 30, "São Paulo"],
    ["Ana Carla", 55, "Rio de Janeiro"],
    ["Elizabeth", 75, "Brasília"]
]
nome_arquivo = input("Familia.csv")
try:
  with open(familia, mode='w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(["Nome", "Idade", "Cidade"])
    escritor_csv.writerows(dados_pessoas)
  print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'.")
