datos_personales = []
boletas = []

cartelera = [
    ["spiderman across the spider-verse", 150, 2500],
]

filas_asientos = 10
columnas_asientos = 15
matriz_asientos = [["." for _ in range(columnas_asientos)] for _ in range(filas_asientos)]

def registrar_datos():
    nombre = input("ingrese su nombre: ")
    correo = input("ingrese su correo: ")
    duoc = input("eres estudiante duoc: ")
    if duoc == "si":
        print("usted tiene un descuento de 20%")
    datos_personales.append([nombre, correo, duoc])

def mostrar_cartelera():
    print("cartelera disponible")
    for i, pelicula in enumerate(cartelera):
        print(i + 1, "-", pelicula[0], "- asientos de la sala", pelicula[1] , "-", "precio:", pelicula[2])

def mostrar_matriz():
    print("mapa de asientos:")
    print("  ", end="")
    for i in range(1, columnas_asientos + 1):
        print(i, end=" ")
    print()
    for i in range(filas_asientos):
        print(chr(65 + i), end=" ")
        for j in range(columnas_asientos):
            print(matriz_asientos[i][j], end=" ")
        print()

def reservar_asientos():
    mostrar_cartelera()
    movie = int(input("seleccione una pelicula: ")) -1
    if movie < 0 or movie >= len(cartelera):
        print("seleccione una pelicula que este disponible")
        return
    asientos_disponibles = cartelera[movie][1]
    if asientos_disponibles == 0:
        print("no quedan asientos disponibles para esta pelicula")
        return
    
    mostrar_matriz()
    print("seleccione los asientos (ejemplo: A1)")
    asientos_reservar = input("seleccione los asientos que desea reservar: ").split(", ")


    asientos_seleccionados = []
    for asiento in asientos_reservar:
        fila, columna = obtener_coordenadas_asiento(asiento)
        if not validar_asiento(fila, columna):
            print("el asiento", asiento, "no es valido")
            return
        if matriz_asientos[fila][columna] == "X":
            print("el asiento", asiento, "ya esta ocupado")
            return
        matriz_asientos[fila][columna] = "X"
        asientos_seleccionados.append(asiento)

    cartelera[movie][2] -= len(asientos_seleccionados)
    nombre = datos_personales[-1][0]
    correo = datos_personales[-1][1]
    pelicula = cartelera[movie][0]
    boleta = [nombre, correo, pelicula, len(asientos_seleccionados), asientos_seleccionados]
    boletas.append(boleta)
    generar_boleta(nombre, correo, pelicula, len(asientos_seleccionados), asientos_seleccionados)
    print("ha reservado sus asientos con exito")

def obtener_coordenadas_asiento(asiento):
    fila = ord(asiento[0].upper()) - 65
    columna = int(asiento[1:]) - 1
    return fila, columna

def validar_asiento(fila, columna):
    return 0 <= fila < filas_asientos and 0 <= columna < columnas_asientos

def generar_boleta(nombre, correo, pelicula, asientos_reservados, asientos_seleccionados):
    print("-------boleta de reserva-------")
    print("nombre:", nombre)
    print("correo:", correo)
    print("pelicula:", pelicula)
    print("asientos reservados:", asientos_reservados)
    print("asientos seleccionados:", ", ".join(asientos_seleccionados))
    print("-------------------------------")

def mostrar_boletas():
    print("-------boletas generadas-------")
    for i, boleta in enumerate(boletas):
        nombre = boleta[0]
        correo = boleta[1]
        pelicula = boleta[2]
        asientos_reservados = boleta[3]
        asientos_seleccionados = boleta[4]
        generar_boleta(nombre, correo, pelicula, asientos_reservados, asientos_seleccionados)
    print("-------------------------------")

def menu():    
    
    while True:
        print("seleccione una opcion:")
        print("1. reservar asientos")
        print("2. mostrar boletas generadas")
        print("3. salir")
       

        opcion = input("seleccione una opcion: ")
        registrar_datos()
        if opcion == "1":
            reservar_asientos()   
        elif opcion == "2":
            mostrar_boletas()
        elif opcion == "3":
            print("hasta la proxima")
            break
        else:
            print("opcion invalida por favor seleccione una opcion valida")
menu()
