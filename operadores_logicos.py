#variables

num1=2
num2=5

#operadores logicos
#compuerta and

print(num1==num2 and num1<=num2)#1 1-v
print(num1==num2 and num1>num2)# 1 0-F
print(num1<num2 and num1>num2)#0 0-F
print(num1<num2 and num1>=num2)#0 1-F

#Ejemplo 1
#comprobacion de datos
usuario=input ("Digite el usuario: ")
contraseña=input("Digite la contraseña: ")
#AND
print(usuario=="Jessica" and contraseña== "asdf")

#or
#compuerta and

print(num1==num2 or num1<=num2)#0 1-v
print(num1<=num2 or num1>num2)# 1 0-v
print(num1>num2 or num1>num2)#0 0-F
print(num1>num2 or num1>=num2)#0 1-F

#not
print(not True)#f
print(not False)#V