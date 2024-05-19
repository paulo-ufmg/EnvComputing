# Trabalho.
#
# Este arquivo faz parte do trabalho da disciplina de Ambintes de Computação do dpto de 
# pós graduação da Ciência da Computação da  UFMG
import re
import os

class Bioprof:
    """Bioprof - Trabalho da disciplina de Ambientes de Computação DCC-PPGCC.UFMG(2024)
    Leitura de arquivo de sequencia .FASTA e manipulação de sequências
    Disciplina: Ambientes de Computação
    Local: UFMG, 2024
    Professor:  Diego .
    Alunos:
     - Fredy Ernesto Villena Patiño (fredyvp@ufmg.br)
     - Paulo Rocha (paulo-rocha@ufmg.br)
     - Rodrigo Jereissati Martins (rod.jereissati@gmail.com)

    Link do github: https://github.com/paulo-ufmg/Bioprof
    """
    
    def __init__(self):
        self.__version__ = "0.02"
        self.id = "" #string que contém o nome(identificação da sequencia)
        self.ids = [] #Lista de id's das sequências referenciadas pelo index da lista
        self.info ={} #Dicionario que armazena um comentario da sequência
        self.composicao_DNA_RNA_PROTEINA = {} #nucleotideos ou aminoácidos presente na sequencia DNA-RNA ou de Proteina
        #self.nucleotideo = {} #nucleotideos ou aminoácidos presente na sequencia DNA-RNA ou de Proteina
        self.composicao_total = [] #Totalização de nucleotídeos na sequencia  {"C":0,"G":0,"T":0,"U":0}
        self.sequencia = [] # Lista de string contendo a sequencia de DNA,RNA ou Proteina                                                                                                                                                        x    
        self.codons = {
           'TTT':'F','TTC':'F','TTA':'L','TTG':'L','TCT':'S','TCC':'S','TCA':'S','TCG':'S','TAT':'Y','TAC':'Y','TAA':'*','TAG':'*','TGT':'C','TGC':'C','TGA':'*','TGG':'W','CTT':'L','CTC':'L','CTA':'L','CTG':'L','CCT':'P',
           'CCC':'P','CCA':'P','CCG':'P','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q','CGT':'R','CGC':'R','CGA':'R','CGG':'R','ATT':'I','ATC':'I','ATA':'I','ATG':'M','ACT':'T','ACC':'T','ACA':'T','ACG':'T','AAT':'N','AAC':'N',
           'AAA':'K','AAG':'K','AGT':'S','AGC':'S','AGA':'R','AGG':'R','GTT':'V','GTC':'V','GTA':'V','GTG':'V','GCT':'A','GCC':'A','GCA':'A','GCG':'A','GAT':'D','GAC':'D','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGA':'G','GGG':'G'
        }
        self.alerta = True

    def message_view(self,mensagem,interrupt=False):
        """Exibir mensagem de alerta"""
        if(self.alerta):print(mensagem)
        if(interrupt): exit()        
        

    def seq_existe (self,id):
       """Retorna verdadeiro se a sequencia identificada por id está registrada"""
       return True if(id in self.ids) else False 
    
    def get_seqs(self):
        """Retorna a lista de sequencias registradas"""
        return  self.ids

    def tamanho_sequencia(self,id_ou_indice): #permite receber como paramentro um inteiro que é o indice ou uma string id que é a identificação da sequencia
        """Soma a quantidade nucleotideos ou aminoácidos de uma sequencia"""
        indice = id_ou_indice if (isinstance(id_ou_indice, int)) else self.ids.index(id_ou_indice)    
        indice = id_ou_indice if (isinstance(id_ou_indice, int)) else self.ids.index(id_ou_indice)
        tamanho = 0
        if((len(self.composicao_total) < indice) or not isinstance(indice, int)): 
            self.message_view("Sequencia não encontrada!")
            return 0
        for n in self.composicao_total[indice]:
            tamanho += self.composicao_total[indice][n]
        return tamanho

    def nova_sequencia(self,id):
       """Insere uma nova sequencia na lista ids"""
       if not(self.seq_existe(id)):
          self.ids.append(id)
          self.composicao_total.append(dict(self.composicao_DNA_RNA_PROTEINA)) #Expressão dict faz uma copia do dicionario
          self.sequencia.append("") #Inicializa uma string na lista para aramazenar a sequencia
          return True 
       else:
          
          return False
       
    def get_sequencia(self,id):
        """ Retorna a sequencia armazenada com seus nucleotídeos (DNA e RNA) ou dos aminoácidos (Proteina)"""
        return self.sequencia[ self.ids.index(id) ]  if (self.seq_existe(id)) else None
    
    def get_composicao_seq(self,id):
        """ Retorna a composição da sequência com os totais de nucleotídeos (DNA e RNA) ou dos aminoácidos (Proteina) """
        if (self.seq_existe(id)):
            temp = f"T({self.tamanho_sequencia(self.ids.index(id))}): "
            for chave, valor in self.composicao_total[ self.ids.index(id) ].items():
                temp +=  chave +'('+str(valor)+')'+','
            return temp
        self.message_view("Sequencia não encontrada!")   

    def get_tipo_seq(self,id):
        """Identifica uma sequencia se é de DNA, RNA ou PROTEINA"""
        seq = self.get_sequencia(id)
        if(seq.find("U") != -1):  
            return "RNA"
        return "DNA" if(len(re.findall(r'[^ACGT]', seq)) == 0) else "Proteina" #Se sequencia contém somente ACGT é um DNA


    def insert_comment(self,id,info):
       """Armazena o comentário da sequência"""
       if (self.seq_existe(id) and info is not None):
            self.info[self.ids.index(id)] = info
     
    def add_item(self,id,item):
        """Adciona um somatório de nucleotídos ou aminoácidos da sequência"""
        if(re.sub(r'[\t\n\r\f\v\b\0\a\s]', '',item)==""):
            return 
        if(self.seq_existe(id)): 
            if("ACGTUDEFHIKLMNPQRSVWY".find(item) != -1): #ACGTU (Nucleotídeos presentes no DNA ou RNA) | ACDEFGHIKLMNPQRSTVWY (Aminoácidos presentes na Proteina)
                indice = self.ids.index(id)
                if(item in self.composicao_total[ indice ]):
                    self.composicao_total[ indice ][item] += 1
                else:
                    self.composicao_total[ indice ][item] = 1    
                self.sequencia[ indice ] += item    
            else:
               self.message_view(f"Um nucleotídeo ou aminoácido não reconhecido na sequencia[{id}]!{item}",True)
        else:
            self.message_view(f"-Identificação de sequência não encontrada!{id}")
                    
    def ver_info_seq(self,id):
        """Exibe dados de uma sequência"""
        if(self.seq_existe(id)):
            indice = self.ids.index(id)
            print("Informações da sequência:")
            print("=========================")
            print(f"Id: {self.ids[indice]}")
            print(f"Sequencia de {self.get_tipo_seq(id)}")
            if(indice in self.info ):
                print(f"Info: {self.info[indice]}")
            print(f"Composição: {self.get_composicao_seq(id)}")
                #print(f"Q(n): A({self.composicao_total[indice]['A']}),C({self.composicao_total[indice]['C']}),G({self.composicao_total[indice]['G']}),T({self.composicao_total[indice]['T']}),U({self.composicao_total[indice]['U']})")
            print(f"Tamanho sequencia: {self.tamanho_sequencia(indice)}")
            if(("G" in self.composicao_total[indice])and("C" in self.composicao_total[indice])):
                GC = (self.composicao_total[indice]['G']+self.composicao_total[indice]['C'])/self.tamanho_sequencia(indice)
                print("GC: {:.2f} %".format(GC*100))
        else:
            self.message_view("Sequencia não encontrada!")   
       
    def identifica_id(self,line):
        """Retorna a string de identificação da sequência (id)"""
        match = re.match(r'^>(\S+)', line)
        if match:
            return match.group(1)
        else:
            return None

    def identifica_info(self,line):
        """Retorna a string de comentário da sequência (id)"""
        match = re.match(r'^>[\w\|]+ (.+)', line)
        if match:
            return match.group(1)
        else:
           return None

    
            


    def leiaArquivoFasta(self,nome_arquivo):
        """ Lê  todas as sequências de um arquivo Fasta """    
        with open (nome_arquivo) as arq:
            while True:
                self.line = arq.readline()
                if not self.line:
                    break
                if self.line.strip()[0]==";":
                    continue
                if(self.line.find('>') >= 0): #Identificado nova sequencia
                    self.id = self.identifica_id(self.line)
                    if(self.nova_sequencia(self.id)):
                        comment = self.identifica_info(self.line)
                        self.insert_comment(self.id,comment)
                    else: self.id = None    
                else:    #compilando a sequencia
                    if(self.id != None):
                        for i in [*self.line]:
                            self.add_item(self.id,i)  

    
    def add_seq(self,*args):
        print(args)
        exit()

        """Insere uma sequência através de código"""
        if(self.nova_sequencia(id)):
            self.insert_comment(id,comment)
            for n in sequencia:
                self.add_item(id,n) 
        else:
            self.message_view("Erro ao adicionar ou sequência já inserida!")   




