#Funcionalidade: 3.(REVC) Busca o DNA em um arquivo e transcreve o DNA COMPLEMNTAR(cDNA) REVERSO. Exemplo: AAAACCCGGT
#Saida: Transcrição: cDNA (substituiÇÃO de “A”<->"T" e "C"<->"G". Exempllo: ACCGGGTTTT

nome_arquivo = 'arquivo_L02E03_string_de_dna.txt'
revc = list()
def main():
    global revc, nome_arquivo
    with open (nome_arquivo) as arq:
        temp =""
        while True:
            line = arq.readline().strip()
            if not line: #interrompe o while se nenhuma linha for lida!
                break
            for i in [*line][::-1]: #percorre a lista de string de forma reversa
                match i:
                    case "A":
                        temp="T"
                    case "T":
                        temp="A"
                    case "C":
                        temp="G"
                    case "G":
                        temp="C"
                    case _:
                        temp = i

                revc += [temp]
main()
print(''.join(revc))
