#Funcionalidade: 
#Saida: 

"""
5. (GC) O conteúdo GC de uma string de DNA é dado pela porcentagem de
símbolos na string que são 'C' ou 'G'. Por exemplo, o conteúdo de GC de
"AGCTATAG" é de 37,5%. Observe que o complemento reverso de qualquer string
de DNA tem o mesmo conteúdo de GC. Considerando isso, faça um programa que
leia um arquivo FASTA contendo várias identificadores (que começam com o
carácter “>”) e sequências de DNA. O programa deve retornar o identificador da
sequência que possua o maior conteúdo GC seguido do valor do conteúdo GC [5].
Exemplo entrada:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGA
GG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAG
ACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGT
AGGTGGAAT
Saída:
Rosalind_0808
60.919540

"""
import re
class File_fasta:
    
    def __init__(self):
       self.autor = 'Paulo Rocha'
       self.ids = [] #Lista de id's das sequências referenciadas pelo index da lista
       self.info ={} #Dicionario que armazena um comentario da sequência
       self.nucleotideo = {"A":0,"C":0,"G":0,"T":0,"U":0} #nucleotideos presente na sequencia
       self.nucleotideos = [] #Lista de aminoácido {"C":0,"G":0,"T":0,"U":0}
    
    def seq_existe (self,id):
       return True if(id in self.ids) else False 
    
    def get_seqs(self):
        return  self.ids
    #erro verificar
    def soma_nucleotideos(self,indice):
        total = 0
        for n in self.nucleotideos[indice]:
            total += self.nucleotideos[indice][n]
        return n    

    def new_seq(self,id):
       if not(self.seq_existe(id)):
          self.ids.append(id)
          self.nucleotideos.append(self.nucleotideo)
       else:
          print("Sequencia já inserida!")   

    def insert_comment(self,id,info):
       if (self.seq_existe(id) and info is not None):
            self.info[self.ids.index(id)] = info
     
    def add_aminoacido(self,id,tipo):
        if(re.sub(r'[\t\n\r\f\v\b\0\a\s]', '',tipo)==""):
            return 
        if(self.seq_existe(id)): 
            if("ACGTU".find(tipo) != -1):
               self.nucleotideos[ self.ids.index(id) ][tipo] += 1
            else:
               print(f"Nucleotídeo não reconhecido!{tipo}")
        else:
            print(f"-Identificação de sequência não encontrada!{id}")
                    
    def get_seq(self,id):
        if(self.seq_existe(id)):
            indice = self.ids.index(id)
            print("Informações da sequência:")
            print("=========================")
            print(f"Id: {self.ids[indice]}")
            if(indice in self.info ):
                print(f"Info: {self.info[indice]}")
            #print(self.nucleotideos)   
            print(f"Q(n): A({self.nucleotideos[indice]['A']}),C({self.nucleotideos[indice]['C']}),G({self.nucleotideos[indice]['G']}),T({self.nucleotideos[indice]['T']}),U({self.nucleotideos[indice]['U']})")
            print(f"Total: {self.soma_nucleotideos[indice]}")
            GC = (self.nucleotideos[indice]['G']+self.nucleotideos[indice]['C'])/self.soma_nucleotideos[indice]
            print("GC: {:.2f}%".format(GC))
       
    def identifica_id(self,line):
        match = re.match(r'^>(\S+)', line)
        if match:
            return match.group(1)
        else:
            return None

    def identifica_info(self,line):
        match = re.match(r'^>[\w\|]+ (.+)', line)
        if match:
            return match.group(1)
        else:
           return None

  

#===============================================================
import os
nome_arquivo = 'dados' + os.sep + 'arquivo_L02E05_file_fasta.txt'
seq = File_fasta()
id = ""

def main():
    global id,nome_arquivo
    with open (nome_arquivo) as arq:
        while True:
            line = arq.readline()
            if not line:
                break
            if line.strip()[0]==";":
               continue
            if(line.find('>') >= 0): #Identificado nova sequencia
                id = seq.identifica_id(line)
                seq.new_seq(id)
                comment = seq.identifica_info(line)
                seq.insert_comment(id,comment)
            else:    #compilando a sequencia
                for i in [*line]:
                    seq.add_aminoacido(id,i)
main()
for i in seq.get_seqs():
    print(seq.get_seq(i))
    #seq.get_seq[i]
    print("=======================================")

