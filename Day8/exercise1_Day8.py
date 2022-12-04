def AssignNumber(code):
    if len(code) == 2:
        return '1'
    elif len(code) == 3:
        return '7'
    elif len(code) == 4:
        return '4'
    elif len(code) == 7:
        return '8'
    elif len(code) == 5:
        if 'a' in code:
            return '2'
        elif 'e' in code:
            return '5'
        else:
            return '3'
    elif len(code) == 6:
        if 'f' not in code:
            return '0'
        elif 'g' not in code:
            return '9'
        else:
            return '6'

currDirectory = 'Escritorio/AdventOfCode2021/Day8/'     # Dirección donde se encuentra la fichero de entrada
#input = 'inputExercise_Day8.txt'                       # Fichero de entrada
input = 'example_Day8.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

suma = 0

try:
    for linea in f:
        code = ''
        if linea != '\n':
            linea = linea[:-1].split('|')
            secondPart = linea[1].split()
            for s in secondPart:
                code += AssignNumber(s)
            print(code)
            suma += int(code)
finally:
    f.close()

print('El resultado es: ' + str(suma))