from Bioclass import Bioprof
import os
import sys

#chamada a esse progrma segue: python desafio03.py -i genoma.fasta
arquivo = None if(len(sys.argv) < 3) else sys.argv[2]
arg = None if(len(sys.argv) < 3 ) else sys.argv[1]

if(arquivo==None)and (len(sys.argv)!= 3):
    print("Argumento incorreto! leitura [opção] nome_aquivo_fasta [ opcçao -i | -o ]")
    exit()

if(arg !='-i'):
    print("Argumento incorreto! leitura [opção] nome_aquivo_fasta  [ opcçao -i | -o ]")
    exit()

seq = Bioprof()

seq.leiaArquivoFasta(arquivo)
print(seq.get_seqs())

genoma =  seq.get_seqs()[0] 

#Solução exercício Letra a) do desafio03.py
#-------------------------------------------
def a():
    print("a) Exibir o tamanho da sequência e o percentual de GC")
    print("-----------------------------------------------------")
    print("Tamanho sequencia.: ",seq.get_tamanho_sequencia(genoma))
    print("Percentual de GC..: {:.2f} %".format(seq.get_percentual_GC(genoma)))
    print("==================================================================Done!")
def b():
    print("b)Usando k=31 obtenha as sequências kmers, salve em arquivo e Responda:")
    print("------------------------------------------------------------------------")
    
    r"""Dividir a sequência com k = 31 usando janela deslizante. Salvar todas as sequencias resultantes no arquivo '.\saida\reads.fasta' identificando as sequencia por um número '>n' 
    Responder quantas sequências serão armazenadas nesse arquivo? Opcional: tente reconstruir o genoma original com base no arquivo “reads.fasta”.
    """
    k = 31
    k_mers = seq.get_kmers(genoma,k)
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

def b_desafio(saida):    
    print("Opcional: Reconstruindo o Genoma a partir dos k-mers do arquivo reads.fasta. Por favor aguarde...")

    assembly = Bioprof() #Objeto com os mers (partes do genoma)

    #importa todos os k-mers que forma o genoma para o novo objeto assembly
    assembly.leiaArquivoFasta(saida)
    print(assembly.get_assembly_kmers())
    seq.adiciona_seq("Obtido","Genoma construido a partir dos kmers",assembly.get_assembly_kmers()) #adiciona a sequencia construida a partir do kmers
    print("Comparando:")
    print(seq.get_seqs())
    print("Tamanho Genoma genoma: ",seq.get_tamanho_sequencia(genoma))
    print("Tamanbo Genoma obtido..: ",seq.get_tamanho_sequencia("Obtido"))
    print("Composição Genoma orginal..:",seq.get_composicao_seq(genoma))
    print("Composição Genoma obtido...:",seq.get_composicao_seq('Obtido'))
    print("Comparação identica: ", "Sucesso!" if seq.get_sequencia(genoma) == seq.get_sequencia("Obtido") else "Falha na construção do Genoma pelso k-mers!")
    #print("Sequencia Genoma:",seq.get_sequencia(orginal))
    #print("Sequencia obtida:",seq.get_sequencia('Obtido'))
    print("==================================================================Done!")

def c():
    print("c) CDS - ")
    print("-----------------------------------------------------")
    """
    c) Identifique todas as regiões codificantes (CDS) deste genoma. Considere que a região
    codificante começa com uma metionina (ATG) e termina com um stop códon terminal [ 'TAA','TAG','TGA'] ou ['UAA','UAG','UGA']; 
    considere as seis janelas de codificação (não há problema seu programa retornar falsos-positivos). Salve
    cada possível CDS em um arquivo no formato FASTA (sequencias de DNA ou RNA) (os arquivos devem ser salvos
    em uma pasta chamada “cds”).
    """
    cds = seq.busca_cds(genoma,'ATG')
    print("Regiõoes codificantes:",len(cds))
    #gravar em um arquivo todos os exons obtidos
    for i in range(len(cds)):
        arq = r"cds" + os.sep + "exons" + str(i+1) + ".fasta"
        with open (arq, "w") as arq:
            arq.write(">"+str(i)+"\n")
            arq.write(cds[i])
    print("==================================================================Done!")


def d():
    print("d)  ")
    print("-----------------------------------------------------")
    """
    d) Identifique o gene que codifica a proteína SPIKE (pesquise a importância dessa proteína
    para vírus no ChatGPT ou em um buscador) e salve em um arquivo chamado
    “spike.fasta” dentro da pasta “saida”. Dica: esta proteína possui uma região de grande
    importância com cinco aminoácidos em sequência - o primeiro é uma glicina (G),
    seguida de dois aminoácidos com carga polar positivo (R, K ou H), seguido por um
    aminoácido polar negativo (D ou E) e, por fim, uma outra glicina (G).
    """
    cds = seq.busca_cds(genoma,'ATG')

    #Gerando um arquivo proteina.fasta
    with open ("proteina.fasta", "w") as arq:
        arq.write(">proteina\n")
        arq.write("".join(cds))






    print("==================================================================Done!")

def e():       
    print("e)  ")
    print("-----------------------------------------------------")
    """
    e) Realize a modelagem da estrutura 3D da proteína (spike.fasta) usando ColabFold:
    https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.
    ipynb (use os parâmetros padrão). Opcional: abra a estrutura em um programa de
    visualização de proteínas (como o PyMOL ou o ChimeraX). Por fim, crie um script que
    gera um mapa de distâncias e um mapa de contatos (ligações de hidrogênio) desta
    proteína (esse script não precisa estar conectado diretamente no seu pipeline). Salve os
    mapas no formato PNG ou PDF dentro da pasta “saida”.

    """
def main():
    a()
    b()
    b_desafio("." + os.sep + "saida" + os.sep + "reads" + ".fasta")
    c()
    d()
    #e()
        
main()



