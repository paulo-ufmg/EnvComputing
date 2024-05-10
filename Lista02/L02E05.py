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
