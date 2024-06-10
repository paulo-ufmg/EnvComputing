
from Bioclass import Bioprof
import sys, os

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

print("CDS Total:",len(cds))

#Segmentos codificantes
for i in range(len(cds)):
    arq = r"cds" + os.sep + "codificante_" + str(i+1) + ".fasta"
    with open (arq, "w") as arq:
        arq.write(">"+str(i)+"\n")
        arq.write(cds[i])
