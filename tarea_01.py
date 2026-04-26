lista_empleados = []

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
        self.id = 1
        self.id += Prestamo.contador_id
        self.empleado = empleado
        self.fecha_prestamo = fecha_prestamo
        self.monto = monto
        self.numero_cuota = numero_cuotas
        self.cuota = cuota
        self.saldo = saldo










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
    opcion = int(input(f"\nElegir opcion:\n 1-Crear Empleado\n 2-Crear Prestamo\n 3-Consultar\n 4-Registrar Pago\n 5-Eliminar\n 6-Estadisticas\n 7-Mosrar Empleado\n 8-Salir\n"))
    match opcion:
        case 1:
            crear_empleado()
        case 7:
            mostrar_empleado()
        case 8:
            print("Saliendo del sistema....")
            break
        case _:
            print("Ingresar dato valido")