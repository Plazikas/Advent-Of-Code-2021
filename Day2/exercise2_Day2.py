coordinate_x = 0
coordinate_y = 0
aim = 0

# Función que actualiza el valor en las coordenadas del eje X o Y
def UpdatePosition(way, n):
    if way == 'forward':
        globals()['coordinate_x'] += n
        globals()['coordinate_y'] += globals()['aim'] * n
    elif way == 'up':
        globals()['aim'] -= n
    elif way == 'down':
        globals()['aim'] += n       
    print('Coordenadas X: ' + str(globals()['coordinate_x']) + '\n' + 'Coordenadas Y: ' + str(globals()['coordinate_y']))

currDirectory = 'Escritorio/AdventOfCode2021/Day2/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day2.txt'                       # Fichero de entrada
# input = 'example_Day2.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

try:
    for linea in f:
        if linea != '\n':
            movement = linea.split()
            UpdatePosition(movement[0], int(movement[1]))
finally:
    f.close()

print('La multiplicación de los ejes X e Y es: ' + str(coordinate_x * coordinate_y))