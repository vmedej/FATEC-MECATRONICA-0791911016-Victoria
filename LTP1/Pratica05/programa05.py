#Enunciado: Escreva um programa que permita o usuário calcular a quantidade de notas de 200, 100, 50, 10, 5 e 1
#que ele precisa para formar um valor inteiro informado pelo usuário.
#Depois de informar um valor, o seu programa deve perguntar se o usuário deseja ou não continuar com a execução.

continuar = True

while continuar:
  valor = int(input("Informe o valor: "))
  n200 = valor // 200
  resto = valor % 200
  n100 = resto // 100
  resto = resto % 100
  n50 = resto // 50
  resto = resto % 50
  n10 = resto // 10
  resto = resto % 10
  n5 = resto // 5
  n1 = resto % 5
  print ("Notas de 200:", n200)
  print ("Notas de 100:", n100)
  print ("Notas de 50:", n50)
  print ("Notas de 10:", n10)
  print ("Notas de 5:", n5)
  print ("Notas de 1:", n1)
  continuar = input("\nContinuar? ") == "sim"
