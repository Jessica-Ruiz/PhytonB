#Promocionar productos 
def frutas (mangos,sandia,manzanas,lulo,pera,fresa):
    """
    INDICAR AL USUARIO LOS PRODUCTOS PONE LOS PRESIOS DE LOS PRODUCTOS 
    """
opcion = 0
#Estructura repeticion
while opcion != 6:
    #Lista de productos que se venden
    print("\nBienvenido" )
    print("1. mango")
    print("2. sandia")
    print("3. lulo")
    print("4. pera")
    print("5. Fresa")
    print("6. Salir")
    #opcion a ingresar
    try:
        opcion = int(input("Seleccione el producto que desea comprar: "))
        if opcion == 1:
            print(f"1 kilo de mango cuesta $5000")
        elif opcion == 2:

            print(f"1 kilo de sandia cuesta $6000")
        elif opcion == 3:
            print(f"1 kilo de lulo cuesta $4000")
        elif opcion == 4:
            print(f"El kilo de pera cuesta $5500")    
        elif opcion == 5:
            print(f"El kilo de fresa cuesta $7000")
        elif opcion == 6:
            print(f"Ir a ejecutar la compra...")
        else:
            print("Error")
    except ValueError:
        print("Ingrese una opcion valida")      
def precios(cantidad,total):
    """
    sirve para que el usuario pueda seleccionar la cantidad de producto que ba a comprar con respecto a kilos
    """      
    frutas()





