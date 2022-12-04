def isEmpty(lista):
    return lista == []

# Función que indica si se ha conseguido Bingo en un cartón o no
def IsBingo(dashboard):
    for line in dashboard:
        if isEmpty(line):
            return True
    return False

# Función que devuelve un entero de cuando se consigue bingo, la suma de los número no tachados y el número con el que se consigue bingo
def InfoBingo(balls_numbers, dashboard):
    cont = 0
    for ball in balls_numbers:
        if not IsBingo(dashboard):
            linesCont = 0           # Contador para saber qué línea del cartón estamos
            for line in dashboard:
                if ball in line:
                    dashboard[linesCont].remove(ball)
                linesCont += 1
            cont += 1
        else:
            return (cont, dashboard, balls_numbers[cont - 1])
    
# Función que calcula la suma de números no tachados de un cartón
def ResultSum(infoDashboard):
    suma = 0
    for line in infoDashboard[1]:
        for n in line:
            suma += int(n)
    return suma
    

currDirectory = 'Escritorio/AdventOfCode2021/Day4/'     # Dirección donde se encuentra la fichero de entrada
input = 'inputExercise_Day4.txt'                       # Fichero de entrada
#input = 'example_Day4.txt'
#input = 'prueba.txt'

f = open(currDirectory + input)                         # Abrimos el fichero de entrada

balls_numbers = f.readline()[:-1].split(',')

dashboard = []
lastDashboard = (0, [], 0)
try:
    for linea in f:
        if linea != '\n':
            dashboard.append(linea.split())
        elif not isEmpty(dashboard):
            infoDashboard = InfoBingo(balls_numbers, dashboard)
            if infoDashboard[0] > lastDashboard[0]:
                lastDashboard = infoDashboard
                print('El resultado es: ' + str(ResultSum(lastDashboard) * int(lastDashboard[2])))
            dashboard.clear()
finally:
    f.close()
