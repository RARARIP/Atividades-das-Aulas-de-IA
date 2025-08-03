"""
3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".  

"""


import re

def verificar_forca_senha(senha):
    if len(senha) < 8:
        return "fraca"
    if not re.search(r"\d", senha):
        return "fraca"
    return "forte"

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == "sair":
        print("Encerrando o programa. Até mais!")
        break
    forca = verificar_forca_senha(senha)
    if forca == "forte":
        print("Sua senha é forte! Parabéns!")
        break
    else:
        print("Senha fraca. Tente novamente.")