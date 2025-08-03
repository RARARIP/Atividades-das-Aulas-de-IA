"""
3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.

"""

import requests

def consultar_cep():
    cep = input("Digite o CEP (apenas números, sem traço): ").strip()
    

    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Certifique-se de digitar exatamente 8 números.")
        return
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        dados = response.json()
        
        if "erro" in dados:
            print("CEP não encontrado. Por favor, verifique o número digitado.")
        else:
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro: {dados.get('bairro', 'N/A')}")
            print(f"Cidade: {dados.get('localidade', 'N/A')}")
            print(f"Estado: {dados.get('uf', 'N/A')}")
            print(f"CEP: {dados.get('cep', 'N/A')}")
    except requests.exceptions.RequestException as e:
        print("Ocorreu um erro ao acessar o serviço. Tente novamente mais tarde.")
        print(f"Detalhes do erro: {e}")


consultar_cep()