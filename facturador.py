import re

class Producto:
    def __init__(self, nombre, codigo, precio, cantidad):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        return self.precio * self.cantidad

    def detalle_factura(self):
        return f"{self.codigo}\t{self.nombre.ljust(20)}\t{self.precio:.2f}\t\t{self.cantidad}\t\t{self.subtotal():.2f}\n"


class Cliente:
    def __init__(self, cedula, nombres_apellidos, correo_electronico, direccion):
        self.cedula = cedula
        self.nombres_apellidos = nombres_apellidos
        self.correo_electronico = correo_electronico
        self.direccion = direccion
        self.productos = []
        self.total_cantidad = 0

    def agregar_producto(self, producto):
        if len(self.productos) >= 5:
            print("Error: Máximo 5 artículos por cliente.")
            return

        self.productos.append(producto)
        self.total_cantidad += producto.cantidad

    def verificar_producto_existente(self, codigo, nombre):
        for producto in self.productos:
            if producto.codigo == codigo or producto.nombre == nombre:
                return True
        return False


def ingresar_texto(mensaje):
    while True:
        texto = input(mensaje)
        if texto.isalpha():
            return texto
        else:
            print("Error: Ingrese un valor de texto válido.")


def ingresar_opcion(mensaje, opciones):
    while True:
        opcion = input(mensaje).upper()
        if opcion in opciones:
            return opcion
        else:
            print("Error: Ingrese una opción válida.")


def ingresar_valor_float(mensaje):
    while True:
        valor = input(mensaje)
        try:
            valor_float = float(valor)
            return valor_float
        except ValueError:
            print("Error: Ingrese un valor numérico.")


def ingresar_valor_entero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            valor_entero = int(valor)
            return valor_entero
        except ValueError:
            print("Error: Ingrese un valor entero.")


def ingresar_correo_electronico(clientes):
    while True:
        correo = input("Correo electrónico: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            if not any(cliente.correo_electronico == correo for cliente in clientes):
                return correo
            else:
                print("Error: El correo electrónico ya ha sido ingresado.")
        else:
            print("Error: Ingrese un correo electrónico válido.")


def main():
    clientes = []

    while True:
        cedula = ingresar_valor_entero("Cédula: ")
        if any(cliente.cedula == cedula for cliente in clientes):
            print("Error: La cédula ya ha sido ingresada.")
            continue

        nombres_apellidos = ingresar_texto("Nombres y Apellidos: ")
        correo_electronico = ingresar_correo_electronico(clientes)
        direccion = ingresar_texto("Dirección: ")

        cliente = Cliente(cedula, nombres_apellidos, correo_electronico, direccion)

        while True:
            nombre = ingresar_texto("Nombre: ")
            codigo = ingresar_texto("Código: ")
            precio = ingresar_valor_float("Precio: ")
            cantidad = ingresar_valor_entero("Cantidad: ")

            producto = Producto(nombre, codigo, precio, cantidad)

            if cliente.verificar_producto_existente(codigo, nombre):
                print("Error: El código o nombre del producto ya ha sido ingresado.")
                continue

            cliente.agregar_producto(producto)

            if len(cliente.productos) >= 5:
                print("Error: Máximo 5 artículos por cliente.")
                break

            respuesta = ingresar_opcion("Desea ingresar otro artículo S/N: ", ["S", "N"])
            if respuesta == "N":
                break

        clientes.append(cliente)

        respuesta = ingresar_opcion("Desea ingresar otro cliente S/N: ", ["S", "N"])
        if respuesta == "N":
            break

    print("\n---- GRACIAS POR USAR EL SISTEMA -----\n")

    for i, cliente in enumerate(clientes):
        factura = cliente.generar_factura(i + 1)
        print(factura)


if __name__ == "__main__":
    main()
