#Métodos das strings
texto = "eu Não posso aCreditar em um Deus que não acrEdita em mim (da Quebrada, Linn. 2020)"

#Deixa a primeira letra maiúscula
print(texto.capitalize())

#Converte todas as letras para letras maiúsculas
print(texto.upper())

#Converte todas as letras para letras minúsculas
print(texto.casefold())

#Encontra o que nós pedimos
print(texto.find(","))

#Quantas vezes a palavra se repete no texto (a palavra tem que estar escrita da mesma forma todas as 
#vezes,se uma estiver maiúscula e a outra minúscula elas serão consideradas palavras diferentes)
print(texto.count("não"))

#Tem a mesma função do casefold (na linha 17 ele consegue contar todas as palavras, já que o texto foi
#todo passado para letras minúsculas)
texto_minusculo = texto.lower()
print(texto_minusculo)
print(texto_minusculo.count("não"))

#É o programa anterior (prog10) de forma mais pratica
texto_maiusculo = texto.upper()
print(texto_maiusculo)
print(texto_maiusculo.count(","))
print(texto_maiusculo[:texto_maiusculo.find(",")])
