#!/usr/bin/python3

import graphutil
import sys
import strutil

# HEADERS
USER_ID = 'USER_ID'
TRACK_NAME = 'TRACK_NAME'	
ARTIST = 'ARTIST' 
PLAYLIST_ID	= 'PLAYLIST_ID'
PLAYLIST_NAME = 'PLAYLIST_NAME'

# COMANDOS
CAMINO = "camino"
MAS_IMPORTANTES = "mas_importantes"
RECOMENDACION = "recomendacion"
CICLO = "ciclo"
RANGO = "rango"
CLUSTERING = "clustering"

# CARACTERES 
SEP_CANCIONES = '>>>>'
SEP_CANCION_ARTISTA = ' - '
DECIMALES_CLUSTERING = 3

# INDICES
INDICE_CANCION = 0
INDICE_COMANDO = 0
INDICE_ARTISTA = 1
INDICE_N = 1
INDICE_USUARIO_O_CANCION = 1

#ELEMENTOS
CANCIONES = 'canciones'

#MENSAJES
ENOENT_COMANDO = "No existe el comando ingresando"
ENOENT_RECORRIDO = "No se encontro recorrido"

'''
-----------------------------------------------------------------
                    FUNCIONES AUXILIARES
-----------------------------------------------------------------
'''

def es_cancion(v):
    return type(v) is tuple

def es_usuario(v):
    return type(v) is str

'''
-----------------------------------------------------------------
                          COMANDOS
-----------------------------------------------------------------
'''

def camino(grafo_usuarios, origen, destino):
    '''
    Recibe un grafo bipartito que relaciona usuarios con canciones, y dos canciones, una de 
    origen y otra de destino. Imprime el camino más corto entre la canción de origen y destino.
    Tanto si el origen o destino no son canciones válidas como si no existe camino entre las 
    canciones, se imprimirá el error correspondiente.
    '''
    
    if not (grafo_usuarios.existe_vertice(origen) and grafo_usuarios.existe_vertice(destino)):
    	print("Tanto el origen como el destino deben ser canciones")
    	return

    recorrido = graphutil.camino_minimo(grafo_usuarios, origen, destino)

    if not recorrido: 
    	print("No se encontro recorrido")
    	return

    print(f"{origen[0]} - {origen[1]}", end='')

    for i in range(1,len(recorrido)):

    	print(" --> ", end='')

    	if i%4 == 0:
    		print("donde aparece", end='')
    	if i%4 == 1:
    		print("aparece en playlist", end='')
    	if i%4 == 2:
    		print("de", end='')  		
    	if i%4 == 3:
    		print("tiene una playlist", end='')

    	print(" --> ", end='')
    	
    	if i%4 == 0:
    		print(f"{recorrido[i][0]} - {recorrido[i][1]}", end='')
    	else:
    		print(f"{recorrido[i]}", end='')

    print("")


def mas_importantes(grafo_usuarios, n, pagerank):
    '''
    Imprime por pantalla las canciones más importantes según el algoritmo "Pagerank"
    '''
        
    if not pagerank:
        pagerank = graphutil.pagerank(grafo_usuarios)

    strutil.imprimir_lista_de_tuplas(pagerank[:n], SEP_CANCION_ARTISTA, "; ")

    return pagerank


def recomendacion(grafo_usuarios, elemento, n, lista):
    '''
    Si el elemento recibido es canciones se imprime una lista de canciones que son similares
    a las recibidas en las lista. 
    Si el elemento recibido es usuarios se devuelven usuarios similares. 
    '''
    if elemento == CANCIONES: funcion = es_cancion
    else: funcion = es_usuario

    recomendaciones = graphutil.pagerank_personzalido(grafo_usuarios, lista, n, funcion)

    if elemento == CANCIONES: strutil.imprimir_lista_de_tuplas(recomendaciones, SEP_CANCION_ARTISTA, "; ")
    else: strutil.imprimir_lista(recomendaciones, '; ')


def ciclo(grafo_canciones, n, cancion):
    '''
    Recibe un grafo de canciones, una cancion y un largo n, e imprime un ciclo
    de largo n cuyo origen es la cancion con el formato:

    cancion_a - artista_a --> cancion_b - artista_b... 

    Si el ciclo no existe imprime el mensaje: 'No se encontro recorrido'.
    '''
    
    if not grafo_canciones.existe_vertice(cancion):
        print(ENOENT_RECORRIDO)
        return 

    ciclo = graphutil.ciclo_largo_n(grafo_canciones, n, cancion)

    if ciclo is None: 
        print(ENOENT_RECORRIDO)
        return 
    
    strutil.imprimir_lista_de_tuplas(ciclo, SEP_CANCION_ARTISTA, " --> ", True)

'''
-----------------------------------------------------------------
                  PROCESAMIENTO DE ENTRADA
-----------------------------------------------------------------
'''

def procesar_entrada(ruta_archivo, pagerank):

    grafo_usuarios = None 
    grafo_canciones = None

    for linea in sys.stdin:
        linea = linea.rstrip("\n")
        cadenas = linea.split()
        comando = cadenas[INDICE_COMANDO]

        if comando in (CAMINO, RECOMENDACION, MAS_IMPORTANTES) and grafo_usuarios is None: 
            grafo_usuarios = graphutil.crear_grafo_bipartito_con_archivo(ruta_archivo, USER_ID, PLAYLIST_NAME, TRACK_NAME, ARTIST)

        if comando in (CICLO, CLUSTERING, RANGO) and grafo_canciones is None:
            grafo_canciones = graphutil.crear_grafo_con_archivo(ruta_archivo, PLAYLIST_NAME, TRACK_NAME, ARTIST)

        if comando == CAMINO:
            origen, ultimo_indice = strutil.concatenar_cadenas(cadenas, 1, SEP_CANCIONES)
            destino, _ = strutil.concatenar_cadenas(cadenas, ultimo_indice + 1)

            origen_splitted = origen.split(SEP_CANCION_ARTISTA)
            destino_splitted = destino.split(SEP_CANCION_ARTISTA)

            artista_origen = artista_destino = None
            nombre_cancion_destino = nombre_cancion_origen = None

            if len(origen_splitted) == 2 and len(destino_splitted) == 2:
	            nombre_cancion_origen, artista_origen = origen_splitted
	            nombre_cancion_destino, artista_destino = destino_splitted

            camino(grafo_usuarios, (nombre_cancion_origen, artista_origen), (nombre_cancion_destino, artista_destino))
        
        elif comando == MAS_IMPORTANTES:
            pagerank = mas_importantes(grafo_usuarios, int(cadenas[INDICE_N]), pagerank)

        elif comando == RECOMENDACION:
            lista = []
            ultimo_indice = 2

            while ultimo_indice != len(cadenas) - 1:

                cancion, ultimo_indice = strutil.concatenar_cadenas(cadenas, ultimo_indice + 1, SEP_CANCIONES)
                nombre, artista = cancion.split(SEP_CANCION_ARTISTA)
        
                lista.append((nombre, artista))

            recomendacion(grafo_usuarios, cadenas[1], int(cadenas[2]), lista)

        elif comando == CICLO:
            cancion, _ = strutil.concatenar_cadenas(cadenas, 2)
            nombre_cancion, artista = cancion.split(SEP_CANCION_ARTISTA)

            ciclo(grafo_canciones, int(cadenas[INDICE_N]), (nombre_cancion, artista))
    
        elif comando == RANGO:
            cancion, _ = strutil.concatenar_cadenas(cadenas, 2)
            
            nombre_cancion, artista = cancion.split(SEP_CANCION_ARTISTA)

            print(graphutil.cantidad_en_rango(grafo_canciones, int(cadenas[INDICE_N]), (nombre_cancion, artista)))
        
        elif comando == CLUSTERING:
            if (len(cadenas)) == 1: 
                coeficiente = graphutil.clustering_grafo(grafo_canciones)
            else:
                cancion, _= strutil.concatenar_cadenas(cadenas, 1)
                nombre_cancion, artista = cancion.split(SEP_CANCION_ARTISTA)

                coeficiente = graphutil.clustering_vertice(grafo_canciones, (nombre_cancion, artista))
        
            print(strutil.redondear(coeficiente, DECIMALES_CLUSTERING))

        else: print(ENOENT_COMANDO)

'''
-----------------------------------------------------------------
                     PROGRAMA PRINCIPAL
-----------------------------------------------------------------
'''

def main(ruta_archivo):

    pagerank = []

    procesar_entrada(ruta_archivo, pagerank)


main(sys.argv[1])