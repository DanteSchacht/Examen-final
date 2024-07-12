import Sueldos
import random
import json


trabajadores = []

def asignar_sueldo(Sueldos):
    trabajador = input("ingrese nombre del trabajador: ")
    sueldo = round(random.uniform(300000, 2500000))
    trabajadors = {
                    "Trabajador": trabajador,
                    "Sueldo": sueldo
                }
    trabajadores.append(Sueldos)
    print(f"A {trabajador} se le asigno un sueldo de {sueldo}")
    

    while True:
        agregar = input("Desea asignar otro sueldo? (s/n): ")
        if agregar.lower() == "s":
            trabajador = input("ingrese nombre del trabajador: ")
            sueldo = round(random.uniform(300000, 2500000))
            trabajadors = {
                    "Trabajador": trabajador,
                    "Sueldo": sueldo
                }
            trabajadores.append()
        else:
            break

def clasificar_sueldos(Sueldos):
    sueldo=sueldo    
    
    if sueldo() < 800000: 
        sueldosCalificar={"Nombre": trabajadores[0, 0]
                          }
