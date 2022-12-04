# Función que convierte un número binario a decimal
def ConvertBinaryToDecimal(number):
    number = number[::-1]       # Invertimos el número
    val = 0
    for i in range(0,len(number)):    
        val += int(number[i]) * (2 ** i)
    return val

currDirectory = 'Escritorio/AdventOfCode2021/Day3/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day3.txt'                       # Fichero de entrada
#input = 'example_Day3.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

numbers = []
try:
    for linea in f:
        if linea != '\n':
            numbers.append(linea[:-1])
finally:
    f.close()

cont_ones = []
cont_zeros = []

for c in numbers[0]:        # Inicializamos los contadores a cero
    cont_ones.append(0)
    cont_zeros.append(0)

for val in numbers:         # Hacemos el recuento de unos y ceros en cada posición
    cont = 0
    for c in val:
        if c == '1':
            cont_ones[cont] += 1
        else:
            cont_zeros[cont] += 1
        cont += 1

gamma = ''
epsilon = ''

for i in range (0,len(cont_ones)):
    if cont_ones[i] > cont_zeros[i]:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print('El poder de consumición es: ' + str(ConvertBinaryToDecimal(epsilon) * ConvertBinaryToDecimal(gamma)))