from Bioclass import Bioprof
import sys

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

print(seq.nucleotideos)
exit()

for i in seq.get_seqs():
    seq.get_info_seq(i) #método get_info_seq(id) retorna dados sobre a sequência

