def menu ():
    print("Conversión de números: ")
    print("1. Decimal a Binario, Octal y Hexadecimal")
    print("2. Binario a Decimal")
    print("3. Octal a Decimal")
    print("4. Hexadecimal a Decimal") 
    print("5. Salir")


while True:
    menu()
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        numero = input("Ingrese un número decimal: ")
        if numero.isdigit():
            decimal = int(numero)
            print(f"Número decimal: {decimal}")
            print(f"Binario: {bin(decimal)[2:]}")
            print(f"Octal: {oct(decimal)[2:]}")
            print(f"Hexadecimal: {hex(decimal)[2:].upper()}")
        else:
            print("Error: Debe ingresar un número decimal válido.")

    elif opcion == "2":
        binario = input("Ingrese un número binario: ")
        try:
            decimal = int(binario, 2)
            print(f"Binario {binario} en decimal es: {decimal}")
        except ValueError:
            print("Error: Ingrese solo dígitos binarios (0 o 1).")

    elif opcion == "3":
        octal = input("Ingrese un número octal: ")
        try:
            decimal = int(octal, 8)
            print(f"Octal {octal} en decimal es: {decimal}")
        except ValueError:
            print("Error: Ingrese solo dígitos octales (0 a 7).")

    elif opcion == "4":
        hexa = input("Ingrese un número hexadecimal (0-9, A-F): ")
        try:
            decimal = int(hexa, 16)
            print(f"Hexadecimal {hexa} en decimal es: {decimal}")
        except ValueError:
            print("Error: Ingrese un valor hexadecimal válido.")

    elif opcion == "5":
        print("👋 ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Elija entre 1 y 5.")