#O programa deve ler o código do produto e consultar seu valor em uma 
#tabela de preços pré-definida, depois deve exibir o total do pedido para o usuário

def pegarpreco(codigo):
  #Índice == código do produto e conteúdo é igual ao seu valor
  lista_de_precos = [10, 15, 200, 50, 40, 80, 200]
  if codigo >= 0 and codigo < len(lista_de_precos):
    return lista_de_precos[codigo]
  else:
    return -1

codigo = int(input("Código: "))
print(pegarpreco(codigo))
