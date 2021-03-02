from random import choice

ERROR_VERTICES = KeyError("El/Los vertice/s no pertenece/n al grafo")
ERROR_VERTICE = KeyError("El vertice no pertenece al grafo")
ERROR_UNION = Exception("Los vertices no se encuntran unidos")

class Grafo:
    '''
    Representa un grafo, el cual podra ser dirigido o no.
    '''
    def __init__(self, es_dirigido = False):
        '''
        Crea el grafo vacio, dirigido si se recibe True.
        '''
        self.grafo = {}
        self.es_dirigido = es_dirigido
    
    def __iter__(self):
        '''
        Itera por los vertices del grafo.
        '''
        return iter(self.grafo)

    def __len__(self):
        '''
        Devuelve la cantidad de vertices del grafo.
        '''
        return len(self.grafo)
    
    def __str__(self):
        '''
        Imprime el grafo con el formato {vertice_i: {adyacente_j: peso_i_j}}}.
        '''
        return str(self.grafo)
  
    def existe_vertice(self, v):
        '''
        Devuelve True si el vertice v pertence al grafo.
        '''
        return v in self.grafo
 
    def agregar_vertice(self, v):
        '''
        Agrega el vertice v al grafo.
        '''
        self.grafo[v] = {}
    
    def agregar_vertices(self, vv):
        '''
        Recibe una lista de vertices y los agrega al grafo
        '''
        for v in vv: self.agregar_vertice(v)

    def agregar_arista(self, v, w, peso = 0):
        '''
        Agrega la arista v--peso--w o v<-peso->w en caso de ser dirigido.
        Si no se recibe peso se le asiga peso cero.

        Levanta error si: uno o ambos vertices no existen.
        '''
        if v not in self.grafo or w not in self.grafo: raise ERROR_VERTICES

        self.grafo[v][w] = peso
        if not self.es_dirigido: self.grafo[w][v] = peso

    def eliminar_vertice(self, v):
        '''
        Elimina el vertice del grafo y todas las aristas con las que se
        relaciona.

        Levanta error si: el vertice v no existe
        '''
        if v not in self.grafo: raise ERROR_VERTICE

        self.grafo.pop(v)

        for w in self.grafo:
            if v in self.grafo[w]:
                self.grafo[w].pop(v)

    def estan_unidos(self, v, w):
        '''
        Devuelve True si v y w estan unidos.

        Levanta error si: uno o ambos vertices no existen.
        '''
        if v not in self.grafo or w not in self.grafo: raise ERROR_VERTICES

        return w in self.grafo[v] 
    
    def obtener_vertice_random(self):
        '''
        Devuelve un vertice aleatorio.
        '''
        return choice(list(self.grafo))  

    def obtener_vertices(self):
        '''
        Devuelve una lista con todos lo vertices del grafo.
        '''
        return list(self.grafo)
    
    def obtener_aristas(self):
        '''
        Devuelve una lista de tuplas con todos las aristas del grafo con el 
        formato (v, w, peso) = v--peso->w (dirigido) o v<-peso->w (no dirigido).
        '''
        aristas = []

        for v in self.grafo:
            for w in self.grafo[v]:
                arista = (v, w, self.grafo[v][w])
                if self.es_dirigido: 
                    aristas.append(arista)

                elif not self.es_dirigido and (w, v, self.grafo[v][w]) not in aristas: 
                    aristas.append(arista)
        
        return aristas

    def obtener_adyacentes(self, v):
        '''
        Devuelve una lista con los adyacentes de v. 

        Levanta error si: el vertice v no existe
        '''
        if v not in self.grafo: raise ERROR_VERTICE

        return self.grafo[v]
    
    def peso_union(self, v, w):
        '''
        Devuelve el peso de la arista que une a v y w.

        Levanta error si:
        - uno o ambos vertices no existen.
        - v y w no se encuentran unidos. 
        '''

        if v not in self.grafo or w not in self.grafo: raise ERROR_VERTICES

        if not self.estan_unidos(v, w): raise ERROR_UNION

        return self.grafo[v][w]

g = Grafo(True)
g.agregar_vertice('a')
g.agregar_vertice('b')
g.agregar_arista('a', 'b')
print(g.estan_unidos('a','b'))
