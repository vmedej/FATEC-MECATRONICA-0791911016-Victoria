menor_preco = float("inf")
melhor_loja = ""

continuar = True
while continuar == True:
  preco = float(input("Preço: "))
  loja = input("Nome da loja: ")
  if preco < menor_preco:
    menor_preco = preco
    melhor_loja = loja
  continuar = input("Deseja continuar? ").lower() == "sim"

print("A melhor loja é %s, com o valor de R$%.2f" % (melhor_loja, menor_preco))
