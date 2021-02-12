import random 

class Grafo:
    def __init__(self, es_dirigido = False):
        self.grafo = {}
        self.cantidad_vertices = 0
        self.es_dirigido = es_dirigido
    
    def __iter__(self):
        return iter(self.grafo.keys())

    def __len__(self):
        return self.cantidad_vertices
    
    def __str__(self):
        return str(self.grafo)

    def agregar_vertice(self, v):
        self.grafo[v] = {}
        self.cantidad_vertices += 1  

    def agregar_arista(self, v, w, peso = 0): 
        if v not in self.grafo or w not in self.grafo:
            raise KeyError("El/Los vertice/s no pertenece/n al grafo")

        self.grafo[v][w] = peso
        if not self.es_dirigido: self.grafo[w][v] = peso
    
    def obtener_vertice_random(self):
        return random.choice(list(self.grafo.keys()))

    def eliminar_vertice(self, v):
        if v not in self.grafo:
            raise KeyError("El vertice no pertenece al grafo")
        
        self.grafo.pop(v)
        self.cantidad_vertices -= 1

        for w in self.grafo:
            if v in self.grafo[w]:
                self.grafo[w].pop(v)

    def estan_unidos(self, v, w):
        if v not in self.grafo or w not in self.grafo:
            raise KeyError("El/Los vertice/s no pertenece/n al grafo")

        return v in self.grafo[w] 

    def existe_vertice(self, v):
        return v in self.grafo

    def obtener_vertices(self):
        return [v for v in self.grafo]

    def obtener_adyacentes(self, v):
        if v not in self.grafo:
            raise KeyError("El vertice no pertenece al grafo")

        return self.grafo[v]
    
    def peso_union(self, v, w):
        if v not in self.grafo or w not in self.grafo:
            raise KeyError("El/Los vertice/s no pertenece/n al grafo")

        return self.grafo[v][w]
    
#PRUEBAS (ELIMINAR)

'''
g = Grafo()

print(g)

#agrega vertices

g.agregar_vertice('a')
g.agregar_vertice('b')
g.agregar_vertice('c')
g.agregar_vertice('d')
g.agregar_vertice('e')
g.agregar_vertice('f')
g.agregar_vertice('g')
g.agregar_vertice('h')

print(g)

#agrega aristas

g.agregar_arista('a','b')

#obtener vertice random

print(g.obtener_vertice_random())

'''
 