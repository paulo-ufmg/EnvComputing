#Funcionalidade: 2. Lê arquivo com string e converter em RNA.
#Saida: Transcrição: RNA (substituiÇÃO de “T”s por “U”s. Exempllo: GAUGGAACUUGACUACGUAAAUU

nome_arquivo = 'arquivo_L02E02_string_de_dna.txt'
rna = list()
def main():
    global rna, nome_arquivo
    with open (nome_arquivo) as arq:
        while True:
            line = arq.readline()
            if not line:
                break
            for i in [*line]:
                rna += ["U"] if(i == 'T') else [i]
main()
print(''.join(rna))
