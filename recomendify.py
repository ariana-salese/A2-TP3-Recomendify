import biblioteca
import sys

'''
Comento los que no se si vamos a usar, cuando nos organizamos borramos lo que 
sobra
'''
#ID = 'ID'
USER_ID = 'USER_ID'
TRACK_NAME = 'TRACK_NAME'	
ARTIST = 'ARTIST' 
PLAYLIST_ID	= 'PLAYLIST_ID'
PLAYLIST_NAME = 'PLAYLIST_NAME'
#GENRES = 'GENRES'

'''
-----------------------------------------------------------------
                     FUNCIONES AUXILIARES
-----------------------------------------------------------------
'''

#supongo que esto deberia ir generalizado en la biblioteca 

'''
-----------------------------------------------------------------
                          COMANDOS
-----------------------------------------------------------------
'''

def camino(origen, destino):
    '''
    documentacion
    '''

def mas_importantes(n):
    '''
    documentacion
    '''

def recomendacion(usuario_cancion, n):
    '''
    documentacion
    '''

def ciclo(n, cancion):
    '''
    documentacion
    '''

def rango(n, cancion):
    '''
    documentacion
    '''

def clustering(cancion):
    '''
    documentacion
    '''

'''
-----------------------------------------------------------------
                  PROCESAMIENTO DE ENTRADA
-----------------------------------------------------------------
'''



'''
-----------------------------------------------------------------
                     PROGRAMA PRINCIPAL
-----------------------------------------------------------------
'''

def main(ruta_archivo):

    #grafo_canciones = crear_grafo()

    grafo_usuarios = biblioteca.crear_grafo_con_archivo(ruta_archivo, USER_ID, PLAYLIST_NAME, TRACK_NAME, ARTIST)


main(sys.argv[1])