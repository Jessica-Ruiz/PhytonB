import math

# Variable
opcion = 0

while opcion != 7:
    # Menú calculadora
    print("\nHola calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Raíz")
    print("7. Salir")

    # Opción a ingresar
    try:
        opcion = int(input("Digite la opción de la calculadora: "))
        if opcion == 1:
            num1 = int(input("Digite el primer número: "))
            num2 = int(input("Digite el segundo número: "))
            resultado = num1 + num2
            print(f"Suma = {resultado}")
        elif opcion == 2:
            num1 = int(input("Digite el primer número: "))
            num2 = int(input("Digite el segundo número: "))
            resultado = num1 - num2
            print(f"Resta = {resultado}")
        elif opcion == 3:
            num1 = int(input("Digite el primer número: "))
            num2 = int(input("Digite el segundo número: "))
            resultado = num1 * num2
            print(f"Multiplicación = {resultado}")
        elif opcion == 4:
            num1 = int(input("Digite el primer número: "))
            num2 = int(input("Digite el segundo número: "))
            resultado = num1 / num2
            print(f"División = {resultado}")
        elif opcion == 5:
            base = int(input("Digite el primer número: "))
            potencia = int(input("Digite el segundo número: "))
            if potencia == 0:
                resultado=1
            else:
                resultado = base ** potencia
            print(f"Potencia = {resultado}")
        elif opcion == 6:
            num = float(input("Digite el número para calcular la raíz: "))
            if num < 0:
                print("No se puede calcular la raíz de un número negativo.")
            else:
                resultado = math.sqrt(num)
                print(f"Raíz cuadrada = {resultado}")
        elif opcion == 7:
            print("Saliendo de la calculadora")
        else:
            print("Error: Opción no válida")
    except ValueError:
        print("Ingrese una opción válida")

print("Gracias por utilizar la calculadora")


