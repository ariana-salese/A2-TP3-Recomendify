from grafo import Grafo
from csv import DictReader

def crear_grafo_con_archivo(ruta_archivo, param_1, param_2, param_3, param_4):
    '''
    Recibe un archivo tsv y cuatro parametros del header. Crea y devuelve un grafo
    bipartito que relaciona el param_1 con la aristas cuyo peso es param_2
    a la tupla (param_3, param_4)
    '''

    grafo = Grafo(False)

    with open(ruta_archivo) as archivo:
        lector = DictReader(archivo, delimiter = '\t')

        for linea in lector:
            vertice_1, peso, vertice_2,  = linea[param_1], linea[param_2], (linea[param_3], linea[param_4])

            if vertice_1 not in grafo: grafo.agregar_vertice(vertice_1)
            if vertice_2 not in grafo: grafo.agregar_vertice(vertice_2)

            if not grafo.estan_unidos(vertice_1, vertice_2): grafo.agregar_arista(vertice_1, vertice_2, peso)
    
    return grafo

'''
IDEA GENERAL:
1. Si encontre solucion devuelvo el camino
2. Agrego un adyacente, si no es solucion posible vuelvo
3. No existe solucion
'''

def _ciclo_n(grafo, n, origen, v, visitados, camino):
    '''
    Doc
    '''
    visitados.add(v)
    camino.append(v)

    if len(camino) == n: 
        if origen in grafo.obtener_adyacentes(v): return camino
        return None
    
    for w in grafo.obtener_adyacentes(v):
        if w in visitados: continue

        if _ciclo_n(grafo, n, origen, w, visitados, camino) in not None: return solucion

    camino.remove(v)
    visitados.pop(v)
    
    return None
    

def ciclo_n(grafo, n, origen):
    '''
    Doc
    '''
    camino = []
    visitados = set()

    return _ciclo_n(grafo, n, origen, origen, visitados, camino)

    


