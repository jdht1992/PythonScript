class coche:

    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False
    #Para cambiar el estado de un atributo se puede hacer mediante un metodo asingnandole un valor desde el methodo a la variable encapsulada
    def arranca(self, arrancamos):
        self.__enmarcha = arrancamos

        if self.__enmarcha:
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'

    def estado(self):
        print(f'El coche tiene {self.__ruedas} ruedas. un ancho de {self.anchoChasis} y un largo de {self.largoChasis}')

miCoche = coche()
#No se puede acceder al atributo por que esta encapsulado
miCoche.__ruedas = 5
print(miCoche.arranca(True))
miCoche.estado()
#Para acceder a los atributos encapsulado tienes que ser mediante la instancia, la clase y el atributo
print(miCoche._coche__ruedas)

#Segunda instancia cambiando un atributo encapsulado desde un metodo
miCoche2 = coche()
print(miCoche2.arranca(True))

