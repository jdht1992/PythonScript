class Cliente:

    def __init__(self, dni, nombre, apellidos):

        self.dni = dni
        self.nombre = nombre
        self.apellido = apellidos

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'
        
class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes
        
    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return 
        print('Cliente no encontrado')

    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(f'{str(c)} - BORRADO')
                return 
        print('cliente no encontrado')

#creacion del cliente 
charlie = Cliente(nombre='Charlie', apellidos='Sanchez Ortega', dni='1111111A')
juan = Cliente('22222222B',"Juan","Sanchez Gonzalez")

#creacion de empresa
empresa = Empresa(clientes=[charlie,juan])

#mostrar un cliente
empresa.mostrar_cliente(dni='1111111A')

empresa.borrar_cliente('22222222B')



