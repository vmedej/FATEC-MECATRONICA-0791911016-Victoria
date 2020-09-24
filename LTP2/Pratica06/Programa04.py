#Lista de listas - Tabela
#Pede para o usuário informar uma quantidade de produtos e depois faz 
#a leitura dessa quantidade, lendo nome e valor de cada item

lista_de_compras = []

quantidade = int(input("Informe a quantidade de itens: "))

while len(lista_de_compras) < quantidade:
  nome = input("Informe o nome do produto: ")
  preco = float(input("Infome o preço do produto: "))
  lista_de_compras.append([nome, preco])
  print(lista_de_compras)

total = 0
#For  item passa por todos os itens dentro da lista
for item in lista_de_compras:
  print(item [0],"\t", item[1])
  total = total + item[1]
  
print("\nValor total:", total)
