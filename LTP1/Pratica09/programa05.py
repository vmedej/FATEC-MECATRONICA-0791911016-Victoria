nome = input("Informe seu nome: ")
valor = float(input("Informe um valor: "))
numero_conta = input("Informe o número da conta: ")

validacao = input("String de validação: ")

nome_validacao, numero_conta_validacao = validacao.split(';')

if nome == nome_validacao and numero_conta == numero_conta_validacao:
  print("Os dados informados são válidados")
else:
  print("Os dados informados são incorretos")
