"""
4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final.
"""

import datetime

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = datetime.datetime.now().year
idade_anos = ano_atual - ano_nascimento
idade_dias = idade_anos * 365

print(f"Sua idade aproximada em dias é: {idade_dias} dias.")