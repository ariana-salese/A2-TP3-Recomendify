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


def imprimir_lista_de_tuplas(lista, sep_int, sep_ext, repetir_primero = False):
    '''
    Recibe una lista con el formato [(param_1a, param_2a), (param_1b, param_2b)] e imprime:
    param_1a(sep_int)param_2a sep_ext param_1b(sep_int)param_2b...
    '''
    print(f"{lista[0][0]}{sep_int}{lista[0][1]}", end='')

    for i in range(1, len(lista)):
        print(f"{sep_ext}", end = '')
        param_1, param_2 = lista[i]
        print(f"{param_1}{sep_int}{param_2}", end = '')

    if repetir_primero:
        print(f"{sep_ext}{lista[0][0]}{sep_int}{lista[0][1]}")
    else:
        print("")

def imprimir_lista(lista, separador):
    '''
    Recibe una lista e imprime en una sola linea toda la lista separando cada elemento
    con el sepadador.
    '''

    for i, cadena in enumerate(lista):

        print(cadena, end = '')
        if i != len(lista) - 1: print(separador, end = '')
    
    print('')
    

def redondear(n, decimales):
    '''
    Recibe un numero n y la cantidad de decimales. Se devuelve una cadena 
    con n redondeado y con la cantidad de decimales dada.
    '''
    redondeado = str(round(n, decimales))

    if len(redondeado) == 1: 
        redondeado += "." + "0" * decimales
        return redondeado 

    cantidad_actual = len(redondeado.split('.')[1])

    if decimales != cantidad_actual: 
        redondeado += "0" * (decimales - cantidad_actual) 
    
    return redondeado
