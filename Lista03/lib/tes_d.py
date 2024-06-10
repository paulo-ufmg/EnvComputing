from Bioclass import Bioprof
import os, sys
arquivo = ""
arg =""
if(len(sys.argv) < 3): 
    arquivo = None  
    arg = None  
else: 
    arquivo =  sys.argv[2]
    arg = sys.argv[1]

if(arquivo==None) and (len(sys.argv) != 3 or arg !='-i'):
    print("Argumento incorreto!")
    exit()


seq = Bioprof()
seq.leiaArquivoFasta(arquivo)


cds = seq.busca_cds(0,'ATG')
seq.dna(seq.get_seqs(0)).transcreve().traduz().imprime()

#Gerando um arquivo proteina.fasta
with open ("proteina.fasta", "w") as arq:
    arq.write(">proteina\n")
    arq.write("".join(cds))