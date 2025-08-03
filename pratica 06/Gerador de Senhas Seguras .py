"""

1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.


"""
import random
import string
def gerar_senha(tamanho):
caracteres = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>/?"
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
return senha
def main():
  while True:
    try:
      quantidade = int(input("Digite a quantidade de caracteres para a senha: "))
      if quantidade <= 0:
          print("Digite um número positivo.")
          continue
      break
    except ValueError:
       print("Informe um número válido.")
senha_gerada = gerar_senha(quantidade)
print(f"A senha é: {senha_gerada}")
if __name__ == "__main__":
   main()