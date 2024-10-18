#Declarar una matriz
matriz1=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
#Ubicacion de la matriz
matriz2=[[1,2,3],[4,5,6],[7,8,9]],

#Recorrer una matriz
#Recorre la fila 
for filas in matriz1:
#saca lo elemento de manera individual de la fila 
    for elementos in filas:
        print(f"Elementos matriz: {elementos},{filas}")

#matriz 
#matriz 4* 6

matriz3 = [
    [2,4,6,8,10,12],
    [14,16,18,20,24,26],
    [28,30,32,34,36,38],
    [40,42,44,46,48,50],
    
]
#Recorre la fila 
for filas in matriz3:
#saca lo elemento de manera individual de la fila 
    for elementos in filas:
        print(elementos)
        print(f"Elementos matriz: {elementos},{filas}")

#Matriz 4
matriz4 =[
    ["a","b","c","d","e","f"],
    [1057892288,1057892289,10275892290,1057892291,1057892292,1057892293],
    ["Jessica","Jineth","Erika","Dayana","Valerie","Deyanira"],
    ["True","False","True","False","True","False" ]
]

#Recorre la fila 
for filas in matriz4:
#saca lo elemento de manera individual de la fila 
    for elementos in filas:
        print(elementos)
        print(elementos)

#Tamaño matrz
print(f"Matrz 1")
f=len(matriz1)
print(f"Tamaño filas{f}")
c=len(matriz1[0])
print(f"Tamaño columnas{c}")
#martriz 3
print(f"Matrz 3")
f=len(matriz3)
print(f"Tamaño filas{f}")
c=len(matriz1[0])
print(f"Tamaño columnas{c}")
#Tamaño matriz 4
print(f"----Matriz 4")
f=len(matriz4)
print(f"Tamaño filas{f}")
c=len(matriz1[0])
print(f"Tamaño columnas{c}")


#Recorre matriz con range 
for i in range(f):
    for j in range(c):
#print (f"Posicion {i},{j}: {matriz1[0][0]}")
        print(matriz1[1][2])
        print(matriz1[2][1])

#Tablero de ajedres
ajedrez=[
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
]

for i in ajedrez:
        print(i)

print("Ingrese las datos  de la matriz")
num1=input("Ingese el numero de filas:")
num2=input("Ingrese el nummero de columnas:")
f=[0]
c=[1]
filas=0 or 1
columnas=0 or 1

for filas in f:
    filas=f*num1
    for columnas in c:
        columnas=c*num2
        print(filas,columnas)