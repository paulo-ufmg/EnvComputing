"""
    c) Identifique todas as regiões codificantes (CDS) deste genoma. Considere que a região
    codificante começa com uma metionina (ATG) e termina com um stop códon terminal [ 'TAA','TAG','TGA'] ou ['UAA','UAG','UGA']; 
    considere as seis janelas de codificação (não há problema seu programa retornar falsos-positivos). Salve
    cada possível CDS em um arquivo no formato FASTA (sequencias de DNA ou RNA) (os arquivos devem ser salvos
    em uma pasta chamada “cds”)."""

from Bioclass import Bioprof
import os,args_entrada

#busca arquivo passado na linha de comando
arquivo = args_entrada.busca_arquivo()

seq = Bioprof()
seq.leiaArquivoFasta(arquivo)

print("\033[34mb) CDS - Regiões codificantes: \033[0m")
print("\033[34mb) --------------------------- \033[0m")
cds = seq.busca_cds(0,'ATG')

print("Regiõoes codificantes:",len(cds))

#gravar em um arquivo todos os segmentos codificantes
for i in range(len(cds)):
    arq = r"cds" + os.sep + "cd_" + str(i+1) + ".fasta"
    with open (arq, "w") as arq:
        arq.write(">"+str(i)+"\n")
        arq.write(cds[i])
