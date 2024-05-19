#5. Lê uma séri de sequencias em um arquivo fasta e calcula o (GC)
#Saida: imprime o id da série e o valor do GC da sequência que possuir o maior GC

import os
from Bioclass import Bioprof

nome_arquivo = 'dados' + os.sep + 'arquivo_L02E05_file_fasta.txt'
seq = Bioprof()
GC = []
seq.leiaArquivoFasta(nome_arquivo)
indice = 0
for s in seq.composicao_total:
    GC.append((s['G']+s['C'])/seq.tamanho_sequencia( indice ) )
    indice +=1

maior_GC = max(GC)
indice = GC.index(maior_GC)
print(f"Sequencia de maior GC é: {seq.ids[indice]}")
print("O valor de GC é: {:.2f} %".format(maior_GC*100))
print("--Done!---")

print("Verificando...")
for s in seq.get_seqs():
    seq.ver_info_seq(s)