#Crear una lista
lista=[90,"a","Viernes","False","4.5"]
print(f"Los datos de la lista son: {lista}")

#Datos de una lista

print (lista [2])
print (lista [4])
print (lista [-4])
print (lista [-3])

#Recorrer una lista

print(lista[1:4])
print(lista[0:3])
print(lista[:])
print(lista[2:])
print(lista[-1:])

#Agregar datos a una lista
numeros=[1,5]
numeros.append(100)
numeros.append("jessicaruiz223@unisangil.edu.co")
print(numeros)

#Tamaño lista
longitud = numeros.__len__()
print(f"El tamaño de la lista es  {longitud}")

#Insert
numeros.insert(2,"Jineth")
print(numeros)
numeros.insert(1,"J")
print(numeros)
numeros.insert(5,"1057892288")
print(numeros)
numeros.insert(4,"Ruiz")
print(numeros)
numeros.insert(6,"Rincpn")
print(numeros)
numeros.insert(3,"3.14")
print(numeros)
numeros.insert(0,"Programacion")
print(numeros)

#falta poner la extencion de la lista
val = lista.__len__()
print(f"La cantidad de elementos de la lista es de: {val}")
#Reemplazar datos de una lista
numeros[-1]="ruizrinconjessicajineth@gmail.com"
print(numeros)

numeros[2]="Dinalut"
print(numeros)

numeros[4]="Astronomia"
print(numeros)
#Eliminar datos
# remover el dato exactamente escrito
numeros.remove(100)
print(numeros)
#Elimina el ultimo elemento de la lista
numeros.pop()
print(numeros)

#elminar datos de manera identada(variso a la vez)
numeros[2:4]=[]
print(numeros)

#Sacar dato  de manera individual
#Recorrer lista
for i in lista:
    print(f"Datos lista: {i}")
lista.reverse()
print(lista)

#Ordenar datos de una lista de 
# forma ascendente
lista_2=[10,2,4,5,7,8,3]
print(sorted(lista_2))
#Muestra un vacio
print(lista_2.sort())

#Ordenar descendente
lista_2.sort(reverse=True)
print(lista_2)

#Sumar datos de la lista y dar pormedio
sumar=sum(lista_2)
prpmedio=sumar/len(lista_2)
print(f"La suma de los valores de la lista es de {sumar}")
print(f"El promedio al sumar los valores de la lista es de {prpmedio}")