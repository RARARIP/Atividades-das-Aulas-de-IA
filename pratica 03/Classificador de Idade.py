"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).


"""

idade = int(input("Por favor, informe a sua idade: "))


if idade >= 0  e idade <= 12:
    categoria = "Criança"
elif idade >= 13 e idade <= 17:
    categoria = "Adolescente"
elif idade >= 18 e idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"
else:
    categoria = "Idade inválida"


print(f"Você é classificado como: {categoria}")