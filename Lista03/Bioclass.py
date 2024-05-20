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
       self.sequencia = [] # Lista de string contendo a sequencia de DNA,RNA ou Proteina
       self.alerta = True
       self.codons = {
            "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L","CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L","AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M","GUU": "V",
            "GUC": "V", "GUA": "V", "GUG": "V","UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S","CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P","ACU": "T", "ACC": "T",
            "ACA": "T", "ACG": "T","GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A","UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*","CAU": "H", "CAC": "H", "CAA": "Q",
            "CAG": "Q","AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K","GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E","UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
            "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R","AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R","GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"           
        }

    def message_view(self,mensagem,interrupt=False):
        """Exibir mensagem de alerta"""
        if(self.alerta): print(mensagem)
        if(interrupt): exit()        
        

    def seq_existe (self,arg):
       """Retorna verdadeiro se a sequencia identificada em argumento está registrada"""
       if(isinstance(arg, int)): return True if 0 <= arg < len(self.ids) else False #procura por um indice presente na Lista de identificação de sequencias (ids)
       else: return True if(arg in self.ids) else False  #procura pela identificação da sequencia na Lista de identificação de sequencias (ids)
    
    def get_seqs(self):
        """Retorna a lista de sequencias registradas"""
        return  self.ids
    
    def get_info(self,id_ou_indice):
        """Retorna comentário da sequencia"""
        indice = id_ou_indice if (isinstance(id_ou_indice, int)) else self.ids.index(id_ou_indice)
        if indice in self.info:
            return self.info[indice]
        else: self.message_view("Sequencia não possui comentário!")   
        
        
    def get_tamanho_sequencia(self,id_ou_indice): #permite receber como paramentro um inteiro que é o indice ou uma string id que é a identificação da sequencia
        """Soma a quantidade nucleotideos ou aminoácidos de uma sequencia"""
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
          self.message_view("Sequencia já inserida!")   
          return False
       
    def get_sequencia(self,id):
        """ Retorna a sequencia armazenada com seus nucleotídeos (DNA e RNA) ou dos aminoácidos (Proteina)"""
        return self.sequencia[ self.ids.index(id) ]  if (self.seq_existe(id)) else None
    
    def get_composicao_seq(self,id):
        """ Retorna a composição da sequência com os totais de nucleotídeos (DNA e RNA) ou dos aminoácidos (Proteina) """
        if (self.seq_existe(id)):
            temp = f"T({self.get_tamanho_sequencia(self.ids.index(id))}): "
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
    
    def get_percentual_GC(self,arg):
        """Retorna a percentual(%) de Guanina e Citosina na sequência."""
        if (self.seq_existe(arg)):
            indice = arg if isinstance(arg, int) else self.ids.index(arg) 
            G = self.composicao_total[indice]['G'] if('G' in self.composicao_total[indice]) else 0
            C = self.composicao_total[indice]['C'] if('C' in self.composicao_total[indice]) else 0
            GC = ( G + C ) / self.get_tamanho_sequencia(indice) if(self.get_tamanho_sequencia(indice) > 0) else 0
            return GC*100
        self.message_view("Sequencia não encontrada!")
        return None



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
            print(f"Tamanho sequencia: {self.get_tamanho_sequencia(indice)}")
            print("Percentual de GC: {:.2f} %".format(self.get_percentual_GC(indice)))
            
            #if(("G" in self.composicao_total[indice])and("C" in self.composicao_total[indice])):
            #    GC = (self.composicao_total[indice]['G']+self.composicao_total[indice]['C'])/self.get_tamanho_sequencia(indice)
            #    print("GC: {:.2f} %".format(GC*100))


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
        with open (nome_arquivo, "r") as arq:
            while True:
                self.line = arq.readline()
                if not self.line: break #interrompe ao final do arquivo
                if self.line.strip() == "": continue  # Ignorar linhas em branco
                if self.line.strip()[0]==";": continue # ignora linhas de comentário

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

    def add_seq(self,n1,n2,n3):
        """Insere uma sequência através de código"""
        if(self.nova_sequencia(n1)):
            self.insert_comment(n1,n2)
            for n in n3:
                self.add_item(n1,n) 
        else:
            self.message_view("Erro ao adicionar ou sequência já inserida!")   

    # Calcula a distância de Hamming (dH) entre duas sequências
    def dH(self,id1,id2):
        """Distãncia de Hamming (dH) entre duas sequências de DNA ou RNA"""
        if(self.seq_existe(id1) and self.seq_existe(id2)):
            if([self.get_tipo_seq(id1),self.get_tipo_seq(id2)] == ['DNA','DNA'] or [self.get_tipo_seq(id1),self.get_tipo_seq(id2)] == ['RNA','RNA']):
                if(self.get_tamanho_sequencia(id1)==self.get_tamanho_sequencia(id2)):
                    seq1 = self.get_sequencia(id1)
                    seq2 = self.get_sequencia(id2)
                    dist =0 
                    for n1, n2 in zip(seq1, seq2):
                        if(n1 != n2):
                            dist += 1
                    return dist       
                else: self.message_view("As sequências têm comprimentos diferentes.")       
            else: self.message_view("Para calcular a distância de hamming as sequências devem ser de DNA ou de RNA.")       
        else: self.message_view("Identificação das sequências não encontrada!")       
        return False
    
    def rna2proteina(self,id):
        proteina = []
        if(self.seq_existe(id)):
            if(self.get_tipo_seq(id) == "RNA"):
                mRNA = self.get_sequencia(id)
                for i in range(0, len(mRNA), 3):
                    codon = mRNA[i:i+3]  # Extrai o códon de 3 nucleotídeos
                    aminoacido = self.codons.get(codon, 'X')  # Obtém o aminoácido correspondente ao códon
                    proteina.append(aminoacido)  # Adiciona o aminoácido à lista
                # Junta os aminoácidos em uma única string
                return ''.join(proteina) 
            else: self.message_view("Sequência para transcrição não é um RNA!")              
        else: self.message_view("Identificação das sequências não encontrada!")              
        return None
    
    def transc_dna2rna(self,id):
        """Transcrição de uma sequência de DNA em um mRNA -Substitui todas as ocorrências de 'T' por 'U' """
        if(self.seq_existe(id)):
            if(self.get_tipo_seq(id) == "DNA"):
                DNA = self.get_sequencia(id)
                mRNA =  DNA.replace('T', 'U')
                return mRNA
            else: self.message_view("Sequência para transcrição não é um DNA!")              
        else: self.message_view("Identificação das sequências não encontrada!")              
        return None


    def get_kmers(self,id,k):
        """Retorna uma lista de sequencias k da janela deslizante da sequência
        :param sequencia: A sequência de entrada (string)
        :param k: O comprimento dos k-mers (inteiro)
        :return: Uma lista de k-mers
        """
        if(self.seq_existe(id)):
            if(k <= self.get_tamanho_sequencia(id)):
                sequencia = self.get_sequencia(id)
                kmers = []
                for i in range(len(sequencia) - k + 1):
                    kmers.append(sequencia[i:i + k])
                return kmers
            else: self.message_view("Comprimento k (k-mers) maior que a sequência!")                  
        else: self.message_view("Identificação das sequências não encontrada!")  
        return None                
    
    def get_assembly_kmers(self):
        """Assembly, monta um genoma a partir dos kmers (conjunto de todas as sequencias do objeto)"""
        if(len(self.ids) > 1):
            genoma = ""
            for i in range(len(self.ids)-1):
                genoma += self.sequencia[i][0]
            genoma += self.sequencia[len(self.ids)-1]
            return genoma
        if (len(self.ids) == 1): return self.ids[0]
        else: self.message_view("Não existe Mers suficientes para construir uma estrutura de sequência!")                  
        return None
    