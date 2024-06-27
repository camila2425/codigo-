def mostrar_escenario(escenario):
    print("\t\t\t=====ESCENARIO======\n")
    for i in range(0, 50, 10):
        fila = ""
        for j in range(10):
            fila += f"{escenario[i + j]}\t"
        print(fila)
    print("\n")

def comprar_entradas(escenario, precios, ventas, compradores):
    cantidad = int(input("Ingrese la cantidad de entradas que desea comprar (1 o 2): "))
    if cantidad < 1 or cantidad > 2:
        print("Cantidad inválida. Intente nuevamente.")
        return

    for _ in range(cantidad):
        mostrar_escenario(escenario)
        asiento = int(input("Seleccione el número del asiento que desea comprar: "))
        if escenario[asiento - 1] == 'X':
            print("El asiento no se encuentra disponible o ya está vendido.")
            return
        escenario[asiento - 1] = 'X'
        precio = precios[asiento]
        run = input("Ingrese el RUN de la persona que ocupará el asiento (sin guión ni puntos): ")
        ventas.append(precio)
        compradores.append(run)
        print(f"Se ha comprado el asiento {asiento} por ${precio} para el RUN {run}.\n")

def mostrar_ganancias_totales(ventas):
    total = sum(ventas)
    print(f"Las ganancias totales de las ventas de entradas de hoy son: ${total}\n")

def mostrar_compradores(compradores):
    if not compradores:
        print("No hay registros de compradores.\n")
    else:
        print("Listado de RUN de personas que compraron entradas:")
        for idx, run in enumerate(compradores, start=1):
            print(f"{idx}. {run}")
        print("\n")

# Mensaje de bienvenida
print("¡Bienvenido al sistema de venta de entradas para el concierto Tour Michael Jackson!")
print("Aquí puedes comprar entradas, ver ubicaciones disponibles, y más.\n")

# Diccionario de precios y lista de asientos
precios = {1: 100000, 2: 100000, 3: 100000, 4: 100000, 5: 100000,
           6: 100000, 7: 100000, 8: 100000, 9: 100000, 10: 100000,
           11: 100000, 12: 100000, 13: 100000, 14: 100000, 15: 100000,
           16: 100000, 17: 100000, 18: 100000, 19: 100000, 20: 100000,
           21: 50000, 22: 50000, 23: 50000, 24: 50000, 25: 50000,
           26: 50000, 27: 50000, 28: 50000, 29: 50000, 30: 50000,
           31: 10000, 32: 10000, 33: 10000, 34: 10000, 35: 10000,
           36: 10000, 37: 10000, 38: 10000, 39: 10000, 40: 10000,
           41: 10000, 42: 10000, 43: 10000, 44: 10000, 45: 10000,
           46: 10000, 47: 10000, 48: 10000, 49: 10000, 50: 10000}

# Mostrar valores segun el rango de precios de entradas y asientos 
print ("\t\t\tAsientos VIP 100000 desde (1 al 20)")
print ("\t\t\tAsientos normales 50000 desde (21 al 30)")
print ("\t\t\tAsientos economicos 10000 desde (31 al 50)")


escenario = [str(i) for i in range(1, 51)]
ventas = []
compradores = []

# Bucle principal para el menu 
while True:
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Mostrar ganancias totales de las ventas")
    print("4. Ver listado de asistentes")
    print("5. Salir")
    opcion = input("Seleccione una de las opciones mostradas en pantalla: ")

    if opcion == '1':
        comprar_entradas(escenario, precios, ventas, compradores)
    elif opcion == '2':
        mostrar_escenario(escenario)
    elif opcion == '3':
        mostrar_ganancias_totales(ventas)
    elif opcion == '4':
        mostrar_compradores(compradores)
    elif opcion == '5':
        print("¡Gracias por utilizar el sistema de ventas para este concierto! ¡Que tenga un buen día!")
        print ("\t\t\t===Sanchez Producciones===")
        break
    else:
        print("Opción inválida. Por favor, seleccione nuevamente.\n")