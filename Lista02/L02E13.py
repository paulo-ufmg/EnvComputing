"""
Program junta vários arquivos fasta em um único arquivo com o nome all.fasta
Ele busca os arquivos a serem mesclados dentro de outro arquivo
"""
#entrada:Ler um arquivo "arquivo_L02E13_entrada.txt"
#-------------------
"""
Rosalind_10.fasta
Rosalind_12.fasta
Rosalind_15.fasta
"""

#saida: Um arquivo “all.fasta” contendo:
#---------------------------------------
"""
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGC
GTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
"""

import os
from Bioclass import Bioprof
arqs = []
#Lendo os nomes de arquivos a serem mesclados
with open ("dados"+ os.sep + "arquivo_L02E13_entrada.txt", "r") as arq:
    while True:
        line = arq.readline()
        if not line: break #interrompe ao final do arquivo
        if line.strip() == "": continue  # Ignorar linhas em branco
        arqs.append(line.strip("\n"))

seq = Bioprof()
for n in arqs:
    seq.leiaArquivoFasta(n)

with open ("all_fasta", "w") as arq:
    for s in seq.get_seqs():
        arq.write(">"+s+"\n")
        arq.write(seq.get_sequencia(s)+"\n")
