class animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class perro(animal):
    def sonido(self):
        print('Guuauu!')

class vaca(animal):
    def sonido(self):
        print('Muuu!')

class gato(animal):
    def sonido(self):
        print('Miiiaauuu!')