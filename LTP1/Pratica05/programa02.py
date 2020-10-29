#Guarda a somatoria dos valores informados
somatoria = 0
#Conta a quantidade de valores informados
contador = 0
#Guarda o maior valor informado
maior = 0
#Guarda o menor valor informado
menor = 0
#Constrói a lógica de repetição - enquanto se mantiver verdadeiro, repete o código
continuar = True

while continuar == True:
  valor = int(input("Informe o valor: "))
  #Adiciona o valor na somatoria
  #(somatoria += valor) é o mesmo que (somatoria = somatoria + valor)
  somatoria += valor 
  #Adiciona mais um na contagem
  #(contador += 1) é o mesmo que (contador = contador + 1)
  contador += 1
  #Para verificar se é  primeiro número informado
  if contador == 1:
    maior = valor
    menor = valor
  else:
    if valor > maior:
      maior = valor
    elif valor < menor:
      menor = valor
  #Verifica se o usuário deseja continuar
  continuar = input("Continuar? ") == 'sim'

media = somatoria/contador
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)
