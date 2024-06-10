"""
    d) Identifique o gene que codifica a proteína SPIKE (pesquise a importância dessa proteína
    para vírus no ChatGPT ou em um buscador) e salve em um arquivo chamado
    “spike.fasta” dentro da pasta “saida”. Dica: esta proteína possui uma região de grande
    importância com cinco aminoácidos em sequência - o primeiro é uma glicina (G),
    seguida de dois aminoácidos com carga polar positivo (R, K ou H), seguido por um
    aminoácido polar negativo (D ou E) e, por fim, uma outra glicina (G).
    ["G",    (R,K ou H)    ,    (D ou E),     "G"] 
    Possibilidades:
    GRDG  GREG  GKDG  GKEG GHDG GHEG """
from Bioclass import Bioprof
import os, sys
import args_entrada

#busca arquivo passado na linha de comando
arquivo = args_entrada.busca_arquivo()

seq = Bioprof()
seq.leiaArquivoFasta(arquivo)

cds = seq.busca_cds(0,'ATG')
print(seq.get_seqs())
seq.dna(seq.get_seqs(0)).transcreve().traduz().imprime()


#Gerando um arquivo proteina.fasta
with open ("proteina.fasta", "w") as arq:
    arq.write(">proteina\n")
    arq.write("".join(cds))