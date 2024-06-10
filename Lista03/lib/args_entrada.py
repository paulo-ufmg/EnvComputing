import os, sys

def busca_arquivo():
    #chamada a esse progrma segue: python a.py -i genoma.fasta
    arquivo = None if(len(sys.argv) < 3) else sys.argv[2]
    arg = None if(len(sys.argv) < 3 ) else sys.argv[1]

    if(arquivo==None)and (len(sys.argv)!= 3):
        print("Argumento incorreto! leitura [opção] nome_aquivo_fasta [ opcçao -i | -o ]")
        exit()

    if(arg !='-i'):
        print("Argumento incorreto! leitura [opção] nome_aquivo_fasta  [ opcçao -i | -o ]")
        exit()
    return arquivo    
