soma = 0
contador = 0

while contador < 3:
  numero = int(input("Digite um número: "))
  soma = soma + numero
  contador = contador + 1

media = soma / 3
print("Valor médio:", media)
