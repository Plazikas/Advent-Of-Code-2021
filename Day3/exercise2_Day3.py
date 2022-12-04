# Función que calcula el número de unos y ceros en cada posición de una lista de números binarios
def CountZerosAndOnes(list):
    cont_zeros = []
    cont_ones = []
    for c in list[0]:           # Inicializamos los contadores a cero
        cont_ones.append(0)
        cont_zeros.append(0)
    
    for val in list:         # Hacemos el recuento de unos y ceros en cada posición
        cont = 0
        for c in val:
            if c == '1':
                cont_ones[cont] += 1
            else:
                cont_zeros[cont] += 1
            cont += 1
    return [cont_zeros, cont_ones]

# Función que convierte un número binario a decimal
def ConvertBinaryToDecimal(number):
    number = number[::-1]       # Invertimos el número
    val = 0
    for i in range(0,len(number)):    
        val += int(number[i]) * (2 ** i)
    return val

currDirectory = 'Escritorio/AdventOfCode2021/Day3/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day3.txt'                       # Fichero de entrada
# input = 'example_Day3.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

numbers = []
try:
    for linea in f:
        if linea != '\n':
            numbers.append(linea[:-1])
finally:
    f.close()

# Obtenermos "oxygen generator rating"
oxygen_numbers = numbers
pos = 0         # Posición que estamos considerando
while (len(oxygen_numbers) != 1):
    aux = []
    contadores = CountZerosAndOnes(oxygen_numbers)
    if contadores[0][pos] > contadores[1][pos]:
        for val in oxygen_numbers:
            if val[pos] == '0':
                aux.append(val)
    else:
        for val in oxygen_numbers:
            if val[pos] == '1':
                aux.append(val)
    oxygen_numbers = aux
    pos += 1

# Obtenermos "oxygen generator rating"
CO2_numbers = numbers
pos = 0
while (len(CO2_numbers) != 1):
    aux = []
    contadores = CountZerosAndOnes(CO2_numbers)
    if contadores[0][pos] <= contadores[1][pos]:
        for val in CO2_numbers:
            if val[pos] == '0':
                aux.append(val)
    else:
        for val in CO2_numbers:
            if val[pos] == '1':
                aux.append(val)
    CO2_numbers = aux
    pos += 1

print('El ratio de apoyo a la vida es: ' + str(ConvertBinaryToDecimal(oxygen_numbers[0]) *
        ConvertBinaryToDecimal(CO2_numbers[0])))