from Bioclass import Bioprof
import os,sys
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

k = 31
k_mers = seq.get_kmers(0,k)
path_dir = "." + os.sep + "saida"
if not os.path.exists(path_dir):
    os.makedirs(path_dir)      

saida = "." + os.sep + "saida" + os.sep + "mers" + ".fasta"
with open (saida, "w") as arq:
    for n, mer in enumerate(k_mers):
        arq.write(">" + str(n + 1)+"\n") 
        arq.write(mer + "\n") 
        arq.write("\n") 
print("Número de arquivos mers: ", len(k_mers)) 