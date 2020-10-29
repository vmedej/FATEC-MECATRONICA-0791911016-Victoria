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
