#Função (passo dois)
def funcao(lista):
  resposta = []
  media = sum(lista)/len(lista)
  for valor in lista:
    if valor > media:
      resposta.append(valor)
  return resposta

#Criar uma lista vazia(passo um)
valores = []
quantidade = int(input("Informe a quantidade de valores: "))
while len(valores) <  quantidade:
  valor = float(input("Informe o valor:"))
  valores.append(valor)

#Mostrar resultados do programa (passo três)
print(funcao(valores))
