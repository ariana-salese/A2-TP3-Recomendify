import biblioteca
import sys
import mensajes

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
                     FUNCIONES AUXILIARES
-----------------------------------------------------------------
'''

#Hacemos una biblioteca aparte para el manejo de cadenas?
#Cambiamos el nombre la bibliteca de grafos a algo como grafos graphutilies or smth like that?

def concatenar_cadenas(cadenas, indice_inicio, cadena_fin = None):
    '''
    Recibe: una lista de cadenas, indice de inicio (indice_inicio) y una cadena final (cadena_fin).

    Devuelve una cadena resultante concatenando desde la cadena que se encuentra en el indice_inicio
    hasta la cadena_fin (no inclusive), ademas del indice en el que se encuentra la cadena_fin. Si
    cadena_fin es None se concatena hasta el final de la lista y se devuelve el indice de la ultima
    cadena existente. 
    '''
    cadena_resultante = ''

    for i in range(indice_inicio, len(cadenas)):
        cadena_actual = cadenas[i] 

        if cadena_actual == cadena_fin: return cadena_resultante[:-1], i

        cadena_resultante += cadena_actual + ' '

    return cadena_resultante[:-1], len(cadenas) - 1


'''
-----------------------------------------------------------------
                          COMANDOS
-----------------------------------------------------------------
'''

def camino(origen, destino):
    '''
    documentacion
    '''
    pass

def mas_importantes(n):
    '''
    documentacion
    '''
    pass

def recomendacion(usuario_cancion, n):
    '''
    documentacion
    '''
    pass

def ciclo(n, cancion):
    '''
    documentacion
    '''
    pass

def rango(n, cancion):
    '''
    documentacion
    '''
    pass

def clustering(cancion):
    '''
    documentacion
    '''
    pass


'''
-----------------------------------------------------------------
                  PROCESAMIENTO DE ENTRADA
-----------------------------------------------------------------
'''

#EJEMPLOS DE ENTRADAS

# -> CAMINO
#  camino Don't Go Away - Oasis >>>> Quitter - Eminem
# camino CANCION_1 - ARTISTA_1 >>>> CANCION_2 - ARTISTA_2

# -> MAS_IMPORTANTES
# mas_importantes 20

# -> RECOMENDACION
# recomendacion canciones 10 Love Story - Taylor Swift >>>> Toxic - Britney Spears >>>> I Wanna Be Yours - Arctic Monkeys >>>> Hips Don't Lie (feat. Wyclef Jean) - Shakira >>>> Death Of A Martian - Red Hot Chili Peppers

# -> CICLO DE N CANCIONES
# ciclo 7 By The Way - Red Hot Chili Peppers

# -> RANGO
#  rango 8 Shots - Imagine Dragons

# -> CLUSTERING
# clustering Teenage Dream - Katy Perry

def procesar_entrada():
    
    for linea in sys.stdin:
        linea = linea.rstrip("\n")
        cadenas = linea.split()
        comando = cadenas[0]

        if comando == CAMINO:
            origen, ultimo_indice = concatenar_cadenas(cadenas, 1, SEP_CANCIONES)
            destino, _ = concatenar_cadenas(cadenas, ultimo_indice + 1)

            nombre_cancion_origen, artista_origen = origen.split(SEP_CANCION_ARTISTA)
            nombre_cancion_destino, artista_destino = destino.split(SEP_CANCION_ARTISTA)

            camino((nombre_cancion_origen, artista_origen), (nombre_cancion_destino, artista_destino))
        
        elif comando == MAS_IMPORTANTES:
            mas_importantes(cadenas[INDICE_N])
        
        elif comando == RECOMENDACION:
            pass

        elif comando == CICLO:
            cancion, _ = concatenar_cadenas(cadenas, 2)
            nombre_cancion, artista = cancion.split(SEP_CANCION_ARTISTA)

            ciclo(cadenas[INDICE_N], (nombre_cancion, artista))
    
        elif comando == RANGO:
            cancion, _ = concatenar_cadenas(cadenas, 2)
            nombre_cancion, artista = cancion.split(SEP_CANCION_ARTISTA)

            rango(cadenas[INDICE_N], (nombre_cancion, artista))

        elif comando == CLUSTERING:
            cancion, _= concatenar_cadenas(cadenas, 1)
            nombre_cancion, artista = cancion.split(SEP_CANCION_ARTISTA)

            clustering((nombre_cancion, artista))
        
        else: print(mensajes.ENOENT_COMANDO)


'''
-----------------------------------------------------------------
                     PROGRAMA PRINCIPAL
-----------------------------------------------------------------
'''

def main(ruta_archivo):

    #grafo_canciones = crear_grafo()

    grafo_usuarios = biblioteca.crear_grafo_con_archivo(ruta_archivo, USER_ID, PLAYLIST_NAME, TRACK_NAME, ARTIST)

    procesar_entrada()

main(sys.argv[1])