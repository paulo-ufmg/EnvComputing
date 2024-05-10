# filter function
# Filtra os numeros pares de uma lista

numeros = [2,3,4,7,9,22,13,14]
#===========================================
def num_par(num):
    """
    Retorna True se o argumento for par
    """
    return num % 2 == 0
#-------------------------------------------
pares = filter(num_par, numeros) #Retorna um objeto tipo <class 'filter'>
for n in pares:
    print(n)

#ou
#Converte o objeto <class 'filter'> em uma lista
print(f"Lista dos numeros pares: {list(filter(num_par, numeros))}") 






