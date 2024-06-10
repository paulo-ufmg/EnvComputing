"""a) Leitura de um arquivo completo do genoma em arquivo passado como parâmetro. 
- Imprime na tela o tamanho da sequência e qual o conteúdo GC do genoma.
======================================================================================"""
from Bioclass import Bioprof
import os, sys
import args_entrada

#busca arquivo passado na linha de comando
arquivo = args_entrada.busca_arquivo()

seq = Bioprof()
seq.leiaArquivoFasta(arquivo)
#print(seq.get_seqs()) #Visualiza sequências carregadas

#salva arquivo temporário para ser usado nos próximos scripts
#arquivo_temp =  "." + os.sep + "temp" + os.sep +  "saida_a.fasta"
#seq.salvaSeqArquivoFasta(arquivo_temp,seq.get_seqs("genomma"))

#resposta do exercício
print("\033[34mExibir o tamanho da sequência e o percentual de GC\033[0m")
print("Tamanho sequencia.: ",seq.get_tamanho_sequencia(0))
print("Percentual de GC..: {:.2f} %".format(seq.get_percentual_GC(0)))
