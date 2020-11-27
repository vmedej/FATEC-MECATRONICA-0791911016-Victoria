def lerNumerosPositivos():
  continuar = True
  while continuar == True:
    numero = int(input("Informe um valor: "))
    continuar = numero < 0
  return numero

def somarDoisNumeros(numero1, numero2):
  return numero1 + numero2

def exibir_saida_formatada(numero1, numero2, resultado):
  print("A soma de {} com {} é igual a: {}".format(numero1, numero2, resultado))
  print("A soma de %i com %ié igual a: %i" % (numero1, numero2, resultado))

primeiro_valor = lerNumerosPositivos()
segundo_valor = lerNumerosPositivos()
resposta = somarDoisNumeros(primeiro_valor, segundo_valor)
exibir_saida_formatada(primeiro_valor, segundo_valor, resposta)
