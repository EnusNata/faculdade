#Questão 4   (1,0 ponto)
#Seja a Backus-Naur Form (BNF):
#<exp> ::= <exp> + <exp> | <term>
#<term> ::= <term> * <term> | <factor>
#<factor> ::= ( <exp> ) | <digit>
#<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 

#Implemente um programa em Python com a utilização da biblioteca re (Regex), ou nltk que represente a BNF.
#Além do programa, mostre a saída do programa para as seguintes entradas:
#   a. 1+3*5
#   b. (1+3)*5

import re

pegar_parenteses_internos = r'[(]{1}[^\(\)]+[)]{1}'
pegar_multiplicacao = r'\d+\*\d+'
pegar_soma = r'\d+\+\d+'

entrada_um = r'1+3*5'
entrada_dois = r'(1+3)*5'

#poderia ter feito de maneira muito mais facil, usando apenas eval nos parenteses internos,
#porem, eu preferi utilizar um representação mais fiel, desde a prioridade de operadores até 
#a recursão dos parenteses , que nos leva de volta a <exp> , no caso resolver_expressao. 

def resolver_parenteses(expressao):
    expressao_resolvida = expressao

    while re.findall( pegar_parenteses_internos , expressao_resolvida ):

        lista_parenteses = re.findall( pegar_parenteses_internos , expressao_resolvida )

        parenteses_interno = lista_parenteses[0]
        expressao_parenteses_interno = parenteses_interno[1:-1] #remove o parenteses para resolver a expressao.
        resultado_parenteses_interno = resolver_expressao(expressao_parenteses_interno)

        expressao_resolvida = expressao_resolvida.replace( parenteses_interno, str(resultado_parenteses_interno), 1 )
    return expressao_resolvida


def resolver_multiplicacao(expressao):
    expressao_resolvida = expressao
    
    while re.findall( pegar_multiplicacao , expressao_resolvida ):
        
        #esse retorno é uma lista.
        multiplicacoes = re.findall( pegar_multiplicacao , expressao_resolvida )

        #ao chegar nesse modulo todas as multiplicacao devem possuir mesma prioridade.
        operacao_multiplicacao = multiplicacoes[0]
        resultado_multiplicacao =  eval(operacao_multiplicacao)

        #devemos resolver uma operacao, substituí-la
        expressao_resolvida = expressao_resolvida.replace(operacao_multiplicacao, str(resultado_multiplicacao), 1)
    return expressao_resolvida

def resolver_soma(expressao):
    expressao_resolvida = expressao

    while re.findall( pegar_soma , expressao_resolvida ):
        
        somas = re.findall( pegar_soma , expressao_resolvida )

        operacao_soma = somas[0]
        resultado_soma = eval(operacao_soma)

        expressao_resolvida = expressao_resolvida.replace( operacao_soma, str(resultado_soma) , 1) 
    return expressao_resolvida

def resolver_expressao(expressao):

    resultado_parenteses = resolver_parenteses(expressao)

    resultado_multiplicacao = resolver_multiplicacao(resultado_parenteses)

    resultado_soma = resolver_soma(resultado_multiplicacao)

    resultado_final = resultado_soma

    return resultado_final

print(resolver_expressao(entrada_um))
print(resolver_expressao(entrada_dois))