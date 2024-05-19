"""
Janela deslizante obtem a maior frequencia k-mer dado um valor de k

10. (BA1A) Podemos dizer que um padrão p é o mais frequente k-mer (onde k é o
tamanho de p) em um texto t se a quantidade de p em t for maior que todos os k-
mers. 

Por exemplo, "ACTAT" é um 5-mer mais freqüente em
"AAACTATACACTATAACTATT", e "ATA" é um 3-mer mais freqüente de
"CGATATATCCATAG". Considerando isso, faça um programa que leia um arquivo
contendo uma string de DNA s seguida de um inteiro k. O programa deve retornar
todos os k-mers mais frequentes em s, separados por espaço [10].
Exemplo entrada:
ACGTTGCATGTCGCATGATGCATGAGAGCT
4
Saída:
CATG GCAT
Classic Bioinformatics
"""
import os
import re
from Bioclass import Bioprof

nome_arquivo = 'dados' + os.sep + 'arquivo_L02E10_entrada.txt'
seq = Bioprof()
seq.leiaArquivoFasta(nome_arquivo)
#print(seq.get_seqs()) #veirificando as sequencias armazenadas
#print(seq.info) #veirificando comentários das sequencias
#Recebendo os dados de entrada
id_sequencia = "4mer" #Executado com "4mer" e testado com "5mer" e "3mer" com suas respectivas sequencias
sequencia = seq.get_sequencia(id_sequencia) 
k = int(seq.get_info(id_sequencia))

#obtendo os kmer da sequencia
kmers = []
for i in range(len(sequencia) -k + 1):
    kmer = sequencia[i:i + k]
    kmers.append(kmer)

#criando uma identidade unica dos kmer´s
ident = set(kmers) #Conjunto ident não possui kmer repetido

#Totalizando os k-mer obtidos
soma_kmer = []
for kmer in ident: #Contando a quantidade de kmer repetidos
    soma_kmer.append(kmers.count(kmer))

#Encontrando o k-mer mais frequente
kmers = list(ident) #retorna os elementos ident para uma lista
mais_frequente = max(soma_kmer)
print("Sequência: ",sequencia)
print("k-mer: ",k)
for i in range(len(ident)-1):
    if soma_kmer[i] == mais_frequente:
        print(kmers[i],end=" ")
    




