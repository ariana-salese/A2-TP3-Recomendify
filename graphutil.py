from grafo import Grafo
from cola import Cola
from csv import DictReader
import sys
import csv
from strutil import redondear
from datetime import datetime

csv.field_size_limit(sys.maxsize)

D = 0.85
ITERACIONES_PRP = 350 #PRP = Page Rank Personalizado
RANDOM_WALKS_PRP = 50 

def crear_grafo_bipartito_con_archivo(ruta_archivo, param_1, param_2, param_3, param_4):
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
            
            if not grafo.existe_vertice(vertice_1): grafo.agregar_vertice(vertice_1)
            if not grafo.existe_vertice(vertice_2): grafo.agregar_vertice(vertice_2)

            if not grafo.estan_unidos(vertice_1, vertice_2): grafo.agregar_arista(vertice_1, vertice_2, peso)
   
    return grafo


def crear_grafo_con_archivo(ruta_archivo, param_1, param_2, param_3):
    '''
    Recibe un archivo tsv y tres parametros de su header. Devuelve un grafo que relaciona
    la tupla (param_2, param_3) de cada linea si param_1 es igual en estas. 
    '''
    grafo = Grafo()
    datos = {}

    with open(ruta_archivo) as archivo:
        lector = DictReader(archivo, delimiter = '\t')
        
        for linea in lector:
            grupo = linea[param_1]
            vertice = (linea[param_2], linea[param_3])

            if not grafo.existe_vertice(vertice): grafo.agregar_vertice(vertice)

            grupo_actual = datos.get(grupo, [])

            for w in grupo_actual: 
                if w == vertice: continue

                if not grafo.estan_unidos(vertice, w):
                    grafo.agregar_arista(vertice, w)
            
            if vertice not in grupo_actual: 
                grupo_actual.append(vertice)
                datos[grupo] = grupo_actual

    return grafo


def _ciclo_largo_n(grafo, n, origen, v, visitados, camino):
    '''
    Recibe un grafo, un origen, un largo n y un vertice actual. Devuelve una 
    lista de vertices que representa un ciclo de largo n que comienza en el
    origen. Si este no existe, devuelve None. 
    '''    
    visitados.add(v)
    camino.append(v)

    if len(camino) == n: 
        if origen in grafo.obtener_adyacentes(v): return camino
        return None
    
    for w in grafo.obtener_adyacentes(v):
        if w in visitados: continue

        solucion = _ciclo_largo_n(grafo, n, origen, w, visitados, camino)

        if solucion is not None: return solucion
                 
        camino.pop()
        visitados.remove(w)
    
    return None
    

def ciclo_largo_n(grafo, n, origen):
    '''
    Recibe un grafo, un largo n y un vertice origen. Devuelve una lista de vertices
    que representa un ciclo de largo n que comienza en el origen. Si este no existe,
    devuelve None. 
    '''
    camino = []
    visitados = set()

    return _ciclo_largo_n(grafo, n, origen, origen, visitados, camino)


def camino_minimo(grafo, origen, destino):

    '''
    Recibe un grafo, un vértice de origen y uno de destino. 
    Devuelve una lista del recorrido mínimo, donde se incluye
    el peso entre las aristas.
    Si no se encuentra camino devuelve None.
    '''

    visitados = set()
    padre = {}
    q = Cola() 
    visitados.add(origen)
    padre[origen] = None 
    q.encolar(origen)
    encontre_destino = False

    while not q.esta_vacia() and not encontre_destino: 
        v = q.desencolar()
        for w in grafo.obtener_adyacentes(v): 
            if w not in visitados: 
                visitados.add(w)
                padre[w] = v
                q.encolar(w)
                if w == destino: 
                    encontre_destino = True
                    break

    if not encontre_destino: return None

    return reconstruir_camino(grafo, padre, destino)
    

def reconstruir_camino(grafo, padre, destino):
    '''
    Reconstuye el camino desde el vertice cuyo padre es None hasta el destino.
    Devuelve una lista con los vertices recorridos incuyendo los pesos que los 
    une.
    '''
    
    destino_actual = destino
    recorrido = []

    while destino_actual is not None:
        recorrido.append(destino_actual)

        if padre[destino_actual] is not None: 
            recorrido.append(grafo.peso_union(destino_actual, padre[destino_actual]))
        
        destino_actual = padre[destino_actual]

    return recorrido[::-1]


