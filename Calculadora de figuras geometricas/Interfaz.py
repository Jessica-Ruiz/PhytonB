#Funcion menu proncipal
def menu ():
    """
    Muestra el menu de las figuras geometricas
    """
    print("\n Bienvenido a la calculadora de figuras geometricas")
    print("1.Cuadrado")
    print("2.Triangulo")
    print("3.Circulo")
    print("4.Salir")
    op= int(input("Digite una opcion del menu: "))
    return op

#Mostrar informacion seleccionada

def opcion_seleccionada(op):
    """
    Mostrar lo seleccionado del menu en letras
    """
    Cuadrado = 1
    Triangulo = 2
    Circulo = 3
    Salir = 4
    #Condicianales
    if op == 1:
        print(f"Usted selecciono la opcion Cuadrado")
        return
    elif op == 2:
        print(f"Usted selecciono la opcion Triangulo")
        return
    elif op == 3:
        print(f"Usted selecciono la opcion Circulo")
        return
    elif op == 4:
        print(f"Usted selecciono la opcion Salir")
        return
    else:
        print(f"Opcion no valida!!!")
        return
    
#Solicitud de informacion
#Cuadrado
def solicitud_cuadrado () :
    """
    Solicita la medida del lado para calculo de area lado
    tipo de dato float
    """
    lado=float(input("Digite el lado: "))
    return lado
#Triangulo
def solicitud_triangulo () :
    """
    Solicita base y altura para calculo de area 
    tipo de dato float, retorna primero la base 
    y despues la altura
    """
    base = float(input("Digite el base: "))
    Altura = float(input("Digite el altura: "))
    return base,Altura
#Circulo
def solicitud_circulo () :
    """
    Solicita la medida del radio para calculo de area lado,
    tipo de dato float
    """
    radio = float(input("Digite el radio: "))
    return radio

#Mostar informacion areas
#Mostrar area de un cuadrado
def mostrar_cuadrado(area):
    """
    Muestra el area del cuadrado
    tipo float
    """
    print(f"El area del cuadrado es: {area}")

#Mostrar area de un triangulo
def mostrar_triangulo(area):
    """
    Muestra el area del triangulo
    tipo float
    """
    print(f"El area del triangulo es: {area}")
#Mostrar area de un circulo
def mostrar_circulo(area):
    """
    Muestra el area del circulo
    tipo float
    """
    print(f"El area del circulo es: {area}")



