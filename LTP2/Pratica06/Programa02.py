#Revisão de conceitos de lista 
def exibirstatusdalista(lista):
 valor_medio = sum(lista)/len(lista)
 maior_valor = max(lista)
 menor_valor = min(lista)
 lista.sort() 
 print("A média é:", valor_medio)
 print("O maior valor é:", maior_valor)
 print("O menor valor é:", menor_valor)
 print("Lista ordenada:", lista)

def leituralista(lista, quantidade):
  while len(lista) < quantidade:
    valor = float(input("Informe um valor: "))
    lista.append(valor)


#Programa principal
valores = []
quantidade = int(input("Informe uma quantidade: "))
leituralista(valores, quantidade)
exibirstatusdalista(valores)