def cantidad_en_rango(grafo, n, origen):
    '''
    Devuelve la cantidad de vertices que se encuentran exactamente a n aristas 
    del vertice v. 
    '''

    orden = {}
    orden[origen] = 0

    cola = Cola()
    cola.encolar(origen)
 
    vertices = 0

    while not cola.esta_vacia():
        v = cola.desencolar()

        for w in grafo.obtener_adyacentes(v):
            if w in orden: continue

            orden[w] = orden[v] + 1

            if orden[w] > n: return vertices 
            if orden[w] == n: vertices += 1

            cola.encolar(w)

    return vertices


def clustering_vertice(grafo, vertice):
    '''
    Devuelve el coficiente de clustering del vertice.
    '''
    ady = grafo.obtener_adyacentes(vertice)
    cant_ady = len(ady)
    cant_conecciones = 0

    if cant_ady < 2: return 0

    for w in ady:
        for x in grafo.obtener_adyacentes(w):   
            if x in ady: cant_conecciones += 1

    return (cant_conecciones) / (cant_ady * (cant_ady - 1))


def clustering_grafo(grafo):
    '''
    Devuelve el coficiente de clustering del grafo.
    '''
    coeficientes = 0

    for v in grafo:
        coeficientes += clustering_vertice(grafo, v)
    
    return coeficientes / len(grafo)


def pagerank(grafo):
    '''
    Devuelve una lista con el pagerank de cada nodo
    '''

    dict_pgrnk = {}

    #Inicializo el diccionario
    for nodo in grafo:
       dict_pgrnk[nodo] = 1 / len(grafo)

    padres = {}

    for nodo in grafo:
        padres[nodo] = []

    for nodo in grafo:
        for hijo in grafo.obtener_adyacentes(nodo):
            padres[hijo].append(nodo)

    result_raw = _pagerank(grafo, dict_pgrnk, padres, 100)

    result = {}

    for clave, valor in result_raw.items():
        if isinstance(clave, tuple):
            result[clave] = valor

    return [dato[0] for dato in sorted(result.items(), key=lambda x: x[1], reverse=True)]


def _pagerank(grafo, dict_pgrnk, padres, n, cont = 0):

    new_dict_pgrnk = {}

    for nodo in dict_pgrnk:
        pgrnk_sum = 0
        for padre in padres[nodo]:
            pgrnk_sum += dict_pgrnk[padre] / len(grafo.obtener_adyacentes(padre))
        new_dict_pgrnk[nodo] = ((1 - D) / len(grafo)) + D * pgrnk_sum

    cont+= 1
        
    if cont < n:
        return _pagerank(grafo, new_dict_pgrnk, padres, n, cont)

    return new_dict_pgrnk


def random_walk(grafo, v, rango, rango_act, valores):
    '''
    Realiza un camino aleatorio y define valores del 0 a 1
    segun cuan probable es llegar a estos vertices desde el vertice v.
    '''

    if rango_act == rango: return valores

    adyacentes_v = grafo.obtener_adyacentes(v)

    if rango_act == 0:
        valor_a_sumar = 1 / len(adyacentes_v)
    else:
        valor_a_sumar = valores[v] / len(adyacentes_v)

    w = grafo.obtener_adyacente_random(v)

    valores[w] = valores.get(w, 0) + valor_a_sumar

    return random_walk(grafo, w, rango, rango_act + 1, valores)


def pagerank_personzalido(grafo, vertices, n, pertenece = None):
    '''
    Devuelve una lista de n vertices que mas se relacionan con los vertices pasados 
    por parametro
    '''

    valores_totales = {}

    for v in vertices:
        valores = {}

        for i in range(RANDOM_WALKS_PRP): #Varios random walks por cada vértice

            valores_actuales = random_walk(grafo, v, ITERACIONES_PRP, 0, valores)

            for w, valor in valores_actuales.items():
                valores_totales[w] = valores_totales.get(w, 0) + valor  

    valores_finales = {} #Elimino los dados por parámetro

    for v, valor in valores_totales.items():
        if v not in vertices:
            valores_finales[v] = valor

    aux = list(valores_finales.items())
    aux.sort(key = lambda x: x[1] , reverse = True) 

    if pertenece is not None:
        vertices = [v for v, _ in aux if pertenece(v)][:n]
    else:
        vertices = [v for v, _ in aux][:n]

    return vertices

