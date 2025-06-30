"""

Realice un programa en python, que permita generar un menú de gestión de entradas para el concierto de "noche de brujas"
El menú principal debe permitir mostrar cuatro opciones
"""
A="""

1| Comprar entrada
2| Consultar comprador
3| Cancelar compra
4| Salir del sistema
"""
"""
Las opciones del menú deben estar implementadas mediante funciones separadas del código principal

1- se debe permitir ingresar el nombre del comprador, tipo de entrada y código de confirmación (por separado)
Para que la compra sea exitosa se debe cumplir con lo siguiente:
    a) El nombre del comprador no debe repetirse.
    b) El tipo de entrada debe ser, General $10000 o VIP $50000
    c) El código de confirmación debe tener un mínimo de seis carácteres.
En el caso de cumplir con todas las condiciones, la entrada se registra como exitosa.

2- El menú debe permitir buscar compradores por nombre, si el comprador existe, debe mostrar datos asociados. (Nombre usuario, tipo de entrada con precio, y coódigo de confirmación.)
Si no existe el usuario el mensaje a mostrar sería : "Comprador no existe."

3- El menú debe permitir mostrar una opción que me permita eliminar un comprador con toda su información asociada.

4- Continuar comprando o salir del sistema

"""
compradores=[
    {"Nombre":"Ignacio", "Entrada":"VIP", "Code":"000001" }

]
EXIT = 0
def OPT1():
    print("Usted escogió opción 1")
    NC=0
    Entrada=0
    while NC!= 1:
        Nombre=input("Ingrese su nombre para comprar entradas: ")
        for name in compradores:

            if name["Nombre"]== Nombre:
                print("Este nombre ya ha sido registrado, ingrese otro nombre por favor.")
        else:
                NC = 1
                print("Escoja su tipo de entrada:" \
                "1| VIP = $50000" \
                "2| General = $10000")
                ticket=int(input("Escriba el número de su elección."))
                if ticket == 1:
                    Entrada="VIP"
                elif ticket == 2:
                    Entrada="General"
                else:
                    print("Error")
                    return
                Codigo=int(input("Ingrese ahora su codigo de confirmación, debe ser de 6 digitos mínimo: "))
                if Codigo < 100000:
                    print("Error, debía ser un codigo de mínimo 6 digitos.")
                    return
                else:
                    print(f"Se ha registrado su entrada exitosamente: Nombre {Nombre}, Entrada {Entrada}, Codigo {Codigo}")
                compradores.append(
                    {"Nombre": Nombre,"Entrada":Entrada,"Code":Codigo}
                )
                return

def OPT2():
    print("Usted escogió opción 2")
    Nombre=input("Ingrese el nombre que desee buscar")
    for name in compradores:
        if name["Nombre"]==Nombre:
            print(f"Se han encontrado datos para {Nombre}:")
            print(name)
    else:
            print("Comprador no existe.")
            return
def OPT3():
    print("Usted escogió opción 3")
    Nombre=input("Ingrese el nombre de la persona para cancelar la compra")
    for name in compradores:
        if name["Nombre"]==Nombre:
            print(f"Se han encontrado datos para {Nombre}:")
            print(name)
            print("¿Seguro que desea eliminar los datos asociados y cancelar la compra?")
            borrar=int(input("ingrese 1 para borrar o cualquier tecla para salir"))
            if borrar == 1:
                compradores.remove(name)
                print("Se ha eliminado la información y cancelado la compra.")
            else:
                print("Ha escogido salir.")
                return
    else:
            print("Comprador no Existe.")
            return
def OPT4():
    print("Usted escogió opción 4")
    print("Saliendo del sistema.")

    return
#########################################################################################################################################

while EXIT !=1:
    print("Bienvenido a la compra de entradas para noche de brujas")
    print(A)

    OPT=int(input("Ingrese el numero de la opción que desee: "))

    if OPT == 1:
        OPT1()
    elif OPT == 2:
        OPT2()
    elif OPT == 3:
        OPT3()
    elif OPT == 4:
        EXIT = 1
        OPT4()
    else:
        print("Error")