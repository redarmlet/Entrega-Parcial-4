"""EJERCICIO 1: 
La fundación duoc UC solicita servicios profesionales para desarrollar un sistema que le permita almacenar
los datos personales de cada uno de sus estudiantes,
nombre apellido rut correo elec. 
Carrera dentro de la carrera se inserta la sg lista, gastronomía, ingeniería y gastronomía, analista
Ingenieria: desarrollo web, Móvil y desarrollo escritorio
Analista: análisis dashboard limpieza dashboard, creación de dashboard
Gastronomia: historia gastronomía sopaipilla alimento natural y procesado
"""
carreras = {
    "Ingenieria": ["Desarrollo web", "Móvil", "Desarrollo escritorio"],
    "Analista": ["Análisis dashboard", "Limpieza dashboard", "Creación de dashboard"],
    "Gastronomia": ["Historia gastronomía", "Sopaipilla", "Alimento natural y procesado"]
}

def agregar_estudiante():
    while True:
        rut = input("Ingrese RUT: ")
        if rut not in estudiantes:
            break
        else:
            print("RUT ya registrado. Intente otro.")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    print("Carreras disponibles:")
    for c in carreras:
        print("-", c)
    while True:
        carrera = input("Ingrese carrera: ")
        if carrera in carreras:
            break
        else:
            print("Carrera inválida. Intente de nuevo.")
    print("Subcarreras disponibles:")
    for sc in carreras[carrera]:
        print("-", sc)
    while True:
        subcarrera = input("Ingrese subcarrera: ")



EJERCICIO 2:
Realiza un programa en python que permita crear un menu de gestión de entradas para el concierto de noche de brujas. 

El menu principal debe permitir mostrar 4 opciones. 

Menu principal:
Opción:
1.-Comprar entrada
2.-Consultar comprador 
3.-Cancelar compra 
4.-Continuar o salir 

Todas las opciones del menú deben estar implementadas mediante funciones(Def), separadas del código principal (Main). 

Descripción de las opciones

1.-Se debe permitir ingresar el nombre del comprador, tipo de entrada y codigo de confirmación por separados. Para que la compra sea exitosa se debe cumplir con lo siguiente:
a)El nombre del comprador no debe repetirse
b)el tipo de entrada debe ser general($10.000) o VIP($50.000)
c)el codigo de confirmación debe tener un mínimo de 6 caracteres y un número (1,2,etc) como mínimo y 0 espacios.

En el caso de cumplir con todas las condiciones. La entrada de registra como exitosa. 

2.-El menu me debe permitir buscar compradores mediante el nombre. Mensaje a mostrar, si el comprador existe debería mostrar estos asociados: 

-Nombre usuario
-Tipo de entrada 
-Codigo confirmación

Si no existe el usuario mostrar mensaje: comprador no existe

3.-Eliminar la información del comprador o usuario. 

4.-Consultarle al usuario si desea continuar o salir


def tiene_numero(texto):
    for c in texto:
        if c in "0123456789":
            return True
    return False

def comprar_entrada():
    while True:
        nombre = input("Nombre comprador: ")
        if nombre not in entradas:
            break
        else:
            print("Nombre ya registrado. Intente otro.")
    while True:
        tipo = input("Tipo entrada (general/vip): ")
        if tipo == "general" or tipo == "vip":
            break
        else:
            print("Debe ingresar general o vip.")
    while True:
        codigo = input("Código confirmación: ")
        if len(codigo) >= 6 and " " not in codigo and tiene_numero(codigo):
            break
        else:
            print("Código no válido, debe tener mínimo 6 caracteres, un número y sin espacios.")
    entradas[nombre] = {"tipo": tipo, "codigo": codigo}
    print("Compra registrada exitosamente.")

def consultar_comprador(nombre):
    if nombre in entradas:
        print("Nombre:", nombre)
        print("Tipo entrada:", entradas[nombre]["tipo"])
        print("Código confirmación:", entradas[nombre]["codigo"])
    else:
        print("Comprador no existe.")

def cancelar_compra(nombre):
    if nombre in entradas:
        del entradas[nombre]
        print("Compra cancelada.")
    else:
        print("Comprador no encontrado.")

def salir():
    if input("¿Desea continuar? (si/no): ") != "si":
        print("Saliendo...")
        exit()

entradas = {}

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1.- Comprar entrada")
    print("2.- Consultar comprador")
    print("3.- Cancelar compra")
    print("4.- Salir")
    opcion = input("Ingrese opción: ")

    if opcion == "1":
        comprar_entrada()
    elif opcion == "2":
        nom = input("Ingrese nombre comprador a buscar: ")
        consultar_comprador(nom)
    elif opcion == "3":
        nom = input("Ingrese nombre comprador a eliminar: ")
        cancelar_compra(nom)
    elif opcion == "4":
        salir()
    else:
        print("Opción inválida, intente de nuevo.")
