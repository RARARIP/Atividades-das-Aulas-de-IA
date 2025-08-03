"""
1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.  
O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso.


"""

num1 = float(input("Digite o primeiro nA0mero: "))
num2 = float(input("Digite o segundo nA0mero: "))
operacao = input("Digite uma operaA&A#o desejada (+, -, *, /)")

if operacao == '+':
 resultado = num1 + num2
elif operacao == '-':
 resultado = num1 - num2
elif operacao == '*':
 resultado = num1 * num2
elif operacao == '/':
 if num2 == 0:
  print("Erro: divisA#o por zero nA#o (C) possA$vel.")
continue
resultado = num1 / num2
else:
print("Erro: operaA&A#o invA!lida")

