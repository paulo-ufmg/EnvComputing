
#Programa que dividi todas as sequencias de um arquivo FASTA em arquivos separado, 
#usando o id da sequencia como nome do arquivo acrescido da extensão fasta.
#Entrada arquivo FASTA
#---------------------
"""
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGC
GTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
"""
#Arquivos de saída:
#-------------------
#Rosalind_10.fasta
#Rosalind_12.fasta
#Rosalind_15.fasta

import os
from Bioclass import Bioprof

nome_arquivo = 'dados' + os.sep + 'arquivo_L02E12_entrada.FASTA'
seq = Bioprof()
seq.leiaArquivoFasta(nome_arquivo)
print(seq.get_seqs()) #veirificando as sequencias armazenadas

for  s in seq.get_seqs():
    with open (s+".fasta", "w") as arq:
        arq.write(">"+s+"\n")
        arq.write(seq.get_sequencia(s))
