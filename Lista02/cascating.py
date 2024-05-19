"""
Regiões codificantes e não codificantes de uma sequência de DNA
----------------------------------------------------------------
Remover os introns de uma sequencia de DNA, e após transcrita para o mRNA gera a proteina equivalente

Exemplo entrada:
>Rosalind_10 [Sequencia de DNA]
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGC
GTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12 [Intron para ser removido]
ATCGGTCGAA
>Rosalind_15 [Intron para ser removido]
ATCGGTCGAGCGTGT
Saída:
MVYIADKQHVASREAYGHMFKVCA

Bioinformatics Textbook Track
"""
import os
import re
from Bioclass import Bioprof

nome_arquivo = 'dados' + os.sep + 'arquivo_L02E09_string_de_dna.txt'
seq = Bioprof()
seq.leiaArquivoFasta(nome_arquivo)

#Recebendo os dados de entrada

i1 = seq.get_sequencia("Rosalind_12")
i2 =  seq.get_sequencia("Rosalind_15")

#Métodos em cascata para transformar de um DNA  a uma proteina
sequencia = seq.get_sequencia("Rosalind_10").remove_introns(i1).remove_introns(i2).transcreve_rna().to_proteina().sequencia
print(sequencia)