from Bioclass import Bioprof
import sys

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
print("Tamanho: ",seq.get_tamanho_sequencia(0))
print("GC..: {:.2f} %".format(seq.get_percentual_GC(0)))