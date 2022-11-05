from animal import Animal

class Bovino(Animal):
    def __init__(self):
        self.propietario=""
        self.fecha_vacunacion=""
        self.establo=0
    
    def pastar(self):
        if self.establo > 5:
            print("pastar")
        elif self.establo <= 5:
            print("no pastar")
    
    def emitir_sonido(self):
        print("muu")