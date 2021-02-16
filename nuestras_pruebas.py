import csv

ID = 'ID'
USER_ID = 'USER_ID'
TRACK_NAME = 'TRACK_NAME'	
ARTIST = 'ARTIST' 
PLAYLIST_ID	= 'PLAYLIST_ID'
PLAYLIST_NAME =	'PLAYLIST_NAME'
GENRES = 'GENRES'

def leer_archivo_tsv():

    with open("mini_prueba.tsv") as archivo:
        lector = csv.DictReader(archivo, delimiter = '\t')

        for linea in lector:
            print(f"El ID es {linea[ID]}")

            print(f"El nombre de la playlist es {linea[PLAYLIST_NAME]}")

            print(f"El genero es {linea[GENRES]}")

def main():
    leer_archivo_tsv()

main()