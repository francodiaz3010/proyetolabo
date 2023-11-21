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


