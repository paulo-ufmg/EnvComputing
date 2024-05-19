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
sequencia = seq.get_sequencia("Rosalind_10")
intron1 = seq.get_sequencia("Rosalind_12")
intron2 =  seq.get_sequencia("Rosalind_15")

#usando expressões regulares para remover os introns da sequencia de DNA
sequencia = re.sub(intron1, "", sequencia)
sequencia = re.sub(intron2, "", sequencia)
#armazenando a sequencia de DNA obtida na remoção dos itrons
seq.add_seq("DNA_R_10-Introns","Rosalind_10 removido introns da sequencia",sequencia)
sequencia = seq.transc_dna2rna("DNA_R_10-Introns")
seq.add_seq("mRNA_R_10","mRNA do DNA Rosalind_10",sequencia)
sequencia = seq.rna2proteina("mRNA_R_10")
print(sequencia)





