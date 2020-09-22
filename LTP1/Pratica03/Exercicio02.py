#Recebe três números, determina se os três podem ou não serem usados como lados de um triângulo
lado1 = int(input("Informe o primeiro  valor: "))
lado2 = int(input("Informe o segundo  valor: "))
lado3 = int(input("Informe o terceiro  valor: "))

#Determina se os valores podem ou não serem usados como lados do triângulo

#Forma 1
if(lado1>0) and (lado2>0) and(lado3>0):
  if (lado1+lado2)>lado3 and (lado2+lado3)>lado1 and (lado3+lado1)>lado2:
    print ("Os valores são válidos")
else:
  print ("Os valores são inválidos")

#Forma 2
if(lado1>0) and (lado2>0) and(lado3>0) and (lado1+lado2)>lado3 and (lado2+lado3)>lado1 and (lado3+lado1)>lado2:
  print ("Os valores são válidos")
else:
  print ("Os valores são inválidos")
