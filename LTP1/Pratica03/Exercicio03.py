#Recebe os coeficientes de uma equação de 2º e apresenta uma,  duas ou nenhuma das raízes reais que a equação pode possuir, apenas por bhaskara
A = float(input("Digite o primeiro termo: "))
B = float(input("Digite o segundo termo: "))
C = float(input("Digite o terceiro termo: "))

#Potência no Phyton - X elevado a Y = X**Y
delta = (B**2)-(4*A*C)

#Determina o número de raízes em função do valor do delta
if delta<0:
  print ("Não possui raízes reais")
elif delta>0:
  x1 = (-B+delta**0.5)/(2*A)
  x2 = (-B-delta**0.5)/(2*A)
  print ("As raízes são:", x1, x2)
else:
  x2 = (-B-delta**0.5)/(2*A)
  print ("A raíz é:", x2)
