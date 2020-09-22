#Lê três valores, diz qual é o maior e o menor entre eles e diz qual é a média entre eles

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
valor3 = int(input("Informe o terceiro valor: "))

#Encontra o maior valor 
if valor1>=valor2 and valor1>=valor3:
  maior = valor1
elif valor2>=valor1 and valor2>=valor3:
  maior = valor2
else:
  maior = valor3
print ("O maior valor é:" ,maior)
  
#Encontra o menor valor 
if valor1<=valor2 and valor1<=valor3:
  menor = valor1
elif valor2<=valor1 and valor2<=valor3:
  menor = valor2
else:
  menor = valor3
print ("O menor valor é:" ,menor)

#Encontra a média
media = (valor1+valor2+valor3)/3
print ("A média entre os três valores é:" ,media)
