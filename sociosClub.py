
class Club:
    def __init__(self):
        self.socios = []
        self.facturas = []
    
    def adicionarSocio(self):
        nombre = str(input("Ingrese el nombre del socio: "))
        cedula = str(input("Ingrese la cedula del socio: "))
        tipo = str(input("Ingrese el tipo de socio (Platinum, Gold, Silver): ")).strip().lower()

        if tipo == "silver":
            socio = Silver(nombre, cedula)
        elif tipo == "gold":
            socio = Gold(nombre, cedula)
        elif tipo == "platinum":
            socio = Platinum(nombre, cedula)
        else:
            print("Tipo de socio no valido")
            return False
        self.socios.append(socio)
        print("El socio fue añadido exitosamente")
        return True

    def eliminarSocio(self, socio):
        if socio in self.socios:
            self.socios.remove(socio)
            return True
        return False

    def consultarSocioConAutorizados(self, cedula):
        for socio in self.lista_autorizados:
            if socio.cedula == cedula:
                print(f"El {socio.nombre} Si se encuentra autorizado")
                return True
        return False

    def adicionarAutorizado(self, socio):
        if socio in self.socios:
            if len(socio.lista_autorizados) < socio.limiteAutorizados:
                nombreAutorizado = str(input("Ingrese el nombre del autorizado: "))
                cedulaAutorizado = str(input("Ingrese la cedula del autorizado: "))
                nuevoAutorizado = Autorizado(cedulaAutorizado, nombreAutorizado)
                nuevoAutorizado.conSocio = True
                socio.lista_autorizados.append(nuevoAutorizado)
                return True
        return False
    
    def eliminarAutorizado(self, socio, autorizado):
        if socio in self.socios and autorizado in socio.lista_autorizados:
            socio.lista_autorizados.remove(autorizado)
            return True
        return False

    def adicionarConsumo(self, socio):
        if socio in self.socios:
            consumo = str(input("Ingrese lo consumido: "))
            valor = int(input("Ingrese el valor: $"))
            nuevaFact = Factura(consumo, valor, socio.cedula)
            self.facturas.append(nuevaFact)
            socio.consumos.append(nuevaFact)
            return True
        return False

    def pagarConsumo(self, socio, factura):
        if socio in self.socios and factura in socio.consumos:
            socio.consumos.remove(factura)
            return True
        return False
    
    def modificarSocio(self, socio):
        if socio in self.socios:
            socio.nombre = str(input("Ingrese el nuevo nombre: "))
            socio.cedula = str(input("Ingrese la nueva cedula: "))
            return True
        return False

    def modificarConsumo(self, socio):
        if socio in self.socios:
            for consumo in socio.consumos:
                consumo.consumo = str(input("Ingrese el nuevo consumo: "))
                consumo.valor = int(input("Ingrese el nuevo valor: $"))
                return True
            return False
    
    def modificarAutorizado(self, socio, autorizado):
        if socio in self.socios and autorizado in socio.lista_autorizados:
            autorizado.nombre = str(input("Ingrese el nuevo nombre: "))
            autorizado.cedula = str(input("Ingrese la nueva cedula: "))
            return True
        return False

    def consultarAutorizadoConSocio(self, socio):
        if socio in self.socios:
            print(socio.nombre, socio.cedula)
            for usuario in socio.lista_autorizados:
                print(usuario.nombre, usuario.cedula)
            
    
    def consultarConsumosSocio(self, socio):
        if socio in self.socios:
            for consumo in socio.consumos:
                print(consumo.consumo, consumo.valor)
                return True
            return False
    
    def totalConsumos(self, socio):
        if socio in self.socios:
            total = 0
            for consumo in socio.consumos:
                total += consumo.valor
            return total
        
    def totalConsumosTipoSocio(self, socio):
        if socio in self.socios:
            total = 0
            for consumo in socio.consumos:
                total += consumo.valor
            return total
                
class Autorizado:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.conSocio = False  # identifica si el autorizado está con un socio :)

class Socio:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.lista_autorizados = []
        self.consumos = []

class Platinum(Socio):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limiteAutorizados = 999
        self.descuento = 0.15

class Gold(Socio):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limiteAutorizados = 10
        self.descuento = 0.1

class Silver(Socio):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limiteAutorizados = 5
        self.descuento = 0.05

class Factura:
    def __init__(self, consumo, valorConsumido, cedula):
        self.consumo = consumo
        self.valorConsumido = valorConsumido
        self.cedula = cedula

def menuClubUdenar(club):
    print("Seleccione una opción:")
    print("1. Manejo de socios")
    print("2. Manejo de Autorizados")
    print("3. Manejo de consumos")
    print("4. Estadisticas")
    print("5. Salir")

    opcion = input("Ingrese su opción: ")

    match opcion:
        case "1":
            menuManejarSocios(club)
        case "2":
            menuManejarAutorizados(club)
        case "3":
            menuManejarConsumos(club)
        case "4":
            menuInformes()
        case "5":
            print("Gracias por utilizar el sistema")
        case _:
            print("Opción no válida. Por favor, intenta de nuevo.")

