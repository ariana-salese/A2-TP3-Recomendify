import csv
import biblioteca
import sys
import mensajes

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


def main():
    #leer_archivo_tsv()
    #crear_grafo_usuarios()
    #procesar_entrada_1()
    #procesar_entrada_2() #clearly nicer 
    prueba_concatenar_cadenas()

main()