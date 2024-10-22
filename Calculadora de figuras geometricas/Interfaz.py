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
    print(f"Usted selecciono la opcion {op}")