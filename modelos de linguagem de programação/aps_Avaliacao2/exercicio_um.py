#Questão 1 (1,0 ponto)


#Seja a BNF abaixo:

#<SEQ> ::= <DIG><SEQ> | <DIG>
#<DIG> ::= 0|1

#    a) Implemente um programa em Python com a utilização da biblioteca re (Regex) que represente a BNF. 
#    b) Apresenta a saída do seu programa para as palavras: 001   e 1021

import re

# ^ $ a sequencia deve vir desde o inicio até o fim da string.
#[01] os unicos valores aceitos são 0 e 1.
#+ uma sequencia deve ter no minimo um digito 0 ou 1 e no maximo n.

sequencia = r'^[01]+$'

teste_sequencias_um   = r'001'
teste_sequencias_dois = r'1021'

print( re.findall(sequencia, teste_sequencias_um ) )
print( re.findall(sequencia, teste_sequencias_dois ) )

#aparentemente funciona, porem teste mais.

#fase de testes

teste_sequencias = r'1', r'2' , r'10' , r'01' , r'11' , r'20' , r'200' , r'10001' , r'00001'
print()
for teste_sequencia in teste_sequencias:
    print( re.findall( sequencia, teste_sequencia ) )
print()

#funcionou gostoso.