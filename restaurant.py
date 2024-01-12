import os

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = {}
        self.cliente = {}
        self.propina = 0
        self.mesero = ""

    def agregar_item_menu(self, nombre, precio):
        self.menu[nombre] = precio

    def ingresar_datos_cliente(self):
        print("Ingrese los datos del cliente:")
        self.cliente["nombre"] = input("Nombre: ")
        self.cliente["correo"] = self.validar_correo()
        self.cliente["telefono"] = self.validar_numero("Teléfono: ")

    def validar_correo(self):
        while True:
            correo = input("Correo electrónico: ")
            if "@" in correo:
                return correo
            else:
                print("El correo electrónico no es válido. Intente nuevamente.")

    def validar_numero(self, mensaje):
        while True:
            numero = input(mensaje)
            if numero.isdigit():
                return numero
            else:
                print("El valor ingresado no es numérico. Intente nuevamente.")

    def ingresar_pedido(self):
        self.pedido = {}
        continuar = "si"

        while continuar.lower() == "si":
            os.system("clear")  # Limpia la consola antes de mostrar el menú
            print("Menu:")
            for item, precio in self.menu.items():
                print(f"{item} - ${precio}")

            item = input("\nIngrese el nombre del alimento o bebida: ")
            if item in self.menu:
                cantidad = self.validar_numero("Ingrese la cantidad: ")
                precio_unitario = self.menu[item]
                precio_total = int(cantidad) * precio_unitario

                self.pedido[item] = {
                    "cantidad": int(cantidad),
                    "precio_unitario": precio_unitario,
                    "precio_total": precio_total
                }
            else:
                print("El alimento o bebida ingresado no está en el menú.")

            continuar = input("\n¿Desea agregar otro ítem al pedido? (si/no): ")

    def agregar_propina(self):
        self.propina = self.validar_numero("Ingrese el monto de propina para el mesero: ")
        self.mesero = input("Ingrese el nombre del mesero: ")

    def generar_factura(self):
        os.system("clear")  # Limpia la consola antes de mostrar la factura

        # Generar encabezado de la factura
        nombre_restaurante_centro = self.nombre.center(50, " ")
        print(f"{nombre_restaurante_centro}\n")
        print("Factura:")
        print(f"Cliente: {self.cliente['nombre']}")
        print(f"Correo electrónico: {self.cliente['correo']}")
        print(f"Teléfono: {self.cliente['telefono']}")
        print("\nPedido:")
        for item, detalles in self.pedido.items():
            print(f"{item}: {detalles['cantidad']} x ${detalles['precio_unitario']} = ${detalles['precio_total']}")

        print(f"\nPropina para {self.mesero}: ${self.propina}")

# Crear instancia del restaurante
restaurante = Restaurante("Restaurante delicioso")

# Agregar items al menú
restaurante.agregar_item_menu("Hamburguesa", 10)
restaurante.agregar_item_menu("Pizza", 12)
restaurante.agregar_item_menu("Ensalada", 8)
restaurante.agregar_item_menu("Refresco", 2)
restaurante.agregar_item_menu("Café", 3)
restaurante.agregar_item_menu("Sopa", 6)
restaurante.agregar_item_menu("Pasta", 10)
restaurante.agregar_item_menu("Postre", 5)

# Ingresar datos del cliente
restaurante.ingresar_datos_cliente()

# Ingresar pedido
restaurante.ingresar_pedido()

# Agregar propina
restaurante.agregar_propina()

# Generar factura
restaurante.generar_factura()
