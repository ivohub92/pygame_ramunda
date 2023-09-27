def listas_filtradas(lista:list, key:str)->list:
    lista_aux= []
    for diccionario in lista:
        valor= diccionario[key]
        lista_aux.append(valor)
    return lista_aux

def lista_correcta(lista:list)->list:
    lista_aux=[]
    lista_correcta=[]
    for diccionario in lista:
        respuesta= diccionario['correcta']
        lista_aux.append(respuesta)
    for i in range(0,len(lista_aux)):
        valor=lista_aux[i]
        valor_correcta= lista[i][valor]
        lista_correcta.append(valor_correcta)
    return lista_correcta

