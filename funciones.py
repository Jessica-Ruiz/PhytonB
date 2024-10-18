#Funciones
def mensaje():
    """
mostrar mensaje programacion 1:  str
"""
    print("Programacion 1")
    x=10
#Llamar funcion
mensaje()

#Crear Funcion con parametros
def suma (num1,num2):
    """
    Genera la suma de dos numeros enteros 
    con variables de entrada num1, num2
    """
    rta = num1 + num2 
    print(f"La suma entre {num1} + {num2} = {rta} ")

#Llamar funcion
suma(1,2)

#Funcion pedrir datos
def solicitar_datos():
    """
    Solicita num1 y num2, transforma a tipo de dato 
    entero y retorna la informacion
    """
    num1 = int(input("Digite el numero 1: "))
    num2 = int(input("Digite el numero 2: "))
    return num1,num2 

#Llamar funcion
a,b = solicitar_datos()
print(f"Numeros digitados {a} y {b}")
#llamar a suma
suma(a,b)

#Funcion con parametros y valores de retorno
def multiplicacion (num1,num2):
    """
    2 numeros de tipo entero y los retorna 
    """
    rta = num1 * num2
    return rta
rta=multiplicacion(a,b)
print(f"El resultado de la multiplicacion ={rta}")

suma =(rta,a)

