#Importar libreria math
import math
#Area cuadrado
def area_cuadrado (lado):
    """
    Calcula el area del cuadrado
    a=l*l
    tipo de dato float
    """
    area = lado*lado
    return area
#Area triangulo
def area_tiangulo (base,Altura):
    """
    Calcula el area del triangulo
    (base ppor altura )/2
    """
    area = (base*Altura)/2
    return area
#Area circulo
def area_circulo (radio):
    """
    Calcula el area del circulo
    a=pi*r^2
    tipo de dato float
    """
    area =  math.pi*(radio*radio)
    return area