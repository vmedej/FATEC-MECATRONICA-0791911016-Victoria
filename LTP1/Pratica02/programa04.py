#Operadores da divisão (/) e resto da divisão (%)
#divisao = 10/2
#resto = 10%2

#print ("Divisão:", divisao)
#print ("Resto:", resto)

#Ler um número  para ver se ele é par ou ímpar
numero = int(input("Digite um número: "))

#Calcula o resto da divisão por 2
resto = numero%2

#Analisa o valor do resto
if resto == 0:
  print ("O número é par")
else:
  print ("O número é impar")
