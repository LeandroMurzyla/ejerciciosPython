class Vehiculo:
    def __init__(self, marca=str, ruedas=int, color=str, enMarcha=bool):
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = enMarcha

    def arrancar(self, estado):
        if self.enMarcha == True:
            estado = 'Automovil encendido'
        else:
            estado = 'Automovil apagado'
        return estado

    def tipoVehiculo(self, tipo):
        if self.ruedas == 4:
            tipo = 'Automovil'
        elif self.ruedas == 2:
            tipo = 'Motocicleta'
        else:
            tipo = 'Vehiculo desconocido'
        return tipo

    def mostrar(self):
        tipo = self.tipoVehiculo(self.ruedas)
        estado = self.arrancar(self.enMarcha)
        return f'''
        Marca: {self.marca}
        Tipo de Vehiculo: {tipo}
        Color: {self.color}
        Estado: {estado}
        '''


vehiculo1 = Vehiculo('Toyota', 2, 'Negro', False)
print(vehiculo1.mostrar())