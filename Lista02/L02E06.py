"""
6. (HAMM) A distância de Hamming (dH) entre duas cadeias com o mesmo
comprimento é o número mínimo de substituições de símbolos necessárias para
transformar uma cadeia na outra. Sendo assim, faça um programa que leia um
arquivo contendo 2 cadeias de DNA s e t de tamanho idêntico. O programa deve
retornar a distância de Hamming entre s e t, denotada por dH(s,t), onde dH(s,t) é o
número de símbolos correspondentes que diferem em s e t [6].
Exemplo entrada:

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Saída:
"""
from Bioclass import Bioprof

seq = Bioprof()

seq.add_seq("1","Primeira sequencia","GAGCCTACTAACGGGAT")
seq.add_seq("2", "Segunda sequencia","CATCGTAATGACGGCCT")

#print(seq.get_seqs())
#for i in seq.get_seqs():
#    seq.ver_info_seq(i)

print("A distância de Hamming(dH) entre a sequencia 1 e 2 é: ",seq.dH("1","2"))



