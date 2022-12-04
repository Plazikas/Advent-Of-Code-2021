currDirectory = 'Escritorio/AdventOfCode2021/Day1/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day1.txt'                      # Fichero de entrada
# input = 'example_Day1.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

cont = -1       # Contador del número de incrementos, inicializado a -1 para no contar el primero
val = 0         # Valor anterior

try:
    for linea in f:
        if linea != '\n':
            if val < int(linea):
                cont += 1
            val = int(linea)
finally:
    f.close()

print('El número de incrementos es: ' + str(cont))