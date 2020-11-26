#Programa que controla carteira
carteira = { "despesa": 0, "receita": 0, "emprestimo": 0 }

continuar = True 
while continuar:
  opcao = input("Qual o tipo? ").lower()
  valor = float(input("Valor: "))
  if opcao in carteira.keys():
    carteira[opcao] += valor #carteira[opcao] = carteira[opcao] + valor
  else:
    print("A opção informada é inválida!")
  print(carteira)
  continuar = input("Continuar? ") == "sim"

#Apresenta o saldo da carteira:
saldo = carteira["receita"] - (carteira["despesa"] + carteira["emprestimo"])
print("Saldo final:", saldo)
