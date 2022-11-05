from animal import Animal

class Perro(Animal):
    def emitir_sonido(self):
        self.edad = int(input("Ingrese la edad del perro: "))
        if self.edad < 3:
            print("auf auf")
        elif self.edad >=3:
            print("guau guau")