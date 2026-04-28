lista_empleados = []
lista_prestamos = []

class Empleado:
    contador_id = 1
    def __init__(self, cedula, nombre, sueldo):
        self.id = Empleado.contador_id
        Empleado.contador_id += 1
        self.cedula = cedula
        self.nombre = nombre
        self.sueldo = sueldo

        

    def __str__(self):
        return f"\nId: {self.id}\n | Nombre: {self.nombre}\n | Cedula: {self.cedula}\n | Sueldo: {self.sueldo}\n"
    
def crear_empleado():
    cedula = input("Ingresar cedula:\n")
    nombre = input("Ingresar nombre:\n")

    while True:
            try:
                sueldo = float(input("Ingresar sueldo:\n"))
                if sueldo < 0:
                    print("Dato invalido")
                    continue
                break
            except:
                print("Ingrese un numero valido")

    guardar = int(input("Desea guardar?:\n 1-Si\n 2-No\n"))

    if guardar == 1:
        empleado = Empleado(cedula, nombre, sueldo)
        lista_empleados.append(empleado)
        print("Empleado guardado correctamente")
    elif guardar == 2:
        print("No se ha guardado al empleado")
        return
    else:
        print("Dato invalido")



    return empleado

def mostrar_empleado():
    if not lista_empleados:
        print("No hay empleados")
        return

    for empleados in lista_empleados:
        print(empleados)








class Prestamo:
    contador_id = 1
    def __init__(self, empleado, fecha_prestamo, monto, numero_cuotas, cuota, saldo):
        self.id = Prestamo.contador_id
        Prestamo.contador_id += 1
        self.empleado = empleado
        self.fecha_prestamo = fecha_prestamo
        self.monto = monto
        self.numero_cuotas = numero_cuotas
        self.cuota = cuota
        self.saldo = saldo

    def __str__(self):
        return f"ID préstamo: {self.id} | Empleado: {self.empleado.nombre} | Monto: {self.monto} | Saldo: {self.saldo} | Fecha: {self.fecha_prestamo}"

def verificar_empleados():
    if not lista_empleados:
        print("No hay empleados")
        return None
    
    while True:
        try:
            mostrar_empleado()
            id_empleado = int(input("Ingresar el ID del empleado o 0 para cancelar: \n"))

            if id_empleado == 0:
                return None

            for empleado in lista_empleados:
                if empleado.id == id_empleado:
                    return empleado
                
            print("Empleado no encontrado intente otra vez")
                

        except ValueError:
            print("Ingresar un ID Valido")
        



def crear_prestamo():
    empleado = verificar_empleados()

    if empleado is None:
        print("Empleado no encontrado")
        return
    
    fecha_prestamo = input("Ingresar fecha del prestamo:\n")

    while True:
            try:
                monto = float(input("Ingresar el monto"))
                if monto <= 0:
                    print("El monto debe ser mayor a cero")
                    continue
                break
            except ValueError:
                    print("Ingresar un numero de monto valido")

    while True:
            try:
                numero_cuotas = int(input("Ingresar el numero de cuotas"))
                if numero_cuotas <= 0:
                    print("El numero de cuotas debe de ser mayor a 0")
                    continue
                break
            except ValueError:
                print("Ingresar un numero de cuota")

    cuota = monto / numero_cuotas
    saldo = monto

    prestamo = Prestamo(empleado, fecha_prestamo, monto, numero_cuotas, cuota, saldo)
    lista_prestamos.append(prestamo)
    print("Prestamo creado correctamente")

def mostrar_prestamos():

    if not lista_prestamos:
        print("No hay prestamos")

    for prestamo in lista_prestamos:
        print(prestamo)















class Pago:
    contador_id = 1
    def __init__(self, id_prestamo, fecha_pago, valor_pago):
        self.id = 1
        self.id += Pago.contador_id
        self.id_prestamo = id_prestamo
        self.fecha_pago = fecha_pago
        self.valor_pago = valor_pago


while True:
    print("===Menu===")
    opcion = int(input(f"\nElegir opcion:\n 1-Crear Empleado\n 2-Crear Prestamo\n 3-Mostrar prestamo\n 4-Registrar Pago\n 5-Eliminar\n 6-Estadisticas\n 7-Mosrar Empleado\n 8-Salir\n"))
    match opcion:
        case 1:
            crear_empleado()
        case 2:
            crear_prestamo()
        case 3:
            mostrar_prestamos()
        case 8:
            print("Saliendo del sistema....")
            break
        case _:
            print("Ingresar dato valido")