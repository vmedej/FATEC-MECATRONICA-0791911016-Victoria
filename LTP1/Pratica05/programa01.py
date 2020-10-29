#Enunciado: Construa um programa que pergunte ao usuário uma quantidade de valores que ele deseja informar.
#Depois, leia todos esses valores, contando a quantidade deles que são pares e ímpares.
#Depois de ler todos os valores, exiba a quantidade de números pares e impares que foram informados.

quantidade = int(input("Informe a quantidade de valores: "))
contador = 0
quantidade_pares = 0
quantidade_impares = 0

while contador < quantidade:
  valor = int(input("Informe um valor: "))
  if valor % 2 == 0:
    quantidade_pares = quantidade_pares + 1
  else:
    quantidade_impares = quantidade_impares + 1
  contador = contador + 1

print("Números pares:", quantidade_pares)
print("Números impares:", quantidade_impares)
