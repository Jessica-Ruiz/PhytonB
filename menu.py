opcion=(input("Digite la opcion del menu: "))
resultado=1+2

while opcion!="Salir":
    
    if opcion == "1":
        print(f"Bebidad\nJugo de mora\nAgua\nTe\nCafe")
    elif opcion=="2":
        print("Postres\nChocolate\nfresa\nCereza\nManzana")
    elif opcion=="3":
        print("Comidas rapidas\nHamburguesa\nSalchipapa\nSandwich")
    elif opcion=="4":
        print("Dulces\nBomBon bun\Galleta")
    else:
        print("opcion incorecta,ingrese valores del 1 al 4")
print("fuera de menu")
