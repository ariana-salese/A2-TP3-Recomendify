from grafo import Grafo
from csv import DictReader


def crear_grafo_con_archivo(ruta_archivo, param_1, param_2, param_3):
    '''
    Recibe un archivo tsv y tres parametros del header. Crea y devuelve un grafo
    bipartito que relaciona el parametro 1 con la tupla (param_2, param_3)
    '''

    grafo = Grafo(False)

    with open(ruta_archivo) as archivo:
        lector = DictReader(archivo, delimiter = '\t')

        for linea in lector:
            dato_1, dato_2 = linea[param_1], (linea[param_2], linea[param_3])

            if dato_1 not in grafo: grafo.agregar_vertice(dato_1)
            if dato_2 not in grafo: grafo.agregar_vertice(dato_2)

            if not grafo.estan_unidos(dato_1, dato_2): grafo.agregar_arista(dato_1, dato_2)
    
    return grafo