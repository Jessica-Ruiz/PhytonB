#Importar librerias meniu diferente
from Interfaz import menu,opcion_seleccionada,solicitud_cuadrado,solicitud_triangulo,solicitud_circulo,mostrar_cuadrado,mostrar_triangulo,mostrar_circulo

from Figuras import area_cuadrado,area_tiangulo,area_circulo
#Variable
opcion=  0
#Funcion principal
while opcion != 4:
    op = menu()
    formas_geometricas= opcion_seleccionada(op)
    #Condicionales
    if formas_geometricas == 1:
        lado = solicitud_cuadrado()
        area = area_cuadrado(lado)
        mostrar_cuadrado(area)
    elif formas_geometricas == 2:
        base,Altura=solicitud_triangulo()
        area = area_tiangulo(base,Altura)
        mostrar_triangulo(area)
    elif formas_geometricas == 3:
        radio = solicitud_circulo()
        area = area_circulo(radio)
        mostrar_circulo(area)
    elif formas_geometricas == 4:
        print("Saliendo de la calculadora")
        break
    else:
        print("Opcion no valida")

print("Gracias por utilizar la calculadora de figuras geometricas")