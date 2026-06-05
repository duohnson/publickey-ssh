import connect as cnt

def menu():
    print(" === | Welcome | === ")
    print("1. Connect")
    print("2. Exit")

    opcion = int(input("Select:"))
    
    match opcion:
        case 1:
            print("Connecting to server...")
            print(cnt.ssh_connect())

        case 2:
            print("Exiting.")

    return opcion

if __name__ == "__main__":
    menu()
    while True:
        seleccion = menu()
        if seleccion == 2:
            break
