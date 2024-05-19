import time
inicio = time.time()
# seu código deve iniciar aqui
amin = {}
dic = {"ALA":"A","ARG":"R","ASN":"N","ASP":"D","CYS":"C","GLN":"Q","GLU":"E","GLY":"G","HIS":"H","ILE":"I","LEU":"L","LYS":"K","MET":"M","PHE":"F","PRO":"P","SER":"S","THR":"T","TRP":"W","TYR":"Y","VAL":"V"}

seq=""

with open ("3RGK.pdb") as arq:
    #for i in range(404): #essa opção reduz 0,001 segundos
    #    lixo = arq.readline()
    while True:
        line = arq.readline()
        if not line:
            break
        #print(line[0:4])#
    
        if(line[0:4] == "ATOM"):  #Inicio de uma
            if(seq!=line[17:20]):
                print(dic[line[17:20]],end="")
                seq=line[17:20]
            #print(line[17:20])
            #print(dic[line[17:20]])
arq.close()
# seu codigo deve terminar aqui
fim = time.time()
tempo = round(fim - inicio, 3)
print(f"Tempo total de execução: {tempo}s")
'''
***************************************************************
SAÍDA ESPERADA: 
***************************************************************
>Mioglobina humana | PDB ID: 3RGK
GLSDGEWQLVLNVWGKVEADIPGHGQEVLIRLFKGHPETLEKFDRFKHLKSEDEMKASEDLKK
HGATVLTALGGILKKKGHHEAEIKPLAQSHATKHKIPVKYLEFISEAIIQVLQSKHPGDFGAD
AQGAMNKALELFRKDMASNYKEL

***************************************************************
Tempo total de execução: 0.733s
***************************************************************
'''