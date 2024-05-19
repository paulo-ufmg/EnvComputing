"""
8. (SUBS) Programa busca um padrão em uma sequência de DNA
Entrada: 
    GATATATGCATATACTT   #sequencia 
    ATAT                #padrão
Saída: 2 4 10
"""
import os
import re
from Bioclass import Bioprof

nome_arquivo = 'dados' + os.sep + 'arquivo_L02E08_string_de_dna.txt'
seq = Bioprof()

seq.leiaArquivoFasta(nome_arquivo)

padrao = seq.get_sequencia("p")
sequencia = seq.get_sequencia("s")
#print("Padrao:",padrao)
#print("Sequencia:",sequencia)
#primeiro método busca string
#============================
#    n = -1
#    posicao = []
#    while True:
#    n += 1
#    n = sequencia.find(padrao,n)
#    if(n == -1):
#        break
#    posicao.append(n+1)    
#    print(posicao)


#Segundo método usando expressão regular
#=======================================
n = 0
posicao = []
while True:
    encontrei = re.compile(padrao).search(sequencia,n)
    if encontrei:
        n = encontrei.start() + 1
        posicao.append(n)
    else: break    
print(posicao)
