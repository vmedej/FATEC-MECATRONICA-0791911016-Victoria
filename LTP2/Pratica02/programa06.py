#Determinar se um número inteiro é par ou impar

numero = int(input("Digite um numero: "))

#Calcula o resto da divisao de numero por 2

resto = numero % 2

#Condição

if resto == 0:
  print("\nO numero eh par!")
 
else:
  print("\nO numero eh impar!")
