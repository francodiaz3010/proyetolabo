class Destino:
    def __init__(self, nombre_destino):
        self.nombre_destino = nombre_destino

class Pasajero:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

class Viaje:
    def __init__(self, fecha, hora, pasajero, destino):
        self.fecha = fecha
        self.hora = hora
        self.pasajero = pasajero
        self.destino = destino

class MatrizViajes:
    def __init__(self):
        self.matriz_viajes = {}

    def agregar_viaje(self, viaje):
        destino = viaje.destino.nombre_destino
        if destino not in self.matriz_viajes:
            self.matriz_viajes[destino] = []
        self.matriz_viajes[destino].append(viaje)

    def imprimir_matriz(self):
        for destino, viajes in self.matriz_viajes.items():
            print(f"Destino: {destino}")
            for viaje in viajes:
                print(f"  Fecha: {viaje.fecha}, Hora: {viaje.hora}, Pasajero: {viaje.pasajero.nombre}")

# Ejemplo de uso:

destino1 = Destino("Ciudad A")
destino2 = Destino("Ciudad B")

pasajero1 = Pasajero("Juan", "Pérez", "12345678")
pasajero2 = Pasajero("Ana", "Gomez", "98765432")

viaje1 = Viaje("2023-11-20", "10:00", pasajero1, destino1)
viaje2 = Viaje("2023-11-25", "15:30", pasajero2, destino2)
viaje3 = Viaje("2023-12-01", "08:45", pasajero1, destino1)

matriz_viajes = MatrizViajes()
matriz_viajes.agregar_viaje(viaje1)
matriz_viajes.agregar_viaje(viaje2)
matriz_viajes.agregar_viaje(viaje3)

# Imprimir la matriz organizada por destino
matriz_viajes.imprimir_matriz()
