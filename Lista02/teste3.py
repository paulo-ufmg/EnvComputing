
# map function
# Calcula a media das metricas 

metrica1 = [19.25, 54.32, 89.23]
metrica2 = [19.45, 54.35, 89.33]
metrica3 = [19.22, 54.29, 89.19]
#===========================================
def media_metrica(n1,n2,n3):
    """
    Retorna a media de 3 medidas
    """
    return "{:.2f}".format((n1 + n2 +n3 ) / 3) #Retorna a media com arredondamento de dois decimais
#-------------------------------------------
objeto_map = map(media_metrica, metrica1, metrica2, metrica3) #Retorna um objeto tipo <class 'map'>
for n in objeto_map: 
    print(n)             # O objeto <class 'map'> é iterável somente uma vez, depois fica fazio   
print(list(objeto_map))  # Esta instrução vai retornar uma lista vazia

#Pode-se Converter o objeto <class 'map'> em uma lista na primeira iterativdade
objeto_map = map(media_metrica, metrica1, metrica2, metrica3) #Retorna um objeto tipo <class 'map'>
media = list(objeto_map)
print(f"média das metricas: {media}") 






