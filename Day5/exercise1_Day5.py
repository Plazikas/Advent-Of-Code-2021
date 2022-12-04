# Creamos el tablero
dimension = 1000
dashboard = []
for i in range(0, dimension):
    row = []
    for j in range (0,dimension):
        row.append(0)
    dashboard.append(row)

# Función que muestra el estado del tablero
def ShowDashboard(dashboard):
    for row in dashboard:
        print(row)
    print()

# Función que actualiza el tablero tras indicar indicar las coordenadas de inixio y fin de una línea
def UpdateCoverPoints(coord1, coord2):
    x1 = int(coord1[0])
    y1 = int(coord1[1])
    x2 = int(coord2[0])
    y2 = int(coord2[1])

    if x1 == x2:
        for i in range (min(y1,y2), max(y1,y2) + 1):
            globals()['dashboard'][i][x1] += 1
    elif y1 == y2:
        for i in range (min(x1,x2), max(x1,x2) + 1):
            globals()['dashboard'][y1][i] += 1

def CountOverlaps(dashboard):
    suma = 0
    for row in dashboard:
        for n in row:
            if n > 1:
                suma += 1
    return suma

currDirectory = 'Escritorio/AdventOfCode2021/Day5/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day5.txt'                       # Fichero de entrada
#input = 'example_Day5.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

try:
    for linea in f:
        if linea != '\n':
            coordinates = linea[:-1].split(' -> ')
            coordinate1 = coordinates[0].split(',')
            coordinate2 = coordinates[1].split(',')
            UpdateCoverPoints(coordinate1, coordinate2)
finally:
    f.close()

print('El resultado es: ' + str (CountOverlaps(dashboard)))