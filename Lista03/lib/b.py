    

from Bioclass import Bioprof
import os,sys
import args_entrada
r"""Dividir a sequência com k = 31 usando janela deslizante. Salvar todas as sequencias resultantes no arquivo '.\saida\reads.fasta' identificando as sequencia por um número '>n' 
   Responder quantas sequências serão armazenadas nesse arquivo? Opcional: tente reconstruir o genoma original com base no arquivo “reads.fasta"""


#busca arquivo passado na linha de comando
arquivo = args_entrada.busca_arquivo()
seq = Bioprof()
seq.leiaArquivoFasta(arquivo)

print("\033[34mb)Usando k=31 obtenha as sequências kmers, salve em arquivo e Responda:\033[0m")
print("\033[34m------------------------------------------------------------------------\033[0m")
k = 31
k_mers = seq.get_kmers(0,k)
#Criar um diretório <saida>, somente se o mesmo não existir
path_dir = "." + os.sep + "saida"
if not os.path.exists(path_dir): #ou if not os.path.isdir(path_dir):
    os.makedirs(path_dir)      
#Gravando o arquivo Fasta
saida = "." + os.sep + "saida" + os.sep + "reads" + ".fasta"
with open (saida, "w") as arq:
    for n, mer in enumerate(k_mers):
        arq.write(">" + str(n + 1)+"\n") # Escreve a identificação da seqência
        arq.write(mer + "\n") #Escreve a sequencia mer no arquivo
        arq.write("\n") #adicona uma linha em branco no arquivo
print("Sequencias armazenadas no arquivo: ", len(k_mers)) #Poderia ser feito com ->  seq.get_tamanho_sequencia(orginal) - k + 1