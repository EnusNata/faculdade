#Questão 2  (1,0 ponto)

#Seja o trecho de código

#from functools import reduce 

#lstNumerosF = [10.01, 7.03, 2.23]
#lstNomes = ["casa", "google", "escola"]
#lstNumerosI = [7, 3, 9, 23]

#lstMapa = Adicione seu Código aqui(lstNumerosF))
#lstFiltro = Adicione seu Código aqui(lstNomes)
#lstReducao = Adicione seu Código aqui(lstNumerosI)

#print(lstMapa)
#print(lstFiltro)
#print(lstReducao)

#Implementar um programa que utilize, OBRIGATORIAMENTE, map x reduce x filter e funções lambda, de tal modo que:
#    a. Os valores da lstNumeros sejam elevados ao quadrado e tenham aproximação de três casas decimais
#    b. Sejam impressos apenas os elementos de lstNomes que tenham comprimento menor ou igual a 5.
#    c. Os valores de lstReducao sejam multiplicados entre si.
#O seu programa terá que produzir a seguinte saída:
#[100.2, 49.421, 4.973]
#['casa']
#4347

#Implementar um programa que utilize, OBRIGATORIAMENTE, map x reduce x filter e funções lambda, de tal modo que:

#a. Os valores da lstNumeros sejam elevados ao quadrado e tenham aproximação de três casas decimais

lstNumerosF = [10.01, 7.03, 2.23]

print( list( map( lambda numero: format(numero, '.3f') , list( map( lambda numero : numero ** 2 , lstNumerosF) ) ) ) )

#[100.2, 49.421, 4.973] errado
#[100.200, 49.421, 4.973] certo
#o numero de casas decimais se refere a quantidade de casas após a virgula.

#b. Sejam impressos apenas os elementos de lstNomes que tenham comprimento menor ou igual a 5.

lstNomes = ["casa", "google", "escola"]

print( list (filter( lambda nome: len( nome ) <= 5  , lstNomes ) ) )

#['casa'] correto

#c. Os valores de lstNumeros sejam multiplicados entre si.

lstNumerosI = [7, 3, 9, 23]

from functools import reduce

print( reduce( lambda valor_acumulado, numero_n : valor_acumulado * numero_n , lstNumerosI ) )

#4347 correto