def consultar_saldo(saldo):
    print("Su saldo actual es:", saldo, "pesos")
    return saldo

def depositar (saldo):
    cantidad = float(input("Ingrese la cantidad: "))
    while cantidad <= 0:
        print("Error. la cantidad a depositar debe ser mayor que cero")
        cantidad = float(input("Ingrese la cantidad a depositar: "))

    saldo = saldo + cantidad
    print("Deposito exitoso. su nuevo saldo es de: ", saldo, "pesos")
    return saldo

def retirar(saldo):
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    while cantidad <= 0 or cantidad > saldo:
        if cantidad <= 0:
            print("Error. la cantidad a retirar debe ser mayor que cero")
        else:
            print("Error. fondos insuficientes. no puede retirar mas de su saldo disponible")
        saldo = saldo - cantidad  
        print("Retiro exitoso. su nuevo saldo es de: ", saldo, "pesos")
        return saldo

saldo_actual = 1000
opcion = -1

while opcion != 0:
    print("\n--- CAJERO AUTOMATICO ---")
    print("1. consultar saldo")
    print("2. depositar dinero")
    print("3. retirar dinero")
    print("4. salir")

    opcion = int(input("Escoja una opccion: "))

    while opcion < 0 or opcion > 3:
        print("Error. opcion invalida")
        opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        saldo_actual = consultar_saldo(saldo_actual)
    elif opcion == 2:
        saldo_actual = depositar(saldo_actual)
    elif opcion == 3:
        saldo_actual = retirar(saldo_actual)
    elif opcion == 4:
        print("Gracias por utilizar el cajero automático.")    
