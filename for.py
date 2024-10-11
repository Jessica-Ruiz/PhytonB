#Estructura de repeticion FOR
for i in range (2):#Comienza desde cero
    print(f"Su dato es: {i}")

#Estructura de repeticion FOR
for i in range (20,101):#Comienza desde el numero indicado y toma una posicion antes del final -1
    print(f"Su dato es: {i}")

#Estructura de repeticion FOR
for i in range (1,10,2):#Comienza inicio fin -1, incremento
    print(f"Su dato es: {i}")


#Estructura de repeticion FOR
for letra in "Python":
    print(letra)# organiza la letra ppor letra

#Ejemplo 1
cadena ="Python"
for letra in cadena:    
    if letra == "m":
        print("Se encontro la letra h")
        break
    else:
        print("Letra no encontrada")
print("Esta por fuera del ciclo for")

#ejemplo 2
cadena ="Programacion"
u=0
for letra in cadena:    
    if letra == "r":
        print("Se encontro la letra r")
        u+=1
        if u == 2:
                break
    else:
        print("Letra no encontrada")
print("Esta por fuera del ciclo for")

#Ejemplo tabla de multiplicar de la tabla del 2 
print("Tabla del 2")
for i in range (13):
    print (i*2)
#ejemplo
null = int(input("Digite la tabla de multiplicar que desea: "))
for i in range(1,13):
    print(f"2*{i}={i*2}")