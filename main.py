
def menu():
    print(" === | Bienvenido | === ")
    print("1. Opción 1")
    print("2. Salir")

    opcion = int(input("Seleccione:"))
    
    match opcion:
        case 1:
            print("Aún sin configurar")
            return menu()
        case 2:
            print("Saliendo.")
            while True:
                if opcion == 2:
                    break

    return opcion


if __name__ == "__main__":
    menu()