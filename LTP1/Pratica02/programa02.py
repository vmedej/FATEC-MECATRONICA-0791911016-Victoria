#Cria uma variavel para guardar a senha_secreta
senha_secreta = "123456"

#Pede ao usuário uma senha e a valida com a senha secreta
#Cria uma variavel para guardar a senha que o usuário digita
senha = input("Informe sua senha: ")

#Verifica se a senha do usuário esta compile

if senha == senha_secreta:
  print("Bem vindo")

if senha != senha_secreta:
  print ("Senha incorreta")
