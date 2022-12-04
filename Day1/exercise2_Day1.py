currDirectory = 'Escritorio/AdventOfCode2021/Day1/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day1.txt'                       # Fichero de entrada
#input = 'example_Day1.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

cont = 0                # Contador del número de incrementos de la suma
val = []                # Valores a considerar en la suma

val.append(int(f.readline()))    # Leemos las tres primera filas
val.append(int(f.readline()))
val.append(int(f.readline()))

try:
    for linea in f:
        if linea != '\n':
            ant = val
            val = val[1:]
            val.append(int(linea))
            if sum(ant) < sum(val):
                cont += 1
finally:
    f.close()

print('El incremento de las sumas es: ' + str(cont))
            