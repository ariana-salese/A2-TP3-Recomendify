import csv
import biblioteca
import sys
import mensajes
from grafo import Grafo

ID = 'ID'
USER_ID = 'USER_ID'
TRACK_NAME = 'TRACK_NAME'	
ARTIST = 'ARTIST' 
PLAYLIST_ID	= 'PLAYLIST_ID'
PLAYLIST_NAME =	'PLAYLIST_NAME'
GENRES = 'GENRES'

SEP_CANCIONES = '>>>>'
SEP_CANCION_ARTISTA = ' - '

'''
-----------------------------------------------------------------
                     FUNCIONES AUXILIARES
-----------------------------------------------------------------
'''

def concatenar_cadenas(cadenas, indice_inicio, cadena_fin = None):
    '''
    documentacion
    '''
    cadena_resultante = ''

    for i in range(indice_inicio, len(cadenas)):
        cadena_actual = cadenas[i] 

        if cadena_actual == cadena_fin: return cadena_resultante[:-1], i

        cadena_resultante += cadena_actual + ' '

    return cadena_resultante[:-1], len(cadenas) - 1

def ciclo(grafo_canciones, n, cancion):
    '''
    documentacion
    '''
    ciclo = biblioteca.ciclo_n(grafo_canciones, n, cancion)
    
    for cancion_act, artista_act in ciclo: print(f"{cancion_act}{SEP_CANCION_ARTISTA}{artista_act} --> ")

    cancion_act, artista_act = cancion
    print(f"{cancion_act}{SEP_CANCION_ARTISTA}{artista_act}")

'''
-----------------------------------------------------------------
                           PRUEBAS
-----------------------------------------------------------------
'''

def leer_archivo_tsv():

    with open("mini_prueba.tsv") as archivo:
        lector = csv.DictReader(archivo, delimiter = '\t')

        for linea in lector:
            print(f"El ID es {linea[ID]}")

            print(f"El nombre de la playlist es {linea[PLAYLIST_NAME]}")

            print(f"El genero es {linea[GENRES]}")

def crear_grafo_usuarios():
    grafo_usuarios = biblioteca.crear_grafo_con_archivo("mini_prueba.tsv", USER_ID, PLAYLIST_NAME, TRACK_NAME, ARTIST)

    #print("ES EL GRAFO BIPARTITO:", es_bipartito(grafo_usuarios))

    print("Los vertices son:")
    for v in grafo_usuarios: print(v)
    print("\n")

    print("Los adyacentes del usuario sitevagalume son:")
    for i, a in enumerate(grafo_usuarios.obtener_adyacentes("sitevagalume")): print(i, a)
    print("\n")

    print("Los adyacentes de ('Eraser', 'Ed Sheeran') son:")
    for a in grafo_usuarios.obtener_adyacentes(('Eraser', 'Ed Sheeran')): print(a)
    print("\n")

    print("Los adyacentes de cada cancion de sitevagalume:")
    for i, a in enumerate(grafo_usuarios.obtener_adyacentes("sitevagalume")): 
        for j, b in enumerate(grafo_usuarios.obtener_adyacentes(a)):
            print(i, j, b)
    print("\n")

    print("Los adyacentes del usuario franciivaladao son:")
    for i, a in enumerate(grafo_usuarios.obtener_adyacentes("franciivaladao")): print(i, a)
    print("\n")

    print("Los adyacentes de cada cancion de franciivaladao:")
    for i, a in enumerate(grafo_usuarios.obtener_adyacentes("franciivaladao")): 
        for j, b in enumerate(grafo_usuarios.obtener_adyacentes(a)):
            print(i, j, b)
    print("\n")

    #print(grafo_usuarios, "fin")

def procesar_entrada_1():

    i = 0

    while True:
        try: entrada = input()
        except EOFError: break
        print(entrada)
        i += 1 
        if i == 5: 
            print("se trabo ups")
            break
        
def procesar_entrada_2():
    for linea in sys.stdin:
        linea = linea.rstrip("\n")
        cadenas = linea.split()
        print(linea)


def prueba_concatenar_cadenas():
    linea = "camino Don't Go Away - Oasis >>>> Quitter - Eminem"
    cadenas = linea.split()

    print(f"El comando es {cadenas[0]}")
    cancion, ultimo_indice = concatenar_cadenas(cadenas, 1, '-')
    print(f"El nombre de la cancion es: {cancion}")
    print(f"El ultimo indice es: {ultimo_indice}")
    print(f"La cadena que sigue entonces es {cadenas[ultimo_indice]} (SEPARADOR)")
    print(f"La cadena prox {cadenas[ultimo_indice + 1] }")

    origen, ultimo_indice = concatenar_cadenas(cadenas, 1, SEP_CANCIONES)
    destino, _ = concatenar_cadenas(cadenas, ultimo_indice + 1)

    print(f"El origen es: {origen.split(SEP_CANCION_ARTISTA)} \nEl destino es {destino.split(SEP_CANCION_ARTISTA)}")

