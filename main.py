import connect as cnt

def menu():
    print(" === | Bienvenido | === ")
    print("1. Conectar")
    print("2. Salir")

    opcion = int(input("Seleccione:"))
    
    match opcion:
        case 1:
            print("Conectando a servidor...")
            print(cnt.ssh_conexion())

        case 2:
            print("Saliendo.")

    return opcion

if __name__ == "__main__":
    menu()
    while True:
        seleccion = menu()
        if seleccion == 2:
            break
