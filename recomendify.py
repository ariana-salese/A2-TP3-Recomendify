import graphutil
import sys
import mensajes
import strutil
from datetime import datetime

# HEADERS
'''
Comento los que no se si vamos a usar, cuando nos organizamos borramos lo que 
sobra
ID = 'ID'
GENRES = 'GENRES'
'''
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

# INDICES
INDICE_CANCION = 0
INDICE_ARTISTA = 1
INDICE_N = 1
INDICE_USUARIO_O_CANCION = 1

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

def mas_importantes(grafo_canciones, n, pagerank):
    '''
    Imprime por pantalla las canciones más importantes según el algoritmo "Pagerank"
    '''
        
    if not pagerank:
        pagerank = graphutil.pagerank(grafo_canciones)

    strutil.imprimir_lista(pagerank[:n], SEP_CANCION_ARTISTA, ";")

    return pagerank

def recomendacion(usuario_cancion, n):
    '''
    documentacion
    '''
    pass

def ciclo(grafo_canciones, n, cancion):
    '''
    Recibe un grafo de canciones, una cancion y un largo n, e imprime un ciclo
    de largo n cuyo origen es la cancion con el formato:

    cancion_a - artista_a --> cancion_b - artista_b... 

    Si el ciclo no existe imprime el mensaje: 'No se encontro recorrido'.
    '''
    ciclo = graphutil.ciclo_largo_n(grafo_canciones, n, cancion)

    if ciclo is None: 
        print(mensajes.ENOENT_RECORRIDO)
        return 
    
    strutil.imprimir_lista(ciclo, SEP_CANCION_ARTISTA, " --> ", True)

def rango(n, cancion):
    '''
    documentacion
    '''
    pass

'''
-----------------------------------------------------------------
                  PROCESAMIENTO DE ENTRADA
-----------------------------------------------------------------
'''

def procesar_entrada(grafo_usuarios, grafo_canciones, pagerank):

    for linea in sys.stdin:
        linea = linea.rstrip("\n")
        cadenas = linea.split()
        comando = cadenas[0]

        if comando == CAMINO:
            origen, ultimo_indice = strutil.concatenar_cadenas(cadenas, 1, SEP_CANCIONES)
            destino, _ = strutil.concatenar_cadenas(cadenas, ultimo_indice + 1)

            origen_splitted = origen.split(SEP_CANCION_ARTISTA)
            destino_splitted = destino.split(SEP_CANCION_ARTISTA)

            artista_origen = None
            artista_destino = None

            if len(origen_splitted) == 2 and len(destino_splitted) == 2:
	            nombre_cancion_origen, artista_origen = origen_splitted
	            nombre_cancion_destino, artista_destino = destino_splitted

            camino(grafo_usuarios, (nombre_cancion_origen, artista_origen), (nombre_cancion_destino, artista_destino))
        
        elif comando == MAS_IMPORTANTES:
            pagerank = mas_importantes(grafo_canciones, int(cadenas[INDICE_N]), pagerank)
        
        elif comando == RECOMENDACION:
            pass

        elif comando == CICLO:
            cancion, _ = strutil.concatenar_cadenas(cadenas, 2)
            nombre_cancion, artista = cancion.split(SEP_CANCION_ARTISTA)

            ciclo(grafo_canciones, int(cadenas[INDICE_N]), (nombre_cancion, artista))
    
        elif comando == RANGO:
            cancion, _ = strutil.concatenar_cadenas(cadenas, 2)
            nombre_cancion, artista = cancion.split(SEP_CANCION_ARTISTA)

            rango(cadenas[INDICE_N], (nombre_cancion, artista))

        elif comando == CLUSTERING:
            if (len(cadenas)) == 1: 
                coeficiente = graphutil.clustering_grafo(grafo_canciones)
            else:
                cancion, _= strutil.concatenar_cadenas(cadenas, 1)
                nombre_cancion, artista = cancion.split(SEP_CANCION_ARTISTA)
                
                coeficiente = graphutil.clustering_vertice(grafo_canciones, (nombre_cancion, artista))
        
            print(strutil.redondear(coeficiente, 3))

        else: print(mensajes.ENOENT_COMANDO)

'''
-----------------------------------------------------------------
                     PROGRAMA PRINCIPAL
-----------------------------------------------------------------
'''

def main(ruta_archivo):

    start_time = datetime.now()
    grafo_canciones = graphutil.crear_grafo_canciones_provisorio(ruta_archivo, PLAYLIST_ID, TRACK_NAME, ARTIST)
    end_time = datetime.now()
    print(f"CREAR GRAFO CANCIONES: {end_time - start_time}")

    start_time = datetime.now()
    grafo_usuarios = graphutil.crear_grafo_con_archivo(ruta_archivo, USER_ID, PLAYLIST_NAME, TRACK_NAME, ARTIST)
    end_time = datetime.now()
    print(f"CREAR GRAFO USUARIOS: {end_time - start_time}")

    pagerank = []

    procesar_entrada(grafo_usuarios, grafo_canciones, pagerank)


main(sys.argv[1])