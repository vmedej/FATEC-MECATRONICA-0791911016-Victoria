#Usuário informa duas listas, o programa junta as duas e exibe uma terceira lista

lista_1 = []
lista_2 = []
lista_3 = []

#Perguntar quantos valores as listas terão e arrumar uma forma de receber esse valor
quantidade_na_lista_1 = int(input("Quantos valores terá a lista 1? "))

#Enquanto o comprimento da lista 1 for  menor que a lista, o while roda, o len conta a quantidade de elementos existentes na lista
while len(lista_1)<quantidade_na_lista_1:
  valor = int(input("Valor: "))
  #Adicionar no final da lista
  lista_1.append(valor)
  print(lista_1)
  print("Itens na lista:", lista_1)

quantidade_na_lista_2 = int(input("\nQuantos valores terá a lista 2? "))

while len(lista_2)<quantidade_na_lista_2:
  valor = int(input("Valor: "))
  lista_2.append(valor)
  print(lista_2)
  print("Itens na lista:", lista_2)
  
#Juntar as duas listas e transforma-las em uma terceira lista
lista_3 = lista_1+lista_2
print("\n", lista_3)
