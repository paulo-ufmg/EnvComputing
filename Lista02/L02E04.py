#4. (FIB) A sequência de Fibonacci pode ser utilizada para estimar a população de coelhos a partir de uma quantidade de meses. Considerando isso. faça um
#programa que leia um arquivo contendo dois inteiros (n e k) separados por espaço
#onde n corresponde a quantidade de meses e 
#k corresponde a quantidade de pares de filhotes de coelhos que cada casal (par) de coelhos adultos conseguem gerar por mês (ao invés de 1 par, como é normalmente na sequência de Fibonacci). 
#Além disso, os coelhos filhotes demoram 1 mês para se tornarem adultos e capazes de se reproduzir. 
# Sendo assim, o programa deve retornar o total de pares de coelhos depois de n meses, considerando inicialmente que existem 1 par de coelhos filhotes no primeiro mês [4].
#Entrada: 5 3
#Saida: 19

import re,os
nome_arquivo = 'dados' + os.sep + 'arquivo_L02E04_string_de_inteiros.txt'
adultos = 0 # Coelho adulto em condição de reproduzir
laparos = 0  # filhotes recêm nascidos
em_crescimento = 1  # Coelhos que tranformam em adutos depois de 1 mes
contador =0   # Contagem de meses
tempo = {0:(0,1)} #Dicionário para registro de evolução do tempo 1: Primeiro mês (x,y) x Coelhos Adultos e y coelhos filhotes


n =int() #Quantidades de meses a ser avaliada
k = int() #Numero de filhotes gerados

#===============================================================
def leia_n_k(n,k): #Leitura dos valores n, k é feita em arquivo
    global nome_arquivo
    with open (nome_arquivo) as arq:
        line = arq.read()
        return re.findall("[0-9]+", line)

n, k = leia_n_k(n,k) #n e k são recebido como str
n = int(n);k = int(k)
#--------------------------

#========================================Processo manual
for i in range(n):
    contador += 1
    laparos = k * adultos
    adultos += em_crescimento
    em_crescimento = laparos
    tempo[contador] = adultos, laparos
print("┌─────┬───────┬────────┐")
print("│Mês  │Coelhos│Filhotes│")
print("├─────┼───────┼────────┤")
for i in tempo.keys():
    print("│",str(i).ljust(3),"│",str(tempo[i][0]).ljust(5),"│",str(tempo[i][1]).ljust(6),"│")

print("└─────┴───────┴────────┘")
#--------------------
print (f"Total de coelhos: {tempo[n][0]}")




