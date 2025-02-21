from abc import ABC, abstractmethod
import os

class Docente(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []

    @abstractmethod
    def asignar_materia(self, materia):
        pass

    @abstractmethod
    def __str__(self):
        pass

class DocentePlanta(Docente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.maximo_materias = 5

    def asignar_materia(self, materia):
        if len(self.materias) < self.maximo_materias:
            self.materias.append(materia)
        else:
            raise ValueError(f"No se puede asignar más materias al docente {self.nombre}")

    def __str__(self):
        return f"Docente de Planta: {self.nombre}, Materias: {', '.join(self.materias)}"

class DocenteCatedra(Docente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.maximo_materias = 3

    def asignar_materia(self, materia):
        if len(self.materias) < self.maximo_materias:
            self.materias.append(materia)
        else:
            raise ValueError(f"No se puede asignar más materias al docente {self.nombre}")

    def __str__(self):
        return f"Docente Catedra: {self.nombre}, Materias: {', '.join(self.materias)}"

class DocenteInvitado(Docente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.maximo_materias = 2

    def asignar_materia(self, materia):
        if len(self.materias) < self.maximo_materias:
            self.materias.append(materia)
        else:
            raise ValueError(f"No se puede asignar más materias al docente {self.nombre}")

    def __str__(self):
        return f"Docente Invitado: {self.nombre}, Materias: {', '.join(self.materias)}"
class Materia:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

    def __str__(self):
        return f"Materia {self.nombre}, {self.creditos} créditos"

class Estudiante:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.materias = []
    def __str__(self):
        return f"Estudiante: {self.nombre}, código: {self.codigo}"
    
class Calificaciones:
    def _init_(self, estudiante, materia, calificacion):
        self.estudiante = estudiante
        self.materia = materia
        self.calificacion = calificacion
        
    def _str_(self):
        return f"Estudiante: {self.estudiante.nombre}, {self.materia.nombre}, {self.calificacion}" 

class Aplicativo:
    def __init__(self):
        self.profesores = []
        self.estudiantes = []
        self.materias = []

    def docente_add(self, nombre, tipo):
        match tipo:
            case "planta":
                docente = DocentePlanta(nombre)
            case "catedra":
                docente = DocentePlanta(nombre)
            case "invitado":
                docente = DocentePlanta(nombre)
            case _:
                raise ValueError("Tipo no válido")
        self.profesores.append(docente)

    def docente_search(self, nombre):
        for docente in self.profesores:
            if docente.nombre == nombre:
                return docente

    def consultar_docente(self, nombre):
        docente = self.docente_search(nombre)
        if docente:
            print(docente)
            return
        print("Docente no encontrado")

    def eliminar_docente(self, nombre):
        docente = self.docente_search(nombre)
        if docente:
            self.profesores.remove(docente)
            print("Docente eliminado")
            return
        print("Docente no encontrado")

    def materia_search(self, nombre):
        for materia in self.materias:
            if materia.nombre == nombre:
                return materia

    def materia_add(self, nombre, creditos):
        materia = Materia(nombre, creditos)
        self.materias.append(materia)

    def consultar_materia(self, nombre):
        materia_encontrada = self.materia_search(nombre)
        if materia_encontrada:
            print(materia_encontrada)
            return
        print("Materia no encontrada")

    def eliminar_materia(self, nombre):
        materia_encontrada = self.materia_search(nombre)
        if materia_encontrada:
            self.materias.remove(materia_encontrada)
            print("Materia eliminada")
            return
        print("Materia no encontrada")
    def modificar_materia(self, nombre, nuevo_nombre, nuevos_creditos):
        materia_encontrada = self.materia_search(nombre)
        if materia_encontrada:
            materia_encontrada.nombre = nuevo_nombre
            materia_encontrada.creditos = nuevos_creditos
            print("Materia modificada")
            return
        print("Materia no encontrada")

    def estudiante_add(self, nombre, codigo):
        nuevo_estudiante = Estudiante(nombre, codigo)
        self.estudiantes.append(nuevo_estudiante)

    def estudiante_search(self, codigo):
       for estudiante in self.estudiantes:
            if estudiante.codigo == codigo:
                return estudiante

    def consultar_estudiante(self, codigo):
        estudiante_encontrado = self.estudiante_search(codigo)
        if estudiante_encontrado:
            print(estudiante_encontrado)
            return
        print("Estudiante no encontrado")

    def eliminar_estudiante(self, codigo):
        estudiante_encontrado = self.estudiante_search(codigo)
        if estudiante_encontrado:
            self.estudiantes.remove(estudiante_encontrado)
            print("Estudiante eliminado")
            return
        print("Estudiante no encontrado")

    def mod_estudiante(self, codigo, nuevo_codigo, nuevo_nombre):
        estudiante_encontrado = self.estudiante_search(codigo)
        if estudiante_encontrado:
            estudiante_encontrado.codigo = nuevo_codigo
            estudiante_encontrado.nombre = nuevo_nombre
            print("Estudiante modificado")
            return
        print("Estudiante no encontrado")

    def adicionar_materia_profesor(self, materia, profesor):
        materia_encontrada = self.materia_search(materia)
        profesor_encontrado = self.docente_search(profesor)
        if materia_encontrada and profesor_encontrado:
            profesor_encontrado.asignar_materia(materia_encontrada)
            print("Materia asignada")
            return
        print("Materia o profesor no encontrado")

    def eliminar_materia_profesor(self, materia, profesor):
        materia_encontrada = self.materia_search(materia)
        profesor_encontrado = self.docente_search(profesor)
        if materia_encontrada and profesor_encontrado:
            profesor_encontrado.materias.remove(materia_encontrada)
            print("Materia eliminada")
            return
        print("Materia o profesor no encontrado")

    def reportes_materia_profesor(self, profesor):
        profesor_encontrado = self.docente_search(profesor)
        if profesor_encontrado:
            if len(profesor_encontrado.materias) > 0:
                for materia in profesor_encontrado.materias:
                    print(materia)
                return
        print("Profesor no encontrado")
        
    def adicionar_materia_estudiante(self, materia, estudiante):
        materia_encontrada = self.materia_search(materia)
        estudiante_encontrado = self.estudiante_search(estudiante)
        if materia_encontrada and estudiante_encontrado:
            estudiante_encontrado.materias.append(materia_encontrada)
            print("Materia agregada al estudiante")
            return
        print("Estudiante no encontrado")

    def eliminar_materia_estudiante(self, materia, estudiante):
        materia_encontrada = self.materia_search(materia)
        estudiante_encontrado = self.estudiante_search(estudiante)
        if materia_encontrada and estudiante_encontrado:
            estudiante_encontrado.materias.remove(materia_encontrada)
            print("Materia eliminada al estudiante")
            return
        print("Estudiante no encontrado")

    def reporte_materias_estudiante(self, estudiante):
        estudiante_encontrado = self.estudiante_search(estudiante)
        if estudiante_encontrado:
            if len(estudiante_encontrado.materias) > 0:
                for materia in estudiante_encontrado.materias:
                    print(materia)
                return
        print("Estudiante no encontrado")
    
    def encontrar_calificacion(self, estudiante, materia):
        for calificacion in self.calificaciones:
            if calificacion.estudiante == estudiante and calificacion.materia == materia:
                return calificacion

    def adicionar_calificaciones(self, estudiante, materia, calificacion):
        estudiante_encontrado = self.estudiante_search(estudiante)
        materia_encontrada = self.materia_search(materia)
        if estudiante_encontrado and materia_encontrada and materia_encontrada in estudiante_encontrado.materias:
            nueva_calificacion = Calificaciones(estudiante_encontrado, materia_encontrada, calificacion)
            self.calificaciones.append(nueva_calificacion)
            print("Calificación agregada")
            return
        print("Estudiante o materia no encontrado")

    def modificar_calificaciones(self, estudiante, materia, nueva_calificacion):
        estudiante_encontrado = self.estudiante_search(estudiante)
        materia_encontrada = self.materia_search(materia)
        if estudiante_encontrado and materia_encontrada:
            calificacion_encontrada = self.encontrar_calificacion(estudiante_encontrado, materia_encontrada)
            if calificacion_encontrada:
                calificacion_encontrada.calificacion = nueva_calificacion
                print("Calificación modificada")
                return
            print("La calificación no existe")
            return
        print("Estudiante o materia no encontrado")

    def eliminar_calificaciones(self, estudiante, materia):
        estudiante_encontrado = self.estudiante.search(estudiante)
        materia_encontrada = self.materia_search(materia)
        if estudiante_encontrado and materia_encontrada:
            calificacion_encontrada = self.encontrar_calificacion(estudiante_encontrado, materia_encontrada)
            if calificacion_encontrada:
                self.calificaciones.remove(calificacion_encontrada)
                print("Calificación eliminada")
                return
            print("La calificación no existe")
            return
        print("Estudiante o materia no encontrado")
        


def menu_principal():
    aplicativo = Aplicativo()
    while True:
        print("\nMenú Principal")
        print("1. Manejo de docentes")
        print("2. Manejo de materias")
        print("3. Manejo de estudiantes")
        print("4. Manejo académico")
        print("5. Registro de calificaciones")
        print("6. Reportes")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_docentes(aplicativo)
        elif opcion == "2":
            menu_materias(aplicativo)
        elif opcion == "3":
            menu_estudiantes(aplicativo)
        elif opcion == "4":
            menu_academico(aplicativo)
        elif opcion == "5":
            menu_calificaciones(aplicativo)
        elif opcion == "6":
            menu_reportes(aplicativo)
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


def menu_docentes(aplicativo):
    while True:
        print("\nManejo de Docentes")
        print("1. Adicionar docente")
        print("2. Modificar docente")
        print("3. Eliminar docente")
        print("4. Consultar docente")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del docente: ")
            tipo = input("Tipo de docente (planta, catedra, invitado): ").lower()
            aplicativo.docente_add(nombre, tipo)
        elif opcion == "2":
            pass  
        elif opcion == "3":
            nombre = input("Nombre del docente a eliminar: ")
            aplicativo.eliminar_docente(nombre)
        elif opcion == "4":
            nombre = input("Nombre del docente a consultar: ")
            aplicativo.consultar_docente(nombre)
        elif opcion == "0":
            break
        else:
            print("Opción no válida, intente nuevamente.")


def menu_materias(aplicativo):
    while True:
        print("\nManejo de Materias")
        print("1. Adicionar materia")
        print("2. Modificar materia")
        print("3. Eliminar materia")
        print("4. Consultar materia")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la materia: ")
            creditos = int(input("Número de créditos: "))
            aplicativo.materia_add(nombre, creditos)
        elif opcion == "2":
            nombre = input("Nombre de la materia a modificar: ")
            nuevo_nombre = input("Nuevo nombre de la materia: ")
            nuevos_creditos = int(input("Nuevo número de créditos: "))
            aplicativo.modificar_materia(nombre, nuevo_nombre, nuevos_creditos)
        elif opcion == "3":
            nombre = input("Nombre de la materia a eliminar: ")
            aplicativo.eliminar_materia(nombre)
        elif opcion == "4":
            nombre = input("Nombre de la materia a consultar: ")
            aplicativo.consultar_materia(nombre)
        elif opcion == "0":
            break
        else:
            print("Opción no válida, intente nuevamente.")


def menu_estudiantes(aplicativo):
    while True:
        print("\nManejo de Estudiantes")
        print("1. Adicionar estudiante")
        print("2. Modificar estudiante")
        print("3. Eliminar estudiante")
        print("4. Consultar estudiante")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            codigo = input("Código del estudiante: ")
            aplicativo.estudiante_add(nombre, codigo)
        elif opcion == "2":
            codigo = input("Código del estudiante a modificar: ")
            nuevo_codigo = input("Nuevo código del estudiante: ")
            nuevo_nombre = input("Nuevo nombre del estudiante: ")
            aplicativo.mod_estudiante(codigo, nuevo_codigo, nuevo_nombre)
        elif opcion == "3":
            codigo = input("Código del estudiante a eliminar: ")
            aplicativo.eliminar_estudiante(codigo)
        elif opcion == "4":
            codigo = input("Código del estudiante a consultar: ")
            aplicativo.consultar_estudiante(codigo)
        elif opcion == "0":
            break
        else:
            print("Opción no válida, intente nuevamente.")


def menu_academico(aplicativo):
    while True:
        print("\nManejo Académico")
        print("1. Adicionar materias a profesor")
        print("2. Reportes materias profesor")
        print("3. Adicionar materias al estudiante")
        print("4. Reportes materias estudiante")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            profesor = input("Nombre del profesor: ")
            materia = input("Nombre de la materia: ")
            aplicativo.adicionar_materia_profesor(materia, profesor)
        elif opcion == "2":
            profesor = input("Nombre del profesor: ")
            aplicativo.reportes_materia_profesor(profesor)
        elif opcion == "3":
            estudiante = input("Código del estudiante: ")
            materia = input("Nombre de la materia: ")
            aplicativo.adicionar_materia_estudiante(materia, estudiante)
        elif opcion == "4":
            estudiante = input("Código del estudiante: ")
            aplicativo.reporte_materias_estudiante(estudiante)
        elif opcion == "0":
            break
        else:
            print("Opción no válida, intente nuevamente.")


def menu_calificaciones(aplicativo):
    while True:
        print("\nRegistro de Calificaciones")
        print("1. Adicionar calificaciones")
        print("2. Modificar calificaciones")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiante = input("Código del estudiante: ")
            materia = input("Nombre de la materia: ")
            calificacion = float(input("Calificación: "))
            aplicativo.adicionar_calificaciones(estudiante, materia, calificacion)
        elif opcion == "2":
            pass 
        elif opcion == "0":
            break
        else:
            print("Opción no válida, intente nuevamente.")


def menu_reportes(aplicativo):
    while True:
        print("\nReportes")
        print("1. Calificaciones por materia")
        print("2. Calificaciones por estudiante")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            materia = input("Nombre de la materia: ")
        elif opcion == "2":
            estudiante = input("Código del estudiante: ")
        elif opcion == "0":
            break
        else:
            print("Opción no válida, intente nuevamente.")



menu_principal()
