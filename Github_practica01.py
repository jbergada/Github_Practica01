import math

PI = math.pi  

def area_circulo(radio):
    area = math.pow(radio, 2) * PI;
    return area

# volumen del circulo -> Nombre

# Volumen de un cubo -> Nombre

# La circunferencia -> Nombre

# Cambiar la entrada de datos para que puede usarlo desde consola
# input

radio = 3

# Programa principal
area = area_circulo(radio)



print("El area es: ", area)