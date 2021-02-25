from grafo import Grafo
from cola import Cola
from pila import Pila
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


def crear_grafo_canciones_provisorio(ruta_archivo, param_1, param_2, param_3):
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

            if vertice not in grafo: grafo.agregar_vertice(vertice)

            grupo_actual = datos.get(grupo, [])

            for w in grupo_actual: 
                if not grafo.estan_unidos(vertice, w):
                    grafo.agregar_arista(vertice, w)
            
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

# def _rango(grafo, n, origen, v, visitados, n_actual, en_rango):
#     '''

#     '''
#     print("________________________")
#     print(f"EL ORIGEN ES {v}")
#     print(f"n actual es: {n_actual}")
#     visitados.add(v)

#     if n == len(en_rango): 
#         print(f"visitados: {visitados}")
#         if v in en_rango: 
#             print("Ya lo visite, devuelvo 0")
#             return cantidad
#         print("NO lo visite, devuelvo 1")
#         return cantidad + 1 

#     n_actual += 1

#     for w in grafo.obtener_adyacentes(v):
#         if w in visitados: continue
#         print(f"Previo a sumar cantidad = {cantidad}")
#         cantidad = _rango(grafo, n, origen, w, n_actual, cantidad)
    
#     print(f"El origen es: {v}")
#     print("Devuelvo cantidad")
#     return cantidad

# def _rango(grafo, n, origen):
#     '''

#     '''
#     en_rango = []
#     visitados = set()
#     padres = {}
#     orden = {}
#     q = Cola()
#     visitados.add(origen)
#     padres[origen] = None 
#     orden[origen] = 0 
#     q.encolar(origen)

#     while not q.esta_vacia():
#         v = q.desencolar()
#         for w in grafo.obtener_adyacentes(v): 
#             if w in visitados: continue
#             visitados.add(w)
#             padres[w] = v 
#             orden[w] = orden[v] + 1
#             q.encolar(w)

#             if orden[w] == n and w not in en_rango: en_rango.append(w)
	

#     return en_rango

def _rango(grafo, n, n_actual, v, padre, en_rango):

    print("-------------")
    print(f"origen: {v}")
    print(f"n_actual: {n_actual}")
    print(padre)
    print('')

    if n_actual > n:
        print("Me pase, goodbye")
        return en_rango

    if n == n_actual:
        if v not in en_rango: en_rango.append(v)
        print(f"Devuelvo: {en_rango}")
        return en_rango

    n_actual += 1

    for w in grafo.obtener_adyacentes(v):
        print(f"El adyacente es: {w}")
        if w in padre: print(f"Su padre es: {padre[w]}")
        else: print("No tiene padre")
        if w in padre and (padre[v] == w or padre[w] == None): continue
        print("pase")
        padre[w] = v
        _rango(grafo, n, n_actual, w, padre, en_rango)

    print("fin")
    return en_rango



def rango(grafo, n, v):
    '''

    '''
    padre = {}
    padre[v] = None

    return _rango(grafo, n, 0, v, padre, [])