def menuManejarSocios():
    print("Seleccione una opción:")
    print("1. Crear socio")
    print("2. Modificar socio")
    print("3. Eliminar socio")
    print("4. Consultar socios autorizados")
    print("5. Regresar")

    opcion = input("Ingrese su opción: ")

    match opcion:
        case "1":
            club.adicionarSocio()
        case "2":
            # Implementar la lógica para modificar un socio
            print("Funcionalidad de modificar socio no implementada.")
        case "3":
            # Implementar la lógica para eliminar un socio
            cedula = input("Ingrese la cédula del socio a eliminar: ")
            socio_a_eliminar = next((socio for socio in club.socios if socio.cedula == cedula), None)
            if socio_a_eliminar:
                club.eliminarSocio(socio_a_eliminar)
                print("Socio eliminado exitosamente.")
            else:
                print("Socio no encontrado.")
        case "4":
            cedula = input("Ingrese la cédula del socio para consultar autorizados: ")
            club.consultarSocioConAutorizados(cedula)
        case "5":
            return
        case _:
            print("Opción no válida. Por favor, intenta de nuevo.")

def menuManejarAutorizados():
    print("Seleccione una opción:")
    print("1. Adicionar autorizado")
    print("2. Modificar autorizado")
    print("3. Eliminar autorizado")
    print("4. Consultar autorizado con socio")
    print("5. Regresar")

    opcion = input("Ingrese su opción: ")

    match opcion:
        case "1":
            cedula = input("Ingrese la cédula del socio: ")
            socio = next((socio for socio in club.socios if socio.cedula == cedula), None)
            if socio:
                club.adicionarAutorizado(socio)
                print("Autorizado añadido exitosamente.")
            else:
                print("Socio no encontrado.")
        case "2":
            # Implementar la lógica para modificar un autorizado
            print("Funcionalidad de modificar autorizado no implementada.")
        case "3":
            cedula_socio = input("Ingrese la cédula del socio: ")
            socio = next((socio for socio in club.socios if socio.cedula == cedula_socio), None)
            if socio:
                cedula_autorizado = input("Ingrese la cédula del autorizado a eliminar: ")
                autorizado_a_eliminar = next((autorizado for autorizado in socio.lista_autorizados if autorizado.cedula == cedula_autorizado), None)
                if autorizado_a_eliminar:
                    club.eliminarAutorizado(socio, autorizado_a_eliminar)
                    print("Autorizado eliminado exitosamente.")
                else:
                    print("Autorizado no encontrado.")
            else:
                print("Socio no encontrado.")
        case "4":
            cedula_autorizado = input("Ingrese la cédula del autorizado para consultar: ")
            # Implementar la lógica para consultar un autorizado
            print("Funcionalidad de consultar autorizado no implementada.")
        case "5":
            return
        case _:
            print("Opción no válida. Por favor, intenta de nuevo.")

def menuManejarConsumos():
    print("Seleccione una opción:")
    print("1. Adicionar consumo")
    print("2. Pagar consumo")
    print("3. Modificar consumo")
    print("4. Consultar consumo socio")
    print("5. Regresar")

    opcion = input("Ingrese su opción: ")

    match opcion:
        case "1":
            cedula = input("Ingrese la cédula del socio: ")
            socio = next((socio for socio in club.socios if socio.cedula == cedula), None)
            if socio:
                club.registrarConsumo(socio)
                print("Consumo registrado exitosamente.")
            else:
                print("Socio no encontrado.")
        case "2":
            # Implementar la lógica para pagar un consumo
            print("Funcionalidad de pagar consumo no implementada.")
        case "3":
            # Implementar la lógica para modificar un consumo
            print("Funcionalidad de modificar consumo no implementada.")
        case "4":
            cedula = input("Ingrese la cédula del socio para consultar consumos: ")
            socio = next((socio for socio in club.socios if socio.cedula == cedula), None)
            if socio:
                print(f"Consumos de {socio.nombre}:")
                for consumo in socio.lista_consumos:
                    print(f"- {consumo.descripcion}: {consumo.monto}")
            else:
                print("Socio no encontrado.")
        case "5":
            return
        case _:
            print("Opción no válida. Por favor, intenta de nuevo.")

def menuInformes():
    print("Seleccione una opción:")
    print("1. Consultar estadísticas de socios")
    print("2. Consultar estadísticas de consumos")
    print("3. Regresar")

    opcion = input("Ingrese su opción: ")

    match opcion:
        case "1":
            # Implementar la lógica para consultar estadísticas de socios
            print("Funcionalidad de consultar estadísticas de socios no implementada.")
        case "2":
            # Implementar la lógica para consultar estadísticas de consumos
            print("Funcionalidad de consultar estadísticas de consumos no implementada.")
        case "3":
            return
        case _:
            print("Opción no válida. Por favor, intenta de nuevo.")

def menuPrincipal():
    while True:
        print("Menú Principal:")
        print("1. Manejo de socios")
        print("2. Manejo de autorizados")
        print("3. Manejo de consumos")
        print("4. Estadísticas")
        print("5. Salir")

        opcion = input("Ingrese su opción: ")

        match opcion:
            case "1":
                menuManejarSocios()
            case "2":
                menuManejarAutorizados()
            case "3":
                menuManejarConsumos()
            case "4":
                menuInformes()
            case "5":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    club = Club()  
    menuPrincipal() 