class Alumno():
    nombre = ""
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

        def calificacion():
            if(self.nota >= 6): print("Aprobado")
            else: print("No aprobado")

            alumno1 = Alumno("Thor", 5)
            print(alumno1.nombre, " de acuerdo a tu nota ",alumno1.nota,", estas ", alumno1.calificacion())