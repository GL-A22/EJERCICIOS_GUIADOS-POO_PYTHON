# Clase Estudiante

class Estudiante_(object):
    #constructor
    def __init__(self, cedula_, nombre_, apellido_, edad_, calif1_, calif2_, calif3_):
        self.cedula =cedula_
        self.nombre =nombre_
        self.apellido =apellido_
        self.edad =edad_
        self.calif1 =calif1_
        self.calif2 =calif2_
        self.calif3 =calif3_
        self.calificacion = (calif1_ + calif2_ + calif3_) /3
        self.historial =[]

#funciones/Metodos
    #Prsentar datos
    def entregarInfo(self):
        print("No. Cedula {} - {} {} - Nota final {}".format(self.cedula, self.nombre, self.apellido, self.calificacion))

    #editar notas
    def editarCalificacion(self, calif1_, calif2_, calif3_):
        self.calif1 =calif1_
        self.calif2 =calif2_
        self.calif3 =calif3_
        self.calificacion  =(calif1_ +calif2_ + calif3_) /3
        print("¡Registro Exitoso!")

    #incluir evento de historial
    def incluirHistorial(self, calif1_, calif2_, calif3_, dataTime_):
        return ("modificacion: Calificacion_1: {:.2f} Calificacion_2: {:.2f} Calificacion_3: {:.2f} || Tiempo-Edicion: {}".format(calif1_, calif2_, calif3_, dataTime_ ))

    #Entregar Historial
    def etregarHistorial(self):
        print("No. Cedula: {} - {} {}".format(self.cedula, self.nombre, self.apellido))






