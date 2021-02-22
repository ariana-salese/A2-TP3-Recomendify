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

def camino_minimo(grafo, origen, destino):

    '''
    Recibe un grafo, un vértice de origen y uno de destino. 
    Devuelve una lista del recorrido mínimo, donde se incluye
    el peso entre las aristas.
    Si no se encuentra camino devuelve None.
    '''

    visitados = set()
    padres = {}
    q = Cola()
    visitados.add(origen)
    padres[origen] = None
    destino_encontrado = False
    q.encolar(origen)
    
    while not (q.esta_vacia() or destino_encontrado):

        v = q.desencolar()

        for w in grafo.obtener_adyacentes(v):

            if destino_encontrado: break

            if w not in visitados:

                visitados.add(w)
                padres[w] = (v, grafo.peso_union(v,w))
                q.encolar(w)

                if w == destino: destino_encontrado = True

    if not destino_encontrado:
        return None

    s = Pila()
    s.apilar(destino)
    #Apilo los vértices desde el destino al origen para porder invertir el orden
    while s.ver_tope() != origen: 

        actual = s.ver_tope()
        padre_actual = padres[actual][0]

        s.apilar(padres[actual][1]) #Apilo el peso entre el actual y su padre
        s.apilar(padre_actual) #Apilo el padre

    recorrido = []

    while not s.esta_vacia():
        recorrido.append(s.desapilar())

    return recorrido