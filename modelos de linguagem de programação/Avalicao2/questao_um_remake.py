import re 

entrada_um = 'A1'
entrada_dois = 'A2B1'

obter_lista = r'^((?:[AB]{1}[12]{1})+)$'
obter_elemento = r'[AB]{1}[12]{1}'

def executar_bnf(expressao):
    expressao_entrada = re.findall(obter_lista, expressao) #retorna uma lista
    expressao_entrada = expressao_entrada[0] #pega a primeira string da lista , só há uma então atua como casting.

    #esse trecho inverterá a ordem dos elementos da lista.
    elementos_invertidos = []
    for elemento in re.findall( obter_elemento , expressao_entrada ):
        elementos_invertidos.insert(0,elemento)

    #esse trecho concatenará os elementos já invertidos.
    expressao_saida = str()
    for elemento in elementos_invertidos:
        expressao_saida+= elemento

    #retorna a expressão após executar a bnf.
    return expressao_saida

expressao_entrada = entrada_um
expressao_saida = executar_bnf(expressao_entrada)

print('entrada = {}'.format(expressao_entrada) )
print('saida = {}'.format(expressao_saida) )

expressao_entrada = entrada_dois
expressao_saida = executar_bnf(expressao_entrada)

print('entrada = {}'.format(expressao_entrada) )
print('saida = {}'.format(expressao_saida) )