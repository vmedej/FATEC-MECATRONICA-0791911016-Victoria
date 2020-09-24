#Revisão de conceitos de lista 
valores = []

quantidade = int(input("Informe uma quantidade: "))

while len(valores) < quantidade:
  valor = float(input("Informe um valor: "))
  valores.append(valor)

valor_medio = sum(valores)/len(valores)
maior_valor = max(valores)
menor_valor = min(valores)
valores.sort() 

print("A média é:", valor_medio)
print("O maior valor é:", maior_valor)
print("O menor valor é:", menor_valor)
print("Lista ordenada:", valores)
