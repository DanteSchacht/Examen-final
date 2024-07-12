from Sueldos import *
import Sueldos

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

while True:
    print("\nMenú: ")
    print("1.- Asignar sueldo.")
    print("2.- Clasificar sueldo.")
    print("3.- Clasificar sueldo.")
    print("4.- Clasificar sueldo.")
    print("5.- Clasificar sueldo.")
    opcion= input("selecione una opción: ")

    if opcion == "1":
        asignar_sueldo(Sueldos)
    elif opcion == "2":
        print()
    elif opcion == "3":
        print()
    elif opcion == "4":
        print()
    elif opcion == "5":
        print("Has salido del programa.")
    else:
        print("Opcion invalida.")