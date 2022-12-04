currDirectory = 'Escritorio/AdventOfCode2021/Day6/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day6.txt'                       # Fichero de entrada
#input = 'example_Day6.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

try:
    for linea in f:
        if linea != '\n':
            lanternship = linea[:-1].split(',')
        for i in range (0, len(lanternship)):
            lanternship[i] = int(lanternship[i])
finally:
    f.close()

days = 256
for day in range (0, days):
    cont = 0
    for i in range (0, len(lanternship)):
        lanternship[i] -= 1
    for i in range (0, len(lanternship)):
        if (lanternship[i] == -1):
            lanternship[i] = 6
            cont += 1
    for i in range (0, cont):
        lanternship.append(8)
    print(day)
print('El resultado es: ' + str(len(lanternship)))