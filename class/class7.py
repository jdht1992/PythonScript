class Galleta:

    chocolate = False

    def __init__(self, sabor=None, forma=None):
        self.sabor = sabor
        self.forma = forma
        if sabor is not None and forma is not None:
            print(f'se acaba de crear una galleta {self.sabor} {self.forma}')

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if self.chocolate:
            print('Soy una galleta chocolate')
        else:
            print('soy una galleta sin chocolate')

g = Galleta()
