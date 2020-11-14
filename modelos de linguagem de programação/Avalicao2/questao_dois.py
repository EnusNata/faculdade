#Questão 2 (2,0 pontos)

#Implemente um programa em Python que receba uma lista de nomes 
#(use lista = [‘casa’, ‘DIA’, ‘liVRO’, ‘dado’]) 
#e utilizando as funções lambda, map e filter faça:

lista = [ 'casa' , 'DIA' , 'liVRO' , 'dado' ]

#a. Listar todas as palavras que iniciem com uma determinada letra.
#Por exemplo, com ‘d’, não distinguir entre maiúsculas e minúsculas, no caso vai exibir:
#[‘DIA’, ‘dado’]

#com a letra inicial especificada.

letras_iniciais = ['d','D']

print( list( filter( lambda palavra: palavra[0] in letras_iniciais , lista) ) )

#com a letra inicial especificada.


#b. Transformar as palavras de tal modo que apenas a primeira letra seja maiúscula. 
#No caso do exemplo, vai exibir:
#[‘Casa’, ‘Dia’, ‘Livro’, ‘Dado’]

# o método capitalize de objetos string efetua essa operação.
print( list( map( lambda palavra: palavra.capitalize() , lista ) ) )