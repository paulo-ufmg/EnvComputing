
#Programa lê um arquivo PDB. convertendo para o formato FASTA, onde cada identificar do arquivo FASTA contenha a 
#sequência de aminoácidos de cada cadeia polipeptídica do arquivo PDB.
#entrada:
#-----------
"""Arquivo 1A1M.pdb"""
#Saída:
#--------------
"""
>1A1M_A
GSHSMRYFYTAMSRPGRGEPRFIAVGYVDDTQFVRFDSDAASPRTEPRPPWIEQEGPEYWDRNTQIFKTNTQTYRENL
RIALRYYNQSEAGSHIIQRMYGCDLGPDGRLLRGHDQSAYDGKDYIALNEDLSSWTAADTAAQITQRKWEAARVAEQL
RAYLEGLCVEWLRRYLENGKETLQRADPPKTHVTHHPVSDHEATLRCWALGFYPAEITLTWQRDGEDQTQDTELVETR
PAGDRTFQKWAAVVVPSGEEQRYTCHVQHEGLPKPLTLRWEPHH
>1A1M_B
IQRTPKIQVYSRHPAENGKSNFLNCYVSGFHPSDIEVDLLKNGERIEKVEHSDLSFSKDWSFYLLYYTEFTPTEKDEY
ACRVNHVTLSQPKIVKWDRDM
>1A1M_C
TPYDINQML
"""
amin = {}
dic = {"ALA":"A","ARG":"R","ASN":"N","ASP":"D","CYS":"C","GLN":"Q","GLU":"E","GLY":"G","HIS":"H","ILE":"I","LEU":"L","LYS":"K","MET":"M","PHE":"F","PRO":"P","SER":"S","THR":"T","TRP":"W","TYR":"Y","VAL":"V"}

seq=""
sequencia = []
arquivo = "1A1M.pdb"
with open (arquivo) as arq:
    #for i in range(404): #essa opção reduz 0,001 segundos
    #    lixo = arq.readline()
    while True:
        line = arq.readline()
        if not line:
            break
        #print(line[0:4])#
    
        if(line[0:4] == "ATOM"):  #Inicio de uma
            if(seq!=line[17:20]):
                sequencia.append(dic[line[17:20]])
                seq=line[17:20]
arq.close()
 
#Gravando o arquivo Fasta
with open (arquivo+".fasta", "w") as arq:
    arq.write(">"+arquivo+"\n")
    arq.write("".join(sequencia))


