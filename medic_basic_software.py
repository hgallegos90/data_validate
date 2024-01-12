class Paciente:
    def __init__(self, historia_laboral, cedula, nombres_completos, edad):
        self.historia_laboral = historia_laboral
        self.cedula = cedula
        self.nombres_completos = nombres_completos
        self.edad = edad
        self.sintomas = []

    def agregar_sintoma(self, sintoma):
        self.sintomas.append(sintoma)

    def tiene_covid(self):
        return (
            "fiebre" in self.sintomas
            and "fatiga" in self.sintomas
            and "pérdida de olfato y gusto" in self.sintomas
        )


def validar_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False


def solicitar_datos_paciente():
    print("----- Ingrese datos del paciente -----")
    while True:
        historia_laboral = input("Historia Laboral: ")
        if validar_entero(historia_laboral):
            break
        else:
            print("Error: La historia laboral debe ser un número.")

    while True:
        cedula = input("Cédula: ")
        if validar_entero(cedula):
            break
        else:
            print("Error: La cédula debe ser un número.")

    nombres_completos = input("Nombres completos: ")

    while True:
        edad = input("Edad: ")
        if validar_entero(edad):
            break
        else:
            print("Error: La edad debe ser un número.")

    return historia_laboral, cedula, nombres_completos, edad


def solicitar_sintomas():
    print("----- Ingrese síntomas del paciente -----")

    sintomas_disponibles = [
        "fiebre",
        "fatiga",
        "tos",
        "gripe",
        "pérdida de olfato y gusto",
        "dolor de cabeza",
        "dolor de garganta",
        "dificultad para respirar",
        "náuseas",
        "diarrea",
    ]

    sintomas_elegidos = []

    while len(sintomas_elegidos) < 4:
        print("Seleccione un síntoma (ingrese el número):")
        for i, sintoma in enumerate(sintomas_disponibles):
            print(f"{i+1}. {sintoma}")

        opcion = input("Opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(sintomas_disponibles):
            sintoma_elegido = sintomas_disponibles[int(opcion) - 1]
            if sintoma_elegido not in sintomas_elegidos:
                sintomas_elegidos.append(sintoma_elegido)
                respuesta = input("¿Desea ingresar otro síntoma? (S/N): ")
                if respuesta.upper() != "S":
                    break
            else:
                print("Error: Ya ha seleccionado ese síntoma.")
        else:
            print("Error: Opción inválida. Ingrese un número válido.")

    return sintomas_elegidos


def generar_informe(pacientes):
    print("\n" + "CENTRO MÉDICO MARÍA AUXILIADORA".center(50))  # Centro el nombre del centro médico en pantalla
    print("\nHIST.CLÍN\tCÉDULA\t\tNOMBRES\t\t\tCOVID-19")
    count = 0
    for paciente in pacientes:
        count += 1
        print(
            f" {paciente.historia_laboral}\t\t{paciente.cedula}\t{paciente.nombres_completos}\t\t{'SI' if paciente.tiene_covid() else 'NO'}"
        )
    print("\nCANTIDAD DE PACIENTES CON COVID-19:", count)


def main():
    pacientes = []

    while True:
        historia_laboral, cedula, nombres_completos, edad = solicitar_datos_paciente()
        paciente = Paciente(historia_laboral, cedula, nombres_completos, edad)
        paciente.sintomas = solicitar_sintomas()
        prescripcion_medica = input("Registre la prescripción médica: ")

        pacientes.append(paciente)

        respuesta = input("¿DESEA INGRESAR OTRO PACIENTE? (S/N): ")
        if respuesta.upper() != "S":
            break

    generar_informe(pacientes)
    print("\n---- GRACIAS POR USAR EL SISTEMA -----")


if __name__ == "__main__":
    main()
