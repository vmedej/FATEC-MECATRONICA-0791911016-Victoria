#Enunciado: Escreva um programa que permita o usuário informar o seu nome e o seu poder de luta (ki).
#Informe o quando este personagem está acima ou abaixo do poder de luta do Goku (8000).
#O seu programa deve ficar sendo executado até que o nome Kuririn seja informado.

continuar = True

while continuar == True:
  nome = input("Informe o seu nome: ")
  if nome == "kurikin":
    continuar = False
  else:
    ki = int(input("Informe o seu poder de luta: "))
    if ki > 8000:
      print("Mais forte que o Goku")
    else:
      print("Vai treinar")
