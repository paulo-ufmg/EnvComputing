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

    Link do github: https://github.com/paulo-ufmg/Bioclass
    """
    
    def __init__(self):
       self.__version__ = "0.01"
       self.ids = [] #Lista de id's das sequências referenciadas pelo index da lista
       self.info ={} #Dicionario que armazena um comentario da sequência
       self.nucleotideo = {"A":0,"C":0,"G":0,"T":0,"U":0} #nucleotideos presente na sequencia
       self.nucleotideos = [] #Lista de aminoácido {"C":0,"G":0,"T":0,"U":0}
       self.alerta = True
       self.sequencia = [] #Lista completa das sequencias
       
       

    def message_view(self,mensagem,interrupt=False):
        """Exibir mensagem de alerta"""
        if(self.alerta): print(mensagem)
        if(interrupt): exit()        
        

    def seq_existe (self,id):
       """Retorna verdadeiro se a sequencia identificada por id está registrada"""
       return True if(id in self.ids) else False 
    
    def get_seqs(self):
        """Retorna a lista de sequencias registradas"""
        return  self.ids
        
    def soma_nucleotideos(self,indice):
        """Soma a quantidade nucleotideos de uma sequencia"""
        total = 0
        if((len(self.nucleotideos) < indice) or not isinstance(indice, int)): 
            self.message_view("Sequencia não encontrada!")
            return 0
        for n in self.nucleotideos[indice]:
            total += self.nucleotideos[indice][n]
        return total    

    def new_seq(self,id):
       if not(self.seq_existe(id)):
          self.ids.append(id)
          self.nucleotideos.append(dict(self.nucleotideo)) #Expressão dict faz uma copia do dicionario nucleotideo
       else:
          self.message_view("Sequencia já inserida!",True)   

    def insert_comment(self,id,info):
       if (self.seq_existe(id) and info is not None):
            self.info[self.ids.index(id)] = info
     
    def add_nucleotideo(self,id,tipo):
        """Adciona um somatório de nucleotídos da sequência"""
        if(re.sub(r'[\t\n\r\f\v\b\0\a\s]', '',tipo)==""):
            return 
        if(self.seq_existe(id)): 
            if("ACGTU".find(tipo) != -1):
               self.nucleotideos[ self.ids.index(id) ][tipo] += 1
            else:
               self.message_view(f"Nucleotídeo não reconhecido na sequencia[{id}]!{tipo}",True)
        else:
            self.message_view(f"-Identificação de sequência não encontrada!{id}")
                    
    def get_info_seq(self,id):
        if(self.seq_existe(id)):
            indice = self.ids.index(id)
            print("Informações da sequência:")
            print("=========================")
            print(f"Id: {self.ids[indice]}")
            if(indice in self.info ):
                print(f"Info: {self.info[indice]}")
            #print(self.nucleotideos)   
            print(f"Q(n): A({self.nucleotideos[indice]['A']}),C({self.nucleotideos[indice]['C']}),G({self.nucleotideos[indice]['G']}),T({self.nucleotideos[indice]['T']}),U({self.nucleotideos[indice]['U']})")
            print(f"Total: {self.soma_nucleotideos(indice)}")
            GC = (self.nucleotideos[indice]['G']+self.nucleotideos[indice]['C'])/self.soma_nucleotideos(indice)
            print("GC: {:.2f} %".format(GC*100))
            
            
       
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
                    self.new_seq(self.id)
                    comment = self.identifica_info(self.line)
                    self.insert_comment(self.id,comment)
                else:    #compilando a sequencia
                    for i in [*self.line]:
                        self.add_nucleotideo(self.id,i)    
#===============================================================
