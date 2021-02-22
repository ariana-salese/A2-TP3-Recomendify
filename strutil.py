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

def imprimir_lista(lista, separador):
    '''
    Recibe una lista con el formato [(param_1a, param_2a), (param_1b, param_2b)] e imprime:
    param_1a(separador)param_2a --> param_1b(separador)param_2b...
    '''
    for elemento in lista:
        param_1, param_2 = elemento
        print(f"{param_1}{separador}{param_2} -->", end = ' ')

    print(f"{lista[0][0]}{separador}{lista[0][1]}")

