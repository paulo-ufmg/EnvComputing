"""
14. Faça um programa que leia um arquivo contendo várias linhas onde cada linha
possui uma string a separada por espaço de uma string c, onde a é um aminoácido
em um determinado formato (“nome”,”sigla”,”letra”) e c é o formato a ser
convertido de a. O programa deve retornar todas as conversões de a para o formato
c. Segue Tabela de aminoácidos.
Exemplo entrada:
ALA nome
V sigla
Tirosina letra
Saída:
Alanina
Val
Y
"""
import os


def traduz(proteina,tipo_retorno):
    nome = ["Alanina","Arginina","Asparagina","Ácido Aspártico","Cisteína","Glutamina","Ácido Glutâmico","Glicina","Histidina","Isoleucina","Leucina","Lisina","Metionina","Fenilalanina","Prolina","Serina","Treonina","Triptofano","Tirosina","Valina"]
    sigla = ["ALA","ARG","ASN","ASP","CYS","GLN","GLU","GLY","HIS","ILE","LEU","LYS","MET","PHE","PRO","SER","THR","TRP","TYR","VAL"]
    letra = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]

    if(len(proteina) == 1): 
        indice = letra.index(proteina) #identifica o indice da proteina
    else: indice = sigla.index(proteina) if(len(proteina)==3) else nome.index(proteina)

    if(tipo_retorno == "letra"):
        return letra[indice]    
    else: return sigla[indice] if tipo_retorno=="sigla" else nome[indice]
        
ac = []
#Lendo a respectivas proteinas no arqulivo de entrada
with open ("dados"+ os.sep + "arquivo_L02E14_entrada.txt", "r") as arq:
    while True:
        line = arq.readline()
        if not line: break #interrompe ao final do arquivo
        if line.strip() == "": continue  # Ignorar linhas em branco
        ac.append(line.strip("\n").split())
for el in ac:
    print(traduz(el[0],el[1]))



