from clases.Estudiante import Estudiante_
from datetime import datetime

#clase principal

#lista
listaEstudiantes =[]

#Metodos
def registrar():
    print("Registrar estudiante\n")
    cedula = input("Ingrese el numero de cedula: ")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese su edad: "))
    nota_1 = float(input("Ingrese la primera calificacion: "))
    nota_2 = float(input("Ingrese la segunda calificacion: "))
    nota_3 = float(input("Ingrese la tercera calificacion: "))
    objectEstudiante = Estudiante_(cedula, nombre, apellido, edad, nota_1, nota_2, nota_3)
    listaEstudiantes.append(objectEstudiante)

def listarEstudiantes():
    print("Listado estudiantes\n")
    for objectEstudiante in listaEstudiantes:
        objectEstudiante.entregarInfo()

def buscarEstudiabte():
    print("Buscar estudiante\n")
    cedula = input("Ingresar la identificacion del estudiante a buscar: ")
    for objectEstudiante in listaEstudiantes:
        if cedula == objectEstudiante.cedula:
            objectEstudiante.entregarInfo()

def modificarNotas():
    print("Modificar notas\n")
    cedula = input("Ingresar la identificacion del estudiante: ")
    for objectEstudiante in listaEstudiantes:
        if cedula == objectEstudiante.cedula:
            nota_1 = float(input("Ingrese la primera calificacion: "))
            nota_2 = float(input("Ingrese la segunda calificacion: "))
            nota_3 = float(input("Ingrese la tercera calificacion: "))
            dataTime = datetime.now()
            objectEstudiante.editarCalificacion(nota_1, nota_2, nota_3)
            objectEstudiante.entregarInfo()
            recepcionHistorial = objectEstudiante.incluirHistorial(nota_1, nota_2, nota_3, dataTime)
            objectEstudiante.historial.append(recepcionHistorial)

def consultarHistorial():
    print("Consulta de historial\n")
    cedula = input("Ingrese la identificacion del estudiante: ")
    for objectEstudiante in listaEstudiantes:
        if cedula == objectEstudiante.cedula:
            for recepcionHistorial in objectEstudiante.historial:
                print("Evento historial de cambios: {}".format(recepcionHistorial))

def finalizar():
    print("Programa finalizado...\n")
    exit()

#funcion clase principal main()
def main():
    while True:
        print("\n")
        print("*|****************************|*")
        print(" *|******* Bienvenido ******|*")
        print(" *|*******    menu    ******|*")
        print("*|****************************|*")
        print("        ****************        ")
        print("Seleccione una de las siguientes funciones:")
        print("1.- Reggistrar estudiante")
        print("2.- Mostrar estudiante")
        print("3.- Buscar estudiante")
        print("4.- Modificar notas")
        print("5.- Consultar historial")
        print("6.- salir\n")

        opcion = int(input("Inserte el numero de la funcion: "))

        if opcion == 1:
            registrar()
        elif opcion == 2:
            listarEstudiantes()
        elif opcion == 3:
            buscarEstudiabte()
        elif opcion == 4:
            modificarNotas()
        elif opcion == 5:
            consultarHistorial()
        elif opcion == 6:
            finalizar()

#ejecucion
if __name__ == '__main__':
    main();