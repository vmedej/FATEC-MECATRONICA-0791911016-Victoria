#Enunciado: Vamos escrever um programa que quebra uma senha numérica utilizando força bruta.
#Seu usuário deve informar uma senha numérica de 6 dígitos. Seu programa vai testar todos os valores de 000000 a 999999 para determinar qual é a senha do usuário.
#Ao encontrar, exiba o valor da senha para ele.

senha = int(input("Informe uma senha: "))
forca_senha = 0

while forca_senha <= 999999:
  if forca_senha == senha:
    break
  forca_senha += 1 

if senha == forca_senha:
  print("Sua senha é:", forca_senha) 
else:
  print("Não foi possível quebrar a senha")
