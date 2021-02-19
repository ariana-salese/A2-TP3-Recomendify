import csv
import biblioteca

ID = 'ID'
USER_ID = 'USER_ID'
TRACK_NAME = 'TRACK_NAME'	
ARTIST = 'ARTIST' 
PLAYLIST_ID	= 'PLAYLIST_ID'
PLAYLIST_NAME =	'PLAYLIST_NAME'
GENRES = 'GENRES'

'''
-----------------------------------------------------------------
                     FUNCIONES AUXILIARES
-----------------------------------------------------------------
'''

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

def main():
    #leer_archivo_tsv()
    crear_grafo_usuarios()

main()