#Programa que lê um arquivo string_de_dna contendo nucleotídeos.
#Saída deve ser 4 inteiros separados por espaços do somatório de ['A', 'C', 'G', 'T'] respectivamente [1]. 20 12 17 21

nome_arquivo = 'arquivo_L02E01_string_de_dna.txt'
nucleotideo = {"A":0,"C":0,"G":0,"T":0}
def main():
    global nucleotideo,nome_arquivo
    with open (nome_arquivo) as arq:
        while True:
            line = arq.readline()
            if not line:
                break
            for i in [*line]:
                if i in ['A','C','G','T']:
                    nucleotideo[i] +=1
main()
print(nucleotideo.values())