def prueba_crear_grafo_canciones():
    grafo = biblioteca.crear_grafo_canciones_provisorio('mini_prueba.tsv', PLAYLIST_ID, TRACK_NAME, ARTIST)

    #print(grafo)
    for w in grafo.obtener_adyacentes(('Shape Of You', 'Ed Sheeran')): print(w)
    '''
    ('Eraser', 'Ed Sheeran')
    ('Castle On The Hill', 'Ed Sheeran')
    ('Dive', 'Ed Sheeran')
    ('Perfect', 'Ed Sheeran')
    ('Galway Girl', 'Ed Sheeran')
    ('Happier', 'Ed Sheeran')
    ("Hearts Don't Break Around Here", 'Ed Sheeran')
    '''
    for w in grafo.obtener_adyacentes(('Always','Bon Jovi')): print(w)
    '''
    ("It's My Life", 'Bon Jovi')
    ("Livin' On A Prayer", 'Bon Jovi')
    ('Misunderstood', 'Bon Jovi')
    ("I'll Be There For You", 'Bon Jovi')
    ('Thank You For Loving Me', 'Bon Jovi')
    ('You Give Love A Bad Name', 'Bon Jovi')
    ('Bed Of Roses', 'Bon Jovi')
    ('Wanted Dead Or Alive', 'Bon Jovi')
    ('Never Say Goodbye', 'Bon Jovi')
    ('All I Wanna do Is You', 'Bon Jovi')
    ('Blaze Of Glory', 'Bon Jovi')
    ('Crazy', 'Bon Jovi')
    ('I Thank You', 'Bon Jovi')
    '''

def prueba_ciclo_n():
    grafo = biblioteca.crear_grafo_canciones_provisorio('mini_prueba.tsv', PLAYLIST_ID, TRACK_NAME, ARTIST)

    ciclo_3 = biblioteca.ciclo_n(grafo, 3, ('Dive', 'Ed Sheeran'))

    print(ciclo_3)
    print(f"El origen (('Dive', 'Ed Sheeran')) es adyacente al ultimo vertice (('Castle On The Hill', 'Ed Sheeran')): {('Dive', 'Ed Sheeran') in grafo.obtener_adyacentes((('Castle On The Hill', 'Ed Sheeran')))}")

    ciclo_4 = biblioteca.ciclo_n(grafo, 4, ('Dive', 'Ed Sheeran'))

    print(ciclo_4)
    print(f"El origen (('Dive', 'Ed Sheeran')) es adyacente al ultimo vertice (('Shape Of You', 'Ed Sheeran')): {('Dive', 'Ed Sheeran') in grafo.obtener_adyacentes((('Shape Of You', 'Ed Sheeran')))}")

def prueba_rango():
    #creo grafo
    g = Grafo()

    #agrego vertices
    g.agregar_vertices(['a', 'b', 'c', 'd', 'e','f','g'])

    #agrego aristas
    g.agregar_arista('a','b')
    g.agregar_arista('a','c')
    g.agregar_arista('e','b')
    g.agregar_arista('d','c')
    g.agregar_arista('d','e')
    g.agregar_arista('d','g')
    g.agregar_arista('d','f')
    g.agregar_arista('f','e')

    print(f"GRAFO: {g}")
    print('')

    #defino origen

    origen = 'a'

    print(f">>> A rango 1 se encuentran: {biblioteca.rango(g, 1, origen)} vertices || RESP. CORRECTA = [b, c]")

    #print(f">>> A rango 2 se encuentran: {biblioteca.rango(g, 2, origen)} vertices || RESP. CORRECTA = [d, e]")

    #print(f">>> A rango 3 se encuentran: {biblioteca.rango(g, 3, origen)} vertices || RESP. CORRECTA = [e, d, f, g]")

    #print(f">>> A rango 4 se encuentran: {biblioteca.rango(g, 4, origen)} vertices || RESP. CORRECTA = [b, e, d, c, f, g]")



def main():
    #leer_archivo_tsv()
    #crear_grafo_usuarios()
    #procesar_entrada_1()
    #procesar_entrada_2() #clearly nicer 
    #prueba_concatenar_cadenas()
    #prueba_crear_grafo_canciones()
    #prueba_ciclo_n()
    prueba_rango()

main()