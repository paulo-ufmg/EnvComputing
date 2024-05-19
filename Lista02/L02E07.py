
#7. (PROT) Converter um mRNA em uma proteina usando a tabela de códons
#Exemplo entrada:
#  AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
#Saída:
#  MAMAPRTEINSTRING

from Bioclass import Bioprof
import os
arquivo = 'dados' + os.sep + 'arquivo_L02E07_string_rna.txt'
with open(arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()

seq = Bioprof()
seq.add_seq("1","Sequencia de RNA",str(linhas[0]))

print(f"Conversão do mRNA em uma proteina resultou: {seq.rna2proteina("1")}") 


